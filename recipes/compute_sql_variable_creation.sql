--defines variable "max_income"
WITH max_income AS (select max("Monthly_Income") from "LOAN_DEFAULT_customer_information_postgres")

--use variable in select statement
SELECT 'id', 'Status', 12 AS total FROM "LOAN_DEFAULT_customer_information_postgres"

