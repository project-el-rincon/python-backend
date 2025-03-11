BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Measurement" (
	"id"	INTEGER,
	"sensorroom"	INTEGER,
	"timestamp"	INTEGER,
	"sensortype"	INTEGER,
	"value"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Measurement" VALUES (3,'A15','2025-03-11 10:18:20','Strom',10);
INSERT INTO "Measurement" VALUES (4,'A15','2025-03-11 10:18:20','Strom',10);
INSERT INTO "Measurement" VALUES (5,'A15','2025-03-11 10:18:20','Strom',10);
COMMIT;
