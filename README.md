# Python Backend for Smart Building Project

## REST API Scheme
- Room
- time
- Energy usage / temperature / humidity / Lights / CO2 / volume / Motion
- value

==**[Flask-Openapi3](https://luolingchun.github.io/flask-openapi3/v3.x/Usage/Specification/)**==

## Secrets:
- DB NAME: home_data
- DB PASSWORD: vBujy@vvXjOVCcuD

## MQTT Topic Scheme

`school/sensortype`


# README


## General Information

### The Project
- We have all been given the Task of improving energy efficiency at El Rincón school. One group takes care of the selection of sensors that are used to record the values, these also build the control of the individual lamp systems in the desired rooms. Another group was given the task of creating the back end and the last group is responsible for the visulization and control of the data, the so called front end.

### Server Part
- The server part of the project is the development of the back end. We start by looking at the basics of the "rest" API and developing the first models of the SQL database. These are used to establish the communication between the sensors and the front end. 

## Server 

### MQTT - Broker 
- **Messaging Queuing Telemetry Transport**
- This is a server that receives all messages from the clients and then routes the messages to the appropriate destination clients.

### Rest API
- Rest API language: **Python**
- The Rest API is used to make the data usable for the front end.

### URL scheme

- 

## How the Database works 
-  Database Language: **SQL**

### Entity-Relationship-Modell
--- 

**Room**
```sql=q
CREATE TABLE IF NOT EXISTS "Room" (
	"RoomID"	INTEGER,
	"Name"	TEXT,
	"Location"	TEXT,
	PRIMARY KEY("RoomID")
);
```
| RoomID | Name | Location |
| -------- | -------- | -------- |
| Integer | Text | Text |

--- 
**Sensor**
```sql=q
CREATE TABLE IF NOT EXISTS "Sensor" (
	"SensorID"	INTEGER,
	"RoomID"	INTEGER,
	"Type"	TEXT,
	PRIMARY KEY("SensorID"),
	FOREIGN KEY("RoomID") REFERENCES "Room"("RoomID")
);
```

| SensorID | RoomID | Type |
| -------- | -------- | -------- |
| Integer  | Integer  |Integer|

---
**SensorData**
```sql=q
CREATE TABLE IF NOT EXISTS "SensorData" (
	"MeasurementID"	INTEGER,
	"RoomID"	INTEGER,
	"TimeStamp"	INTEGER,
	"SensorType"	TEXT,
	"Values"	INTEGER,
	PRIMARY KEY("MeasurementID"),
	FOREIGN KEY("RoomID") REFERENCES "Room"("RoomID")
);
```

| MeasurmentID | RoomID | TimeStamp |SensorType|Values|
| -------- | -------- | -------- |------|------|
| Integer  | Integer     | Integer |Text|Integer|

--- 
**has**
```sql=q
CREATE TABLE IF NOT EXISTS "has" (
	"MeasurementID"	INTEGER,
	"SensorID"	INTEGER,
	PRIMARY KEY("MeasurementID","SensorID"),
	FOREIGN KEY("MeasurementID") REFERENCES "SensorData"("MeasurementID"),
	FOREIGN KEY("SensorID") REFERENCES "Sensor"("SensorID")
);
```

| MeasurmentID | SensorID |
| -------- | -------- | 
| Integer     | Integer     | 
