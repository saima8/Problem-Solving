/*
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your PL/SQL query statement below
 
delete from person
where count(distinct email) > 1
group by email

DELETE FROM your_table
WHERE rowid not in
(SELECT MIN(rowid)
FROM your_table
GROUP BY column1, column2, column3)

DELETE 
FROM person a
WHERE ROWID > (SELECT MIN(ROWID) FROM person b
WHERE b.id=a.id
);
*/

delete person
where  id not in (
  select min(p.id)
  from   person p
  group  by p.email
)