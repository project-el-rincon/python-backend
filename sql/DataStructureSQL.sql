CREATE TABLE IF NOT EXISTS `Room` (
    `RoomID` INT AUTO_INCREMENT,
    `Name` VARCHAR(255),
    `Location` VARCHAR(255),
    PRIMARY KEY(`RoomID`)
);

CREATE TABLE IF NOT EXISTS `Sensor` (
    `SensorID` INT AUTO_INCREMENT,
    `RoomID` INT,
    `Type` VARCHAR(255),
    PRIMARY KEY(`SensorID`),
    FOREIGN KEY(`RoomID`) REFERENCES `Room`(`RoomID`)
);

CREATE TABLE IF NOT EXISTS `SensorData` (
    `MeasurementID` INT AUTO_INCREMENT,
    `RoomID` INT,
    `TimeStamp` INT,
    `SensorType` VARCHAR(255),
    `Value` INT,
    PRIMARY KEY(`MeasurementID`),
    FOREIGN KEY(`RoomID`) REFERENCES `Room`(`RoomID`)
);

CREATE TABLE IF NOT EXISTS `has` (
    `MeasurementID` INT,
    `SensorID` INT,
    PRIMARY KEY(`MeasurementID`, `SensorID`),
    FOREIGN KEY(`MeasurementID`) REFERENCES `SensorData`(`MeasurementID`),
    FOREIGN KEY(`SensorID`) REFERENCES `Sensor`(`SensorID`)
);
