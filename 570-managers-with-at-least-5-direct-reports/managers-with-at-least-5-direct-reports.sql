select a.name from Employee a 
join Employee b 
on a.id=b.managerID 
group by b.managerID 
having count(*) >= 5;