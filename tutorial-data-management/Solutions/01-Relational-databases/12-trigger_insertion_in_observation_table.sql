CREATE OR REPLACE FUNCTION log_observation_insert()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO omop_cdm.log(action)
VALUES('INSERT');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_observation_insert
AFTER INSERT ON omop_cdm.observation
FOR EACH ROW
EXECUTE FUNCTION log_observation_insert();

