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
    'assets/css/style.css',
]

DEPLOY_DIRECTORIES = [
    'shows/',  # All weekly show directories
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

def create_remote_directory(ftp, remote_path):
    """Create directory on FTP server if it doesn't exist"""
    try:
        ftp.cwd(remote_path)
        # Change back to base directory
        ftp.cwd(FTP_REMOTE_DIR if FTP_REMOTE_DIR else '/')
    except ftplib.error_perm:
        # Directory doesn't exist, create it
        try:
            ftp.mkd(remote_path)
            print(f"  📁 Created directory: {remote_path}")
        except Exception as e:
            print(f"  ⚠️  Could not create directory {remote_path}: {e}")

def upload_file(ftp, local_path, remote_path):
    """Upload a single file to FTP server"""
    try:
        with open(local_path, 'rb') as file:
            ftp.storbinary(f'STOR {remote_path}', file)
        print(f"  ✅ Uploaded: {remote_path}")
        return True
    except Exception as e:
        print(f"  ❌ Failed to upload {local_path}: {e}")
        return False

def upload_directory(ftp, local_dir, remote_dir=''):
    """Recursively upload directory contents"""
    local_path = Path(local_dir)
    
    if not local_path.exists():
        print(f"  ⚠️  Directory not found: {local_dir}")
        return
    
    for item in local_path.rglob('*'):
        if item.is_file():
            # Calculate relative path
            relative_path = item.relative_to(local_path.parent)
            remote_path = str(relative_path).replace('\\\\', '/')
            
            # Create remote directory structure
            remote_dir_path = '/'.join(remote_path.split('/')[:-1])
            if remote_dir_path:
                create_remote_directory(ftp, remote_dir_path)
            
            # Upload file
            upload_file(ftp, str(item), remote_path)

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
        print("\\n📤 Uploading core files...")
        for file_path in DEPLOY_FILES:
            if os.path.exists(file_path):
                # Create directory structure if needed
                remote_dir = '/'.join(file_path.split('/')[:-1])
                if remote_dir:
                    create_remote_directory(ftp, remote_dir)
                
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
        sys.exit(1)
    finally:
        ftp.quit()
        print("\\n🔌 FTP connection closed")

if __name__ == '__main__':
    deploy()
