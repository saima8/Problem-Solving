/* Write your PL/SQL query statement below 
select c.name
from orders o
inner join customers c
on o.id = c.id;
*/

select name as Customers
from customers
where id NOT IN (
select customerId
from orders)
order by name;
 