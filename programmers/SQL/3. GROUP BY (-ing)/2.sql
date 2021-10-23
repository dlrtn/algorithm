SELECT name, count(*)
from animal_ins
group by name
HAVING COUNT(name) > 1
order by name asc