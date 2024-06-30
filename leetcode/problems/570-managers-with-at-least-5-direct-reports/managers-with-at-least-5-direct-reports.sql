# Write your MySQL query statement below
select e1.name
from employee e1, employee e2
where e2.managerId = e1.id
group by e1.id
having count(e1.id)>=5;