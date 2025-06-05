use final_project;
select 
    *
from
    walmartsales_dataset;

-- Task 1: Identifying the Top Branch by Sales Growth Rate.

With Monthly_revenue As (
Select Branch,
Month(str_to_date(date, '%d-%m-%y')) As Month_number,
Sum(total) As Total_rev
From Walmartsales_dataset
Group By Branch, Month_number),

Growth_Rate As (
Select Branch, Month_number, Total_rev,
(Total_rev - Lag(total_rev) Over (Partition By Branch Order By Month_number))/Lag(total_rev) Over (Partition By Branch 
Order By Month_number) * 100 As growth_rate
From Monthly_revenue)

Select Branch, Round(sum(total_rev),2) As Total_rev, round(sum(growth_rate),2) As Growth_rate
From Growth_Rate
Group By Branch;

-- ----------------------------------------------------------------------------------------------------------------


Select 
    Branch,
    Product_line,
    Round(sum(total - gross_income), 2) As Profit_margin
From
    Walmartsales_dataset
Group By Product_line , Branch
Order by Branch , profit_margin;

-- -----------------------------------------------------------------------------------------

Select 
    Customer_id,
    Round(sum(total), 2) As Total_purchase_amount,
    Case
        When Sum(total) > 22000 Then 'High'
        When Sum(total) Between 20000 And 22000 Then 'Medium'
        Else 'Low'
    End As Spending_category
From
    Walmartsales_dataset
Group By Customer_id
Order By Customer_id;

-- -------------------------------------------------------------------------------------------

-- Task 4: Detecting Anomalies in Sales Transactions.

WITH Salesstats AS (    
Select         
Product_line, Avg(total) AS Avg_sales, 
Stddev(total) AS Std_dev    
From Walmartsales_dataset    
Group By Product_line)

Select     
S.Invoice_id, S.Product_line, Round(s.Total, 2) As Total_sales,     Round(ss.Avg_sales,2) As Avg_sales, 
Round(ss.Std_dev,2) As Std_dev,    
Round((s.Total - Ss.Avg_sales) / Ss.Std_dev, 2) As Z_score
From Walmartsales_dataset S
Join Salesstats Ss ON S.Product_line = Ss.Product_line
Where Abs((s.Total - Ss.Avg_sales) / Ss.Std_dev) > 2.5;

-- -----------------------------------------------------------------------------------------------

--  Task 5: Most Popular Payment Method by City.

WITH Paymentcounts AS (    
SELECT City, Payment,        
COUNT(*) AS Paymentcount    
FROM Walmartsales_dataset    
GROUP BY City, Payment),

Mostpopularpayment AS (    
SELECT City, Payment, Paymentcount,        
RANK() OVER (PARTITION BY City ORDER BY Paymentcount DESC) AS RNK    
FROM Paymentcounts)

SELECT  City, Payment AS Most_popular_payment_method,   
Paymentcount AS Transaction_count
FROM Mostpopularpayment
Where Rnk = 1
ORDER BY City;

-- ----------------------------------------------------------------------------------------------

SELECT 
    DATE_FORMAT(STR_TO_DATE(date, '%d-%m-%Y'), '%b') AS Month,
    Gender,
    ROUND(SUM(total), 2) AS Total_sales
FROM
    Walmartsales_dataset
GROUP BY Month , Gender
ORDER BY Month , Gender;

-- ----------------------------------------------------------------------------------------------------

-- Task 7: Best Product Line by Customer Type.

With Total_sales_product_line As (
Select Customer_type, Product_line, Sum(total) As Total_sales    
From Walmartsales_dataset    
Group By Customer_type, Product_line),

Ranked_sales As (
Select Customer_type, Product_line, Total_sales, 
Row_number() 
Over(partition By Customer_type Order By Total_sales Desc) As Rnk
From Total_sales_product_line)

Select Customer_type, Product_line As Preferred_product_line, 
Round(Total_sales, 2) as Total_sales 
From Ranked_sales
Where Rnk=1;

-- -------------------------------------------------------------------------------------------------

SELECT 
    A.Customer_id,
    A.Invoice_id AS First_purchase_invoice,
    DATE(STR_TO_DATE(A.Date, '%d-%m-%y')) AS First_purchase_date,
    B.Invoice_id AS Repeat_purchase_invoice,
    DATE(STR_TO_DATE(B.Date, '%d-%m-%y')) AS Repeat_purchase_date,
    DATEDIFF(STR_TO_DATE(B.Date, '%d-%m-%y'),
            STR_TO_DATE(A.Date, '%d-%m-%y')) AS No_of_days
FROM
    Walmartsales_dataset AS A
        JOIN
    Walmartsales_dataset AS B ON A.Customer_id = B.Customer_id
        AND DATE(STR_TO_DATE(A.Date, '%d-%m-%y')) < DATE(STR_TO_DATE(B.Date, '%d-%m-%y'))
        AND DATEDIFF(STR_TO_DATE(B.Date, '%d-%m-%y'),
            STR_TO_DATE(A.Date, '%d-%m-%y')) <= 30
ORDER BY A.Customer_id , First_purchase_date;

-- ------------------------------------------------------------------------------------------------------------------------

Select 
    Customer_id, Round(sum(total), 2) As Total_sales_rev
From
    Walmartsales_dataset
Group By Customer_id
Order By Total_sales_rev Desc
Limit 5;

-- -------------------------------------------------------------------------------------------------------------------------
-- Task 10: Analyzing Sales Trends by Day of the Week
SELECT 
    DAYNAME(STR_TO_DATE(date, '%d-%m-%y')) AS Day_of_week,
    ROUND(SUM(total), 2) AS Total_sales
FROM
    Walmartsales_dataset
GROUP BY DAYNAME(STR_TO_DATE(date, '%d-%m-%y'))
ORDER BY Total_sales DESC;
    
-- -----------------------------------------------------------------------------------------------------------------------
