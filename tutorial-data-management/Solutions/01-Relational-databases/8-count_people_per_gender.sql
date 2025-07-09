SELECT
gender_source_value,
  COUNT(*) AS gender_count
FROM omop_cdm.person
GROUP BY gender_source_value
