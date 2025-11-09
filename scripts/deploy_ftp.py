#!/usr/bin/env python3
"""
FTP Deployment Script for UWA Website
Uploads all website files to the configured FTP server
"""

import os
import ftplib
from pathlib import Path
import sys

# FTP Configuration from environment variables
FTP_HOST = os.environ.get('FTP_HOST')
FTP_USERNAME = os.environ.get('FTP_USERNAME')
FTP_PASSWORD = os.environ.get('FTP_PASSWORD')
FTP_PORT = int(os.environ.get('FTP_PORT', '21'))
FTP_REMOTE_DIR = os.environ.get('FTP_REMOTE_DIR', '/')  # Remote directory on server

# Files and directories to deploy
DEPLOY_FILES = [
    'index.html',
    'about.html',
    'results.html',
    'archive.html',
]

DEPLOY_DIRECTORIES = [
    'assets/',  # CSS and other assets
    'shows/',   # All weekly show directories
]

def connect_ftp():
    """Establish FTP connection"""
    print(f"Connecting to FTP server: {FTP_HOST}:{FTP_PORT}")
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_HOST, FTP_PORT)
        ftp.login(FTP_USERNAME, FTP_PASSWORD)
        print(f"✅ Connected successfully as {FTP_USERNAME}")
        
        # Change to remote directory
        if FTP_REMOTE_DIR and FTP_REMOTE_DIR != '/':
            print(f"📁 Changing to remote directory: {FTP_REMOTE_DIR}")
            try:
                ftp.cwd(FTP_REMOTE_DIR)
                print(f"✅ Working in: {FTP_REMOTE_DIR}")
            except ftplib.error_perm:
                print(f"⚠️  Remote directory doesn't exist, creating: {FTP_REMOTE_DIR}")
                # Create directory structure
                parts = FTP_REMOTE_DIR.strip('/').split('/')
                current = ''
                for part in parts:
                    current = f"{current}/{part}" if current else part
                    try:
                        ftp.mkd(current)
                        print(f"  📁 Created: {current}")
                    except ftplib.error_perm:
                        # Directory already exists
                        pass
                ftp.cwd(FTP_REMOTE_DIR)
        
        return ftp
    except Exception as e:
        print(f"❌ FTP connection failed: {e}")
        sys.exit(1)

def ensure_remote_directory(ftp, remote_path):
    """Ensure directory exists on FTP server, creating if necessary"""
    if not remote_path or remote_path == '.':
        return
    
    parts = remote_path.strip('/').split('/')
    current_path = FTP_REMOTE_DIR if FTP_REMOTE_DIR and FTP_REMOTE_DIR != '/' else ''
    
    for part in parts:
        if not part:
            continue
        current_path = f"{current_path}/{part}".lstrip('/')
        try:
            ftp.cwd(current_path)
        except ftplib.error_perm:
            try:
                ftp.mkd(current_path)
                print(f"  📁 Created directory: {current_path}")
            except ftplib.error_perm as e:
                # Might already exist or permission issue
                pass
    
    # Return to base directory
    if FTP_REMOTE_DIR and FTP_REMOTE_DIR != '/':
        ftp.cwd(FTP_REMOTE_DIR)

def upload_file(ftp, local_path, remote_path):
    """Upload a single file to FTP server"""
    try:
        # Ensure the directory exists
        remote_dir = '/'.join(remote_path.split('/')[:-1])
        if remote_dir:
            ensure_remote_directory(ftp, remote_dir)
        
        with open(local_path, 'rb') as file:
            ftp.storbinary(f'STOR {remote_path}', file)
        print(f"  ✅ Uploaded: {remote_path}")
        return True
    except Exception as e:
        print(f"  ❌ Failed to upload {local_path}: {e}")
        return False

def upload_directory(ftp, local_dir):
    """Recursively upload directory contents"""
    local_path = Path(local_dir)
    
    if not local_path.exists():
        print(f"  ⚠️  Directory not found: {local_dir}")
        return
    
    print(f"  📂 Uploading directory: {local_dir}")
    
    # Get all files in directory recursively
    for item in local_path.rglob('*'):
        if item.is_file():
            # Calculate relative path from repository root
            relative_path = str(item).replace('\\\\', '/')
            
            # Upload file
            upload_file(ftp, str(item), relative_path)

def deploy():
    """Main deployment function"""
    print("=" * 60)
    print("UWA Website Deployment")
    print("=" * 60)
    
    # Validate credentials
    if not all([FTP_HOST, FTP_USERNAME, FTP_PASSWORD]):
        print("❌ Missing FTP credentials in environment variables")
        print("Required: FTP_HOST, FTP_USERNAME, FTP_PASSWORD")
        sys.exit(1)
    
    print(f"\\n📍 Target directory: {FTP_REMOTE_DIR or '/ (root)'}")
    
    # Connect to FTP
    ftp = connect_ftp()
    
    try:
        # Upload individual files
        print("\\n📤 Uploading core HTML files...")
        for file_path in DEPLOY_FILES:
            if os.path.exists(file_path):
                upload_file(ftp, file_path, file_path)
            else:
                print(f"  ⚠️  File not found: {file_path}")
        
        # Upload directories
        print("\\n📤 Uploading directories...")
        for dir_path in DEPLOY_DIRECTORIES:
            upload_directory(ftp, dir_path)
        
        print("\\n" + "=" * 60)
        print("✅ Deployment completed successfully!")
        print(f"🌐 Files deployed to: {FTP_HOST}{FTP_REMOTE_DIR}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\\n❌ Deployment failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        ftp.quit()
        print("\\n🔌 FTP connection closed")

if __name__ == '__main__':
    deploy()
