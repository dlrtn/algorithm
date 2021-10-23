SELECT ao.ANIMAL_ID, ao.NAME
from ANIMAL_OUTS as ao
where ao.ANIMAL_ID not in (select ANIMAL_INS.ANIMAL_ID
                             from ANIMAL_INS
                             )