/*
名稱:
584. Find Customer Referee(找出由特定人推薦的人)

題目:
Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
Return the result table in any order.
The query result format is in the following example.

Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+

作法:
選擇Customer表格的name欄位抓出所有
where篩選出不是2推薦的(referee_id != '2')
同時因為可能有無推薦人(空)，做一個去除空值(referee_id IS NULL)
*/

Select name From Customer where referee_id != '2' or referee_id IS NULL;