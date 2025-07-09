CREATE VIEW omop_cdm.v_person_observation AS
SELECT person_id, count(*) as observation_count
FROM omop_cdm.observation
GROUP BY person_id
