# GitHub Secrets Setup Guide

This document explains how to configure the required GitHub Secrets for the UWA automation system.

## Required Secrets

The automation workflow requires the following secrets to be configured in your GitHub repository:

### 1. ANTHROPIC_API_KEY
- **Purpose:** Authenticate with Claude API for show generation
- **How to get it:** 
  - Go to https://console.anthropic.com/
  - Navigate to API Keys section
  - Create a new API key
- **Format:** `sk-ant-...` (starts with sk-ant-)

### 2. FTP_HOST
- **Purpose:** FTP server hostname for website deployment
- **Format:** Domain name or IP address
- **Example:** `ftp.yourdomain.com` or `192.168.1.100`

### 3. FTP_USERNAME
- **Purpose:** FTP login username
- **Format:** Your FTP account username
- **Example:** `ftpuser@yourdomain.com` or `uwaftp`

### 4. FTP_PASSWORD
- **Purpose:** FTP login password
- **Format:** Your FTP account password
- **Security:** Never commit this to the repository!

### 5. FTP_PORT (Optional)
- **Purpose:** FTP server port number
- **Default:** `21` (standard FTP port)
- **Format:** Numeric port number
- **Example:** `21` or `2121`

## How to Add Secrets to GitHub

1. Go to your GitHub repository: https://github.com/surreal1st/uwa4
2. Click **Settings** (top menu)
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Enter the **Name** (exactly as shown above)
6. Enter the **Value**
7. Click **Add secret**
8. Repeat for each secret

## Testing the Configuration

Once all secrets are configured, you can test the workflow:

### Option 1: Manual Trigger
1. Go to **Actions** tab in your repository
2. Select **Generate UWA Weekly Shows** workflow
3. Click **Run workflow**
4. Click the green **Run workflow** button
5. Monitor the workflow execution

### Option 2: Wait for Scheduled Run
- The workflow runs automatically every Friday at 2:00 AM EST (7:00 AM UTC)

## Verifying Secrets

You cannot view secret values after they're saved (for security), but you can verify they exist:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. You should see all five secret names listed
3. Each should show "Updated X time ago"

## Troubleshooting

### If the workflow fails with "Missing FTP credentials":
- Verify all FTP secrets (FTP_HOST, FTP_USERNAME, FTP_PASSWORD) are set
- Check for typos in secret names (they're case-sensitive)

### If Claude API calls fail:
- Verify ANTHROPIC_API_KEY is set correctly
- Check your API key is active at https://console.anthropic.com/
- Ensure you have sufficient API credits

### If FTP deployment fails:
- Test FTP credentials manually using an FTP client
- Verify FTP_HOST is accessible from GitHub Actions (some hosts block cloud IPs)
- Check FTP_PORT if using non-standard port

## Security Notes

- ✅ **DO:** Store all credentials as GitHub Secrets
- ✅ **DO:** Use a dedicated FTP account with limited permissions
- ❌ **DON'T:** Commit credentials to the repository
- ❌ **DON'T:** Share secret values in issues or pull requests
- ❌ **DON'T:** Log secret values in workflow outputs

## Next Steps

After configuring secrets:

1. ✅ Verify all 5 secrets are configured
2. ⏳ Test manual workflow trigger
3. ⏳ Verify FTP deployment works
4. ⏳ Wait for first scheduled run (Friday 2am EST)

---

*For more information about GitHub Secrets, see: https://docs.github.com/en/actions/security-guides/encrypted-secrets*
