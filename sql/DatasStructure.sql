-- MySQL Script generated by MySQL Workbench
-- Mon Mar 10 13:11:35 2025
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Room` (
  `RoomID` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Location` VARCHAR(45) NULL,
  PRIMARY KEY (`RoomID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`SensorData`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`SensorData` (
  `MeasurementID` INT NOT NULL,
  `RoomID` INT NULL,
  `TimeStamp` VARCHAR(45) NULL,
  `SensorType` VARCHAR(45) NULL,
  `Values` INT NULL,
  PRIMARY KEY (`MeasurementID`),
  CONSTRAINT `RoomID`
    FOREIGN KEY ()
    REFERENCES `mydb`.`Room` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Sensor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Sensor` (
  `SensorID` INT NOT NULL,
  `RoomID` INT NULL,
  `Type` VARCHAR(45) NULL,
  PRIMARY KEY (`SensorID`),
  CONSTRAINT `RoomID`
    FOREIGN KEY ()
    REFERENCES `mydb`.`Room` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`has`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`has` (
  `MeasurementID` INT NOT NULL,
  `SensorID` INT NOT NULL,
  PRIMARY KEY (`MeasurementID`, `SensorID`),
  CONSTRAINT `MeasurementID`
    FOREIGN KEY ()
    REFERENCES `mydb`.`SensorData` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `SensorID`
    FOREIGN KEY ()
    REFERENCES `mydb`.`Sensor` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
