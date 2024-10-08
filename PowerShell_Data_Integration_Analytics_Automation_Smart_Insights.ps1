Here are **5 advanced PowerShell code examples** focused on **Data Integration and Analytics Automation** to aid **business decision-making**:

### 1. **Automated Data Extraction from Multiple Sources**

This script automates data extraction from different sources, such as SQL databases, CSV files, and web APIs, and combines the data for unified analysis.

```powershell
# Import data from SQL database
$sqlConnection = New-Object System.Data.SqlClient.SqlConnection
$sqlConnection.ConnectionString = "Server=yourServerAddress;Database=yourDatabase;User Id=yourUsername;Password=yourPassword;"
$sqlConnection.Open()
$sqlCommand = $sqlConnection.CreateCommand()
$sqlCommand.CommandText = "SELECT * FROM SalesData"
$reader = $sqlCommand.ExecuteReader()
$dataTable = New-Object System.Data.DataTable
$dataTable.Load($reader)

# Import data from CSV file
$csvData = Import-Csv -Path "C:\Data\RegionalSales.csv"

# Fetch data from web API
$apiResponse = Invoke-RestMethod -Uri "https://api.sales.com/monthlyData" -Method Get

# Combine all datasets for unified analysis
$combinedData = @($dataTable, $csvData, $apiResponse) | Select-Object * -Unique

# Export combined data to a new CSV for analysis
$combinedData | Export-Csv -Path "C:\Data\UnifiedSalesData.csv" -NoTypeInformation
```

### Smart Reasoning:
This script automates the data extraction process from multiple disparate sources and merges the datasets for further analysis. By automating these data integration steps, businesses can gain a comprehensive view of their sales data without manual intervention.

---

### 2. **Automated Data Cleansing and Standardization**

This script automates the cleaning and standardization of raw data, handling missing values, normalizing date formats, and correcting inconsistencies for accurate analysis.

```powershell
# Load raw data
$data = Import-Csv -Path "C:\Data\SalesRawData.csv"

# Clean and standardize data
$cleanedData = $data | ForEach-Object {
    # Replace missing values with 'N/A'
    $_.CustomerName = if ($_.CustomerName -eq "") { "N/A" } else { $_.CustomerName }
    
    # Standardize date format
    $_.TransactionDate = (Get-Date $_.TransactionDate -Format "yyyy-MM-dd")
    
    # Remove invalid entries
    if ($_.TransactionAmount -gt 0) { $_ }
}

# Export cleaned data
$cleanedData | Export-Csv -Path "C:\Data\CleanedSalesData.csv" -NoTypeInformation
```

### Smart Reasoning:
Cleansing and standardizing data is crucial for accurate analytics. This script automates these steps to ensure that business data is consistent and reliable, leading to more meaningful and actionable insights in decision-making processes.

---

### 3. **Automated Data Visualization Generation**

This script automatically generates charts and visualizations from business data and emails the results to stakeholders for quick decision-making.

```powershell
# Import data
$data = Import-Csv -Path "C:\Data\SalesData.csv"

# Generate a bar chart using the imported data
Add-Type -AssemblyName System.Windows.Forms
$chart = New-Object System.Windows.Forms.DataVisualization.Charting.Chart
$chart.Width = 600
$chart.Height = 400
$chart.Titles.Add("Sales Data by Region")

# Define the chart area
$chartArea = New-Object System.Windows.Forms.DataVisualization.Charting.ChartArea
$chart.ChartAreas.Add($chartArea)

# Add data to the chart
$series = New-Object System.Windows.Forms.DataVisualization.Charting.Series
$series.ChartType = [System.Windows.Forms.DataVisualization.Charting.SeriesChartType]::Bar
foreach ($row in $data) {
    $point = New-Object System.Windows.Forms.DataVisualization.Charting.DataPoint
    $point.SetValueXY($row.Region, $row.SalesAmount)
    $series.Points.Add($point)
}
$chart.Series.Add($series)

# Save chart as image
$chart.SaveImage("C:\Reports\SalesChart.png", "Png")

# Email the chart
Send-MailMessage -To "stakeholders@company.com" -Subject "Weekly Sales Report" -Body "Attached is the sales data visualization for this week." -Attachments "C:\Reports\SalesChart.png" -SmtpServer "smtp.server.com"
```

### Smart Reasoning:
This script automates the generation of visual insights from sales data, saving time in preparing reports. Stakeholders receive quick, digestible visual summaries for faster, more informed decision-making.

---

### 4. **Automated Business KPI Calculation and Alerts**

This script automatically calculates key performance indicators (KPIs) from business data and sends alerts when KPIs fall below predefined thresholds.

```powershell
# Import sales data
$salesData = Import-Csv -Path "C:\Data\SalesData.csv"

# Define KPI thresholds
$kpiThreshold = @{
    "Revenue" = 50000
    "CustomerSatisfaction" = 80
}

# Calculate total revenue and customer satisfaction
$totalRevenue = ($salesData | Measure-Object SalesAmount -Sum).Sum
$averageSatisfaction = ($salesData | Measure-Object CustomerSatisfaction -Average).Average

# Send alert if KPIs are below threshold
if ($totalRevenue -lt $kpiThreshold.Revenue) {
    Send-MailMessage -To "manager@company.com" -Subject "Revenue Alert" -Body "Revenue has fallen below the threshold! Total Revenue: $totalRevenue" -SmtpServer "smtp.server.com"
}
if ($averageSatisfaction -lt $kpiThreshold.CustomerSatisfaction) {
    Send-MailMessage -To "manager@company.com" -Subject "Customer Satisfaction Alert" -Body "Customer Satisfaction is below the threshold! Average Satisfaction: $averageSatisfaction%" -SmtpServer "smtp.server.com"
}
```

### Smart Reasoning:
This script automates the calculation of KPIs and sends real-time alerts if critical metrics fall below acceptable levels. This allows business leaders to take corrective actions promptly and improve outcomes.

---

### 5. **Automated Sentiment Analysis of Customer Feedback**

This script integrates with a text analysis API to perform sentiment analysis on customer feedback data, providing insights into customer satisfaction.

```powershell
# Import customer feedback data
$feedbackData = Import-Csv -Path "C:\Data\CustomerFeedback.csv"

# Perform sentiment analysis on each feedback entry
$apiKey = "yourTextAnalysisApiKey"
$feedbackSentiment = foreach ($feedback in $feedbackData) {
    $response = Invoke-RestMethod -Uri "https://api.textanalysis.com/sentiment" -Method Post -Body @{text=$feedback.Comment} -Headers @{Authorization="Bearer $apiKey"}
    
    [PSCustomObject]@{
        CustomerID = $feedback.CustomerID
        Feedback = $feedback.Comment
        Sentiment = $response.sentiment
    }
}

# Export sentiment analysis results
$feedbackSentiment | Export-Csv -Path "C:\Data\FeedbackSentimentAnalysis.csv" -NoTypeInformation

# Email sentiment report
Send-MailMessage -To "stakeholders@company.com" -Subject "Customer Sentiment Analysis" -Body "Attached is the sentiment analysis report for this week's customer feedback." -Attachments "C:\Data\FeedbackSentimentAnalysis.csv" -SmtpServer "smtp.server.com"
```

### Smart Reasoning:
Automating sentiment analysis on customer feedback provides real-time insights into customer satisfaction trends, allowing businesses to make data-driven improvements. This script enables quick identification of areas needing attention based on customer sentiment.

---

### Smart File Name:

For this set of data integration and analytics automation scripts, a suitable file name would be:

**"PowerShell_Data_Integration_Analytics_Automation_Smart_Insights.ps1"**

This name emphasizes the core themes of data integration, analytics, and automated insights, which are crucial for business decision-making.
