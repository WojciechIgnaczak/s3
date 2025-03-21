/*
id,
lines
*/
DROP TABLE IF EXISTS lines;
CREATE TABLE IF NOT EXISTS lines(
    id INTEGER PRIMARY KEY,
    line TEXT,
    modiffied TIMESTAMP default CURRENT_TIMESTAMP
);