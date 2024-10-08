Here are **5 advanced PowerShell code examples** for **Business Intelligence Automation**, designed to streamline data collection, analysis, and reporting for enhanced decision-making. These scripts provide robust value by automating key business intelligence (BI) tasks and integrating data sources for insightful and actionable reports.

---

### 1. **Automated Data Extraction from Multiple Data Sources**

This script extracts data from various databases (SQL Server, Oracle, and CSV files) and consolidates it into a single dataset for analysis.

```powershell
# SQL Server Connection
$SqlServerConn = "Server=SQLServer;Database=SalesDB;User ID=sa;Password=your_password;"
$SqlQuery = "SELECT * FROM SalesData WHERE SaleDate >= GETDATE()-30"

# Extract SQL Data
$SqlData = Invoke-Sqlcmd -ConnectionString $SqlServerConn -Query $SqlQuery

# Oracle Database Connection
$OracleConn = "Data Source=OracleDB;User ID=user;Password=password;"
$OracleQuery = "SELECT * FROM MarketingData WHERE Date >= SYSDATE-30"

# Extract Oracle Data
$OracleData = Invoke-Sqlcmd -ConnectionString $OracleConn -Query $OracleQuery

# CSV File Data Extraction
$CsvData = Import-Csv "C:\Data\FinancialData.csv"

# Merge all data into a single dataset
$ConsolidatedData = $SqlData + $OracleData + $CsvData
$ConsolidatedData | Export-Csv "C:\ConsolidatedData\BusinessData.csv" -NoTypeInformation
```

### Wise Evidence and Robust Value:
Automating data extraction from multiple sources allows for more comprehensive business analysis. This script reduces manual effort, ensuring data is always up to date. It provides better, faster decision-making by consolidating data from across the organization.

---

### 2. **Automated KPI Calculation and Reporting**

This script calculates business Key Performance Indicators (KPIs) such as sales growth, customer acquisition rate, and profitability. It then generates a report for management.

```powershell
# Load the consolidated data
$Data = Import-Csv "C:\ConsolidatedData\BusinessData.csv"

# Calculate KPIs
$TotalSales = ($Data | Measure-Object Sales -Sum).Sum
$SalesGrowth = (($TotalSales - $PreviousMonthSales) / $PreviousMonthSales) * 100
$CustomerAcquisition = ($Data | Where-Object { $_.AcquiredCustomer -eq "Yes" }).Count
$Profitability = ($TotalSales - ($Data | Measure-Object Costs -Sum).Sum) / $TotalSales

# Generate a KPI report
$KPIReport = @{
    "TotalSales" = $TotalSales;
    "SalesGrowth" = "{0:N2}%" -f $SalesGrowth;
    "CustomerAcquisitionRate" = $CustomerAcquisition;
    "Profitability" = "{0:P2}" -f $Profitability
}

$KPIReport | Export-Csv "C:\Reports\KPI_Report.csv" -NoTypeInformation
```

### Wise Evidence and Robust Value:
Automating KPI calculations ensures accuracy and efficiency, empowering leaders to make data-driven decisions. This script supports real-time performance tracking and provides valuable insights for business strategy adjustments.

---

### 3. **Automated Power BI Data Refresh**

This script uses PowerShell to trigger a refresh of Power BI datasets, ensuring that dashboards are always updated with the latest business data.

```powershell
# Power BI API connection
$powerBIGroupId = "your-group-id"
$datasetId = "your-dataset-id"
$accessToken = "your-access-token"

# Trigger dataset refresh
$uri = "https://api.powerbi.com/v1.0/myorg/groups/$powerBIGroupId/datasets/$datasetId/refreshes"
Invoke-RestMethod -Uri $uri -Method Post -Headers @{Authorization = "Bearer $accessToken"}

Write-Output "Power BI dataset refresh triggered successfully."
```

### Wise Evidence and Robust Value:
This script automates the update of Power BI dashboards, ensuring that decision-makers always have access to the latest data. The automation streamlines data flows, reducing manual intervention and maintaining real-time insights into business metrics.

---

### 4. **Automated Trend Analysis for Predictive Insights**

This script performs a trend analysis by analyzing historical sales data and uses linear regression to forecast future sales. It’s an automated predictive tool for business intelligence.

```powershell
# Load historical sales data
$Data = Import-Csv "C:\Data\HistoricalSalesData.csv"

# Extract sales values and dates
$Sales = $Data | Select-Object -ExpandProperty Sales
$Dates = $Data | Select-Object -ExpandProperty Date

# Perform linear regression to identify sales trend
$Count = $Sales.Count
$SumX = 0..($Count-1) | Measure-Object -Sum
$SumY = ($Sales | Measure-Object -Sum).Sum
$SumXY = 0..($Count-1) | ForEach-Object { $Sales[$_] * $_ } | Measure-Object -Sum
$SumX2 = (0..($Count-1) | ForEach-Object { $_ * $_ }) | Measure-Object -Sum

# Calculate slope and intercept
$m = ($Count * $SumXY.Sum - $SumX.Sum * $SumY) / ($Count * $SumX2.Sum - $SumX.Sum * $SumX.Sum)
$b = ($SumY - $m * $SumX.Sum) / $Count

# Forecast next 30 days
$Forecast = @()
for ($i = $Count; $i -lt $Count + 30; $i++) {
    $Forecast += [pscustomobject]@{ Date = (Get-Date).AddDays($i); ForecastedSales = $m * $i + $b }
}

# Output forecast
$Forecast | Export-Csv "C:\Reports\SalesForecast.csv" -NoTypeInformation
```

### Wise Evidence and Robust Value:
By automating trend analysis and predictive forecasting, this script enables businesses to anticipate future performance and adjust strategies accordingly. It delivers data-driven forecasts that improve resource planning and market readiness.

---

### 5. **Automated Customer Segmentation for Targeted Marketing**

This script automatically segments customers based on their purchase behavior, enabling targeted marketing strategies. It uses clustering techniques to identify high-value customers.

```powershell
# Load customer data
$CustomerData = Import-Csv "C:\Data\CustomerData.csv"

# Define customer segments based on purchase behavior
$HighValueCustomers = $CustomerData | Where-Object { $_.TotalPurchases -gt 10000 }
$MidValueCustomers = $CustomerData | Where-Object { $_.TotalPurchases -le 10000 -and $_.TotalPurchases -gt 5000 }
$LowValueCustomers = $CustomerData | Where-Object { $_.TotalPurchases -le 5000 }

# Output segmented data
$HighValueCustomers | Export-Csv "C:\Segments\HighValueCustomers.csv" -NoTypeInformation
$MidValueCustomers | Export-Csv "C:\Segments\MidValueCustomers.csv" -NoTypeInformation
$LowValueCustomers | Export-Csv "C:\Segments\LowValueCustomers.csv" -NoTypeInformation

Write-Output "Customer segmentation completed successfully."
```

### Wise Evidence and Robust Value:
This script automatically segments customers into different value tiers, facilitating targeted marketing campaigns and personalized customer outreach. It boosts marketing efficiency by focusing efforts on the most valuable segments.

---

### Smart File Name:

**"Business_Intelligence_Automation_Scripts.ps1"**

### Wise Evidence and Robust Structure:
- **Business Intelligence Automation**: The title emphasizes the use of automation for BI tasks, showcasing the purpose clearly.
- **Scripts**: Signifying that the file contains multiple solutions for various BI tasks, enhancing usability and clarity.

This file name provides an organized and practical approach, reflecting the comprehensive nature of the automated BI tasks included.
