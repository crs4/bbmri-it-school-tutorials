SELECT distinct(person_id) FROM omop_cdm.condition_occurrence 
WHERE condition_source_value = '444814009'
ORDER BY person_id
