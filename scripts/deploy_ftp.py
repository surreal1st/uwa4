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
    'shows/',   # All weekly show directories (may not exist yet)
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

def ensure_remote_dir(ftp, remote_path):
    """Ensure a remote directory exists, creating all parent directories as needed"""
    if not remote_path or remote_path == '.':
        return
    
    # Get current directory
    original_dir = ftp.pwd()
    
    # Split path into parts
    parts = remote_path.strip('/').split('/')
    
    # Create each directory level
    for i, part in enumerate(parts):
        if not part:
            continue
        
        try:
            # Try to change into directory
            ftp.cwd(part)
        except ftplib.error_perm:
            # Directory doesn't exist, create it
            try:
                ftp.mkd(part)
                print(f"  📁 Created directory: {part}")
                ftp.cwd(part)
            except ftplib.error_perm as e:
                print(f"  ⚠️  Could not create/access directory {part}: {e}")
    
    # Return to original directory
    ftp.cwd(original_dir)

def upload_file(ftp, local_path, remote_path):
    """Upload a single file to FTP server"""
    try:
        print(f"  📤 Uploading: {local_path} → {remote_path}")
        
        # Get directory and filename
        remote_dir = '/'.join(remote_path.split('/')[:-1])
        remote_filename = remote_path.split('/')[-1]
        
        # Ensure directory structure exists
        if remote_dir:
            ensure_remote_dir(ftp, remote_dir)
            # Change to the target directory
            ftp.cwd(FTP_REMOTE_DIR if FTP_REMOTE_DIR != '/' else '/')
            ftp.cwd(remote_dir)
        
        # Upload the file to current directory
        with open(local_path, 'rb') as file:
            ftp.storbinary(f'STOR {remote_filename}', file)
        
        # Return to base directory
        ftp.cwd(FTP_REMOTE_DIR if FTP_REMOTE_DIR != '/' else '/')
        
        print(f"  ✅ Uploaded successfully: {remote_path}")
        return True
    except Exception as e:
        print(f"  ❌ Failed to upload {local_path}: {e}")
        import traceback
        traceback.print_exc()
        return False

def upload_directory(ftp, local_dir):
    """Recursively upload directory contents"""
    local_path = Path(local_dir)
    
    if not local_path.exists():
        print(f"  ⚠️  Directory not found, skipping: {local_dir}")
        return
    
    if not any(local_path.iterdir()):
        print(f"  ⚠️  Directory is empty, skipping: {local_dir}")
        return
    
    print(f"\\n  📂 Processing directory: {local_dir}")
    
    # Get all files in directory recursively
    files_found = False
    for item in local_path.rglob('*'):
        if item.is_file():
            files_found = True
            # Calculate relative path from repository root
            relative_path = str(item).replace('\\\\', '/')
            
            # Upload file
            upload_file(ftp, str(item), relative_path)
    
    if not files_found:
        print(f"  ℹ️  No files found in: {local_dir}")

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
    print(f"📍 Current working directory: {os.getcwd()}")
    
    # List what we're about to deploy
    print(f"\\n📋 Files to deploy:")
    for f in DEPLOY_FILES:
        exists = "✅" if os.path.exists(f) else "❌"
        print(f"  {exists} {f}")
    
    print(f"\\n📋 Directories to deploy:")
    for d in DEPLOY_DIRECTORIES:
        exists = "✅" if os.path.exists(d) else "❌"
        print(f"  {exists} {d}")
    
    # Connect to FTP
    ftp = connect_ftp()
    
    try:
        # Upload individual files
        print("\\n" + "=" * 60)
        print("📤 UPLOADING CORE HTML FILES")
        print("=" * 60)
        for file_path in DEPLOY_FILES:
            if os.path.exists(file_path):
                upload_file(ftp, file_path, file_path)
            else:
                print(f"  ⚠️  File not found: {file_path}")
        
        # Upload directories
        print("\\n" + "=" * 60)
        print("📤 UPLOADING DIRECTORIES")
        print("=" * 60)
        for dir_path in DEPLOY_DIRECTORIES:
            upload_directory(ftp, dir_path)
        
        print("\\n" + "=" * 60)
        print("✅ Deployment completed successfully!")
        print(f"🌐 Files deployed to: {FTP_HOST}{FTP_REMOTE_DIR}")
        print("=" * 60)
        
        # Show final directory structure
        print("\\n📋 Final directory contents:")
        ftp.cwd(FTP_REMOTE_DIR if FTP_REMOTE_DIR != '/' else '/')
        try:
            files = ftp.nlst()
            for f in files:
                print(f"   - {f}")
        except:
            print("   (cannot list)")
        
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
