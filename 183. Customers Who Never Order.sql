/* 
名稱:
183. Customers Who Never Order(找出從沒訂購的客戶)

題目:
Write an SQL query to report all customers who never order anything.
Return the result table in any order.
The query result format is in the following example.

Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

作法:
選擇Customers表格的name欄位 作為輸出 Customers 
id條件為沒有出現在Orders表格中customerId的id
*/

Select name  AS Customers from Customers 
where  id not in (Select customerId from Orders );