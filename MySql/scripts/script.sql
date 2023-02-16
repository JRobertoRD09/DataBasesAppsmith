CREATE TABLE example_table (
  id INT PRIMARY KEY,
  num_col INT,
  bool_col BOOLEAN,
  date_col DATE,
  json_col JSON
);

INSERT INTO example_table (id, num_col, bool_col, date_col, json_col)
VALUES (1, 123, true, '2023-02-15', '{"key": "value"}');

DELIMITER $$

CREATE PROCEDURE example_sp()
BEGIN
  SELECT num_col, bool_col, date_col, json_col FROM example_table WHERE id = 1;
END$$

DELIMITER ;
