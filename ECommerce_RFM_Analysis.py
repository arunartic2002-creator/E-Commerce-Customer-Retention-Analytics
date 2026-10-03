import pyodbc
import pandas as pd

print("Automation started...")
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=EcommerceAnalytics;"
    "Trusted_Connection=yes;"
)

print("SQL Server connection successful!")

query = """
SELECT *
FROM dbo.Ecommerce_Sales;
"""

df = pd.read_sql(query, conn)

print("Data loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

analysis_date = df["Order_Date"].max() + pd.Timedelta(days=1)

rfm = df.groupby("Customer_ID").agg(
    Recency=("Order_Date", lambda x: (analysis_date - x.max()).days),
    Frequency=("Order_ID", "nunique"),
    Monetary=("Sales_Amount", "sum")
).reset_index()

print("RFM calculation completed!")
print("Customers analyzed:", rfm.shape[0])

rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5, 4, 3, 2, 1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"],
    5,
    labels=[1, 2, 3, 4, 5]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1, 2, 3, 4, 5]
)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(int)
    + rfm["F_Score"].astype(int)
    + rfm["M_Score"].astype(int)
)

print("RFM scoring completed!")

rfm["Segment"] = pd.cut(
    rfm["RFM_Score"],
    bins=[0, 5, 8, 11, 13, 15],
    labels=[
        "Lost Customers",
        "At Risk",
        "Potential Loyalists",
        "Loyal Customers",
        "Champions"
    ]
)

print("Customer segmentation completed!")
output_file = r"C:\Users\HP\Desktop\E-Commerce-Customer-Retention-Analytics\Python\rfm_customer_analysis.csv"

rfm.to_csv(
    output_file,
    index=False
)

print("RFM file updated successfully!")
print("File:", output_file)

print("Automation completed successfully!")