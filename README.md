# Zomato Customer Analysis Project

## Overview
This project analyzes customer behavior and order activity for a food-delivery-style business using prepared datasets and supporting reporting materials. The work focuses on understanding customer demographics, purchase patterns, spend behavior, and customer segmentation so that the business can better target active users and identify inactive or non-ordering customers.

## Project Objective
The main goal of this project is to explore:
- customer characteristics such as age, gender, marital status, occupation, income, education, and family size;
- order history and spending behavior;
- customer activity levels and recency-based segmentation;
- patterns that can support customer retention and marketing strategy.

## Files in This Workspace

### Data files
- Customer base data: Final Project Prepared Data - Customer Base.csv
  - Contains customer-level profile and behavioral attributes.
  - Key fields include user_id, name, age, gender, marital status, occupation, monthly income, family size, order_count, total_spend, last_order_date, recency_days, customer_status, recency_score, monetary_score, and rm_score.

- Orders data: Final Project Prepared Data - orders (cleaned).csv
  - Contains transaction-level order records.
  - Key fields include order_date, sales_qty, sales_amount, currency, user_id, r_id, and exclude_from_monetary.

- User profile data: users.csv
  - Contains a simplified user profile table.
  - Key fields include user_id, name, email, password, age, gender, marital status, occupation, monthly income, educational qualifications, and family size.

### Supporting project files
- Zomato_Customer_Analysis_Report.docx
- Zomato_Customer_Analysis_Report_Final_Project V1.docx
- Zomato_Decomposition_Plan 1st Revision.pdf
- Zomato_Dashboard.pbix

## Suggested Use
1. Open the CSV files in Excel, Python, or any BI tool to inspect the customer and order data.
2. Review the Power BI dashboard file to explore the visualized insights.
3. Use the report documents for background context and project structure.

## Key Data Concepts
- Customer status: Indicates whether a customer is currently active, non-ordering, or otherwise categorized.
- Recency score: Measures how recently a customer placed an order.
- Monetary score: Measures the customer’s purchase value.
- RM score: A combined score used for customer segmentation and prioritization.

## Data Notes
- Some records contain missing values, especially in profile fields or order-related fields.
- Some customer rows show placeholder dates such as 1/0/1900 where no valid order date is available.
- The project uses prepared data intended for analysis and reporting training.

## Summary
This repository is a customer analytics project centered on understanding who the customers are, how they buy, and how valuable they are to the business. It combines customer profile data, order transaction data, and dashboard/report deliverables into a complete analytical workflow.
