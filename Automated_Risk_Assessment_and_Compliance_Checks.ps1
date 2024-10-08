Here are **5 advanced PowerShell code examples** for **Risk Assessment and Compliance Checks**, focusing on automating risk management tasks and ensuring business compliance with standards and regulations.

---

### 1. **Automated Security Risk Assessment Based on File Integrity**

This script monitors file integrity across sensitive directories, detecting unauthorized changes or potential breaches. It performs a hash check to ensure the integrity of critical files and flags any discrepancies.

```powershell
# Define directories and files for monitoring
$filesToMonitor = @("C:\SensitiveData\config.ini", "C:\SensitiveData\policy.docx")

# Hash files and store initial state
$initialState = @{}
foreach ($file in $filesToMonitor) {
    $initialState[$file] = Get-FileHash $file
}

# Function to check file integrity
function Check-FileIntegrity {
    foreach ($file in $filesToMonitor) {
        $currentHash = Get-FileHash $file
        if ($initialState[$file].Hash -ne $currentHash.Hash) {
            Write-Output "ALERT: Integrity check failed for $file"
        } else {
            Write-Output "File integrity verified for $file"
        }
    }
}

# Schedule integrity check every day
Register-ScheduledTask -Action (New-ScheduledTaskAction -Execute 'Powershell.exe' -Argument '-Command "& {Check-FileIntegrity}"') -Trigger (New-ScheduledTaskTrigger -Daily -At 2AM)
```

### Smart Reasoning:
This script helps in identifying unauthorized file changes, reducing the risk of data breaches and ensuring compliance with internal security protocols. It automates a critical part of risk assessment by regularly checking file integrity.

---

### 2. **Compliance Check for User Access Permissions**

This script audits user access permissions in critical directories and reports on any users with excessive or unauthorized access, ensuring that security policies are upheld.

```powershell
# Define the directory to audit
$directory = "C:\SensitiveData"

# Audit user access permissions
$acl = Get-Acl $directory
$acl.Access | ForEach-Object {
    if ($_.FileSystemRights -eq "FullControl" -and $_.IdentityReference -ne "DOMAIN\Admins") {
        Write-Output "ALERT: Unauthorized FullControl access by $($_.IdentityReference) in $directory"
    }
    else {
        Write-Output "Permissions check passed for $($_.IdentityReference)"
    }
}
```

### Smart Reasoning:
This script ensures that only authorized users have full control over sensitive directories, aligning with security policies and reducing risk. It automates regular auditing of user permissions to maintain compliance.

---

### 3. **Automated Risk Score Calculation for System Vulnerabilities**

This script analyzes system vulnerabilities and calculates a risk score based on predefined metrics, helping businesses prioritize areas that need immediate attention.

```powershell
# Define vulnerability categories and their associated risk weights
$vulnerabilities = @{
    "MissingPatches" = 5;
    "OpenPorts" = 3;
    "OutdatedSoftware" = 4;
    "WeakPasswords" = 5
}

# Sample input data from security scan
$scanResults = @(
    @{ Name = "Server1"; MissingPatches = 3; OpenPorts = 5; OutdatedSoftware = 2; WeakPasswords = 1 },
    @{ Name = "Server2"; MissingPatches = 2; OpenPorts = 0; OutdatedSoftware = 4; WeakPasswords = 3 }
)

# Calculate risk score for each system
foreach ($result in $scanResults) {
    $riskScore = 0
    foreach ($vulnerability in $vulnerabilities.Keys) {
        $riskScore += $result.$vulnerability * $vulnerabilities[$vulnerability]
    }
    Write-Output "Risk score for $($result.Name): $riskScore"
}
```

### Smart Reasoning:
This script provides a quantitative approach to risk management, calculating risk scores for systems based on critical security metrics. It helps prioritize remediation efforts and enhances risk management strategies.

---

### 4. **Automated Compliance Reporting for Industry Standards (e.g., PCI-DSS)**

This script automatically generates a compliance report for an organization based on industry standards like PCI-DSS. It checks for compliance criteria such as password policies, encryption standards, and audit logging.

```powershell
# Define compliance standards and checks
$complianceChecks = @(
    @{ Standard = "PasswordComplexity"; Requirement = "Must include upper, lower, digits"; Check = { Test-PasswordComplexity } },
    @{ Standard = "DataEncryption"; Requirement = "Sensitive data must be encrypted"; Check = { Test-DataEncryptionStatus } },
    @{ Standard = "AuditLogging"; Requirement = "Audit logs must be enabled"; Check = { Test-AuditLogsEnabled } }
)

# Define compliance check functions
function Test-PasswordComplexity {
    # Sample check logic
    return $true
}

function Test-DataEncryptionStatus {
    # Sample check logic
    return $false
}

function Test-AuditLogsEnabled {
    # Sample check logic
    return $true
}

# Generate compliance report
foreach ($check in $complianceChecks) {
    $result = & $check.Check
    $status = if ($result) { "Compliant" } else { "Non-Compliant" }
    Write-Output "$($check.Standard): $status"
}
```

### Smart Reasoning:
This script automates compliance checks against industry standards like PCI-DSS, ensuring regular assessment and reporting of compliance status. It reduces manual effort while maintaining consistent and accurate reporting.

---

### 5. **Automated Threat Detection and Incident Logging**

This script monitors system logs for potential security threats, such as repeated login failures or unauthorized access attempts, and automatically logs incidents for further investigation.

```powershell
# Monitor system log for failed login attempts
$logName = "Security"
$eventID = 4625 # Event ID for failed login attempts

# Check system logs for specific threats
$events = Get-WinEvent -LogName $logName -FilterHashtable @{Id = $eventID} | Where-Object { $_.TimeCreated -gt (Get-Date).AddMinutes(-60) }

# Log incidents
foreach ($event in $events) {
    $incident = @{
        TimeStamp = $event.TimeCreated;
        User = $event.Properties[5].Value;
        IP = $event.Properties[18].Value;
        Description = "Failed login attempt"
    }
    
    Add-Content -Path "C:\Incidents\IncidentLog.txt" -Value (ConvertTo-Json $incident)
    Write-Output "Incident logged for failed login attempt by $($incident.User) from IP $($incident.IP)"
}
```

### Smart Reasoning:
This script automates threat detection by monitoring logs for security events like failed login attempts and logging incidents for review. It improves response time for potential threats and supports security teams in tracking incidents.

---

### Smart File Name:

A suitable file name for these scripts could be:

**"Automated_Risk_Assessment_and_Compliance_Checks.ps1"**

### Brilliant Reason and Structure:
- **Automated**: Highlights the focus on automation, reducing manual oversight in risk management.
- **Risk Assessment and Compliance Checks**: Clearly defines the purpose, emphasizing risk evaluation and regulatory adherence.
- **Checks**: Implies the scripts perform thorough checks, ensuring nothing is missed.

This file name effectively communicates the goal of the scripts—to automate risk and compliance tasks, streamlining critical functions in business environments.
