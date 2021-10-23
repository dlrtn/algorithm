SELECT HOUR(dateTime) as "HOUR", count(HOUR(dateTime)) as COUNT From ANIMAL_OUTS
where HOUR(dateTime) >8 and HOUR(dateTime) < 20
group by HOUR(dateTime)
order by HOUR(dateTime)