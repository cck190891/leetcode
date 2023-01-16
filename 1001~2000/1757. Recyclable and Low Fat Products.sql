/*
名稱:
1757. Recyclable and Low Fat Products(可回收跟低脂產品)

題目:
Write an SQL query to find the ids of products that are both low fat and recyclable.
Return the result table in any order.
The query result format is in the following example.

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.

作法:
Select找出輸出
where判斷low_fats、recyclable同時為Y
*/
Select product_id From Products
where low_fats = 'Y' and recyclable = 'Y';
