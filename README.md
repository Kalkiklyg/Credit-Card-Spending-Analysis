Credit Card Spending Analysis — California (2023)

An end-to-end EDA & Business Insights Project using Python, SQL, and Power BI


---

⭐ Project Overview

This project analyzes 50,000 credit card transactions from customers in California (2023) to uncover:

Spending patterns

Category-wise revenue

Customer behavior

High-value transactions

Gender spending differences

Business insights for decision making


The goal is to create a clean, reusable EDA workflow and extract actionable insights for finance teams, credit card companies, and business stakeholders.


---

📁 Project Files

File	Description

EDA_workflow_v1.3_creditcardspending.py	Python EDA script with modular functions
credit_card_transaction_flow_cleaneddata.csv	Cleaned dataset
creditcardspending.pbix	Power BI dashboard file
Credit Card Spending Analysis — Final_Report.pdf	Full business analysis report
Screenshots (.png)	Dashboard previews
README.md	Project documentation



---

🧹 About the Dataset

Rows: 50,000
Columns: 9

Column Description

Column	Description

CustomerID	Unique identifier
Name	Customer first name
Surname	Customer last name
Gender	Male/Female
Birthdate	Date of birth
Transaction Amount	Amount spent per transaction
Date	Transaction date
MerchantName	Business where purchase was made
Category	Type of purchase (Travel, Electronics, etc.)



---

🔍 Key Insights

📌 1. High Spending Categories (Python & SQL)

Top 3 categories where customers spend the most:

Category	Avg Spend (Python)	Total Spend (SQL)

Travel	$1500	$12,900,231
Electronics	$500	$4,394,092
Market	$250	$2,151,134


✔ Travel is the #1 revenue driver
✔ Electronics is 2nd, major during festive months
✔ Market spending is daily and stable


---

📌 2. Spending Distribution

Average transaction: $442.11

Minimum: $5.01

Maximum: $2,999.88

Outliers: $1100 → $3000 (mostly Travel & Electronics)



---

📌 3. Gender-Based Insights

Gender	Total Spend

Female	$11M
Male	Lower


✔ Female customers contribute the majority of total revenue


---

📌 4. Business Takeaways

Travel promotions will drive the highest customer engagement

Electronics spending spikes → ideal for targeted cashback campaigns

Grocery/Market transactions have high frequency → loyalty programs

Female customers = strongest profit segment

High-value outliers indicate premium users → VIP credit card tier potential



---

🛠 Tech Stack

Python: Pandas, Matplotlib, Seaborn

SQL: Aggregations, grouping, joins

Power BI: Interactive dashboards

GitHub: Version control

CSV: Realistic dataset



---

📈 Dashboard Preview

added in files
---

🚀 How to Run the Project

1. Clone Repo

git clone https://github.com/Kalkiklyg/Credit-Card-Spending-Analysis

2. Install Libraries

pip install pandas matplotlib seaborn

3. Run Python Script

python EDA_workflow_v1.3_creditcardspending.py

4. Explore Dashboard

Open:
creditcardspending.pbix in Power BI Desktop.


---

🧠 Conclusion

This project provides a full breakdown of spending behavior for California customers in 2023.
It reveals:

Top revenue-driving categories

Customer spending patterns

Gender contribution

High-value outlier segments

Actionable insights for business decisions


The EDA workflow is clean, modular, and reusable for any similar dataset.


---

🤝 Connect With Me

If you found this helpful, let’s connect:

🔗 LinkedIn: https://www.linkedin.com/in/shailesh-pawar-213903281/
🔗 Medium: (add your Medium article link)