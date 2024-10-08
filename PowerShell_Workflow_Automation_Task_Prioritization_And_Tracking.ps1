Here are **5 advanced PowerShell code examples** focused on **Workflow Automation and Task Management** with smart reasoning for **project completion and decision-making**:

### 1. **Automated Task Assignment and Tracking**

This script automates assigning tasks to team members based on workload and tracks their progress by pulling data from a project management API (like Jira or Trello).

```powershell
# Define team members and workload distribution
$team = @(
    @{Name="Alice"; Workload=10},
    @{Name="Bob"; Workload=8},
    @{Name="Charlie"; Workload=12}
)

# Get open tasks from project management API
$tasks = Invoke-RestMethod -Uri "https://api.projectmanager.com/tasks/open" -Method Get

# Assign tasks based on workload (assign fewer tasks to less loaded team members)
foreach ($task in $tasks) {
    $assignedMember = $team | Sort-Object Workload | Select-Object -First 1
    $assignedMember.Workload++
    
    # Update task assignment in the system
    Invoke-RestMethod -Uri "https://api.projectmanager.com/tasks/$($task.id)/assign" -Method Post -Body @{assignee=$assignedMember.Name}
}

# Export updated workload for review
$team | Export-Csv -Path "C:\Reports\TeamWorkload.csv" -NoTypeInformation
```

### Smart Reasoning:
This automation distributes tasks fairly based on current workload, allowing for optimized resource allocation. By dynamically assigning tasks and tracking progress in real-time, managers can ensure balanced workloads and improve project completion efficiency.

---

### 2. **Milestone Progress Tracking and Alerting**

This script monitors milestones in a project and sends alerts when specific milestones are close to or past their deadlines. It helps managers ensure that critical tasks are on track.

```powershell
# Define milestone deadlines
$milestones = @{
    "Design Phase" = (Get-Date "2024-10-15")
    "Development Phase" = (Get-Date "2024-11-05")
    "Testing Phase" = (Get-Date "2024-11-20")
}

# Check current milestone progress
$currentMilestone = "Development Phase"
$currentDate = Get-Date

if ($currentDate -gt $milestones[$currentMilestone].AddDays(-3)) {
    Send-MailMessage -To "manager@company.com" -Subject "Milestone Alert" -Body "The $currentMilestone is nearing its deadline!" -SmtpServer "smtp.server.com"
}

# Notify stakeholders if a milestone is past due
foreach ($milestone in $milestones.Keys) {
    if ($currentDate -gt $milestones[$milestone]) {
        Send-MailMessage -To "executives@company.com" -Subject "Milestone Overdue" -Body "$milestone is overdue!" -SmtpServer "smtp.server.com"
    }
}
```

### Smart Reasoning:
This script ensures critical milestones are met by automatically notifying stakeholders of upcoming or missed deadlines. It reduces the risk of missed project timelines and allows for timely interventions, enhancing overall project management.

---

### 3. **Automated Time Tracking and Reporting**

This script automatically tracks time spent on various project tasks and generates a weekly report for managers to review, helping with project time management and efficiency analysis.

```powershell
# Define team members and project tasks
$team = @("Alice", "Bob", "Charlie")
$tasks = @("Development", "Testing", "Documentation")

# Log time spent on tasks (sample data input from tracking system)
$timeLog = @(
    @{Name="Alice"; Task="Development"; Hours=15},
    @{Name="Bob"; Task="Testing"; Hours=10},
    @{Name="Charlie"; Task="Documentation"; Hours=12}
)

# Generate weekly report
$report = $timeLog | Group-Object Task | ForEach-Object {
    @{
        Task = $_.Name
        TotalHours = ($_.Group | Measure-Object Hours -Sum).Sum
    }
}

# Export report to CSV
$report | Export-Csv -Path "C:\Reports\WeeklyTimeTracking.csv" -NoTypeInformation

# Send report to project manager
Send-MailMessage -To "pm@company.com" -Subject "Weekly Time Tracking Report" -Body "Please find attached the time tracking report for the week." -Attachments "C:\Reports\WeeklyTimeTracking.csv" -SmtpServer "smtp.server.com"
```

### Smart Reasoning:
By automating time tracking, this script eliminates the need for manual reporting and ensures accurate data is provided for time management. Project managers can quickly see which tasks consume the most time and adjust planning accordingly.

---

### 4. **Automated Risk Assessment Based on Task Delays**

This script evaluates potential project risks by analyzing delays in task completion and sending a risk assessment report based on predefined thresholds.

```powershell
# Define tasks and expected completion times
$tasks = @(
    @{Task="Develop Feature A"; ExpectedCompletion=(Get-Date).AddDays(-2); ActualCompletion=(Get-Date).AddDays(-1)},
    @{Task="Develop Feature B"; ExpectedCompletion=(Get-Date).AddDays(-3); ActualCompletion=$null},
    @{Task="Test Feature C"; ExpectedCompletion=(Get-Date).AddDays(-1); ActualCompletion=(Get-Date)}
)

# Define risk thresholds (e.g., delays over 2 days are high risk)
$highRiskThreshold = 2

# Analyze tasks for delays
$report = foreach ($task in $tasks) {
    $delay = if ($task.ActualCompletion) {
        ($task.ActualCompletion - $task.ExpectedCompletion).Days
    } else {
        (Get-Date - $task.ExpectedCompletion).Days
    }
    
    [PSCustomObject]@{
        Task = $task.Task
        Delay = $delay
        RiskLevel = if ($delay -gt $highRiskThreshold) {"High"} elseif ($delay -gt 0) {"Medium"} else {"Low"}
    }
}

# Export risk report
$report | Export-Csv -Path "C:\Reports\RiskAssessment.csv" -NoTypeInformation

# Notify project manager if any high-risk tasks are found
if ($report | Where-Object { $_.RiskLevel -eq "High" }) {
    Send-MailMessage -To "manager@company.com" -Subject "High-Risk Task Alert" -Body "Some tasks have a high risk due to delays. Please see the attached report." -Attachments "C:\Reports\RiskAssessment.csv" -SmtpServer "smtp.server.com"
}
```

### Smart Reasoning:
This script automatically assesses project risks based on delays in task completion, providing an early warning system for project managers. By flagging high-risk tasks, it allows teams to focus on resolving critical issues before they escalate.

---

### 5. **Automated Task Prioritization Based on Resource Availability**

This script dynamically re-prioritizes tasks based on the availability of resources (team members, tools, etc.), helping optimize project completion times.

```powershell
# Define available resources
$resources = @{
    Alice = "Available"
    Bob = "Busy"
    Charlie = "Available"
}

# Define project tasks and required resources
$tasks = @(
    @{Task="Develop Module A"; RequiredResource="Alice"},
    @{Task="Test Module B"; RequiredResource="Bob"},
    @{Task="Write Documentation"; RequiredResource="Charlie"}
)

# Prioritize tasks based on resource availability
$prioritizedTasks = foreach ($task in $tasks) {
    if ($resources[$task.RequiredResource] -eq "Available") {
        [PSCustomObject]@{
            Task = $task.Task
            Priority = "High"
        }
    } else {
        [PSCustomObject]@{
            Task = $task.Task
            Priority = "Low"
        }
    }
}

# Export prioritized tasks list
$prioritizedTasks | Export-Csv -Path "C:\Reports\PrioritizedTasks.csv" -NoTypeInformation
```

### Smart Reasoning:
This script helps in dynamic task prioritization based on real-time availability of resources, ensuring efficient project execution. Automating this process allows managers to avoid bottlenecks and better allocate resources to the most critical tasks.

---

### Smart File Name:

For these workflow automation and task management examples, a suitable file name would be:

**"PowerShell_Workflow_Automation_Task_Prioritization_And_Tracking.ps1"**

This name emphasizes the core focus on workflow automation, task prioritization, and tracking, while also hinting at advanced project management capabilities.
