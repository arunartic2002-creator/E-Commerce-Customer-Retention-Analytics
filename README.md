## Automation Workflow

The project includes an automated customer RFM analysis pipeline.

### Workflow

SQL Server
↓
Python & Pandas
↓
RFM Calculation
↓
RFM Scoring
↓
Customer Segmentation
↓
CSV Output
↓
Power BI Refresh

### Automation Process

1. Customer sales data is stored and cleaned in SQL Server.
2. A Python script connects to SQL Server using `pyodbc`.
3. Pandas calculates Recency, Frequency, and Monetary values.
4. Customers are assigned RFM scores and segments.
5. The Python script automatically updates `rfm_customer_analysis.csv`.
6. Windows Task Scheduler runs the Python script automatically on a daily schedule.
7. Power BI uses the updated RFM CSV for customer segmentation analysis.

### Tools Used

- SQL Server
- Python
- Pandas
- pyodbc
- Power BI
- DAX
- Windows Task Scheduler
