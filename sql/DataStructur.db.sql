CREATE TABLE IF NOT EXISTS "Room" (
	"RoomID"	INTEGER,
	"Name"	TEXT,
	"Location"	TEXT,
	PRIMARY KEY("RoomID")
);
CREATE TABLE IF NOT EXISTS "Sensor" (
	"SensorID"	INTEGER,
	"RoomID"	INTEGER,
	"Type"	TEXT,
	PRIMARY KEY("SensorID"),
	FOREIGN KEY("RoomID") REFERENCES "Room"("RoomID")
);
CREATE TABLE IF NOT EXISTS "SensorData" (
	"MeasurementID"	INTEGER,
	"RoomID"	INTEGER,
	"TimeStamp"	INTEGER,
	"SensorType"	TEXT,
	"Value"	INTEGER,
	PRIMARY KEY("MeasurementID"),
	FOREIGN KEY("RoomID") REFERENCES "Room"("RoomID")
);
CREATE TABLE IF NOT EXISTS "has" (
	"MeasurementID"	INTEGER,
	"SensorID"	INTEGER,
	PRIMARY KEY("MeasurementID","SensorID"),
	FOREIGN KEY("MeasurementID") REFERENCES "SensorData"("MeasurementID"),
	FOREIGN KEY("SensorID") REFERENCES "Sensor"("SensorID")
);