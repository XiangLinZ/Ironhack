-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema CochesLab
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cocheslab
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cocheslab
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cocheslab` DEFAULT CHARACTER SET utf8mb3 ;
USE `cocheslab` ;

-- -----------------------------------------------------
-- Table `cocheslab`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cocheslab`.`cars` (
  `idCars` INT NOT NULL AUTO_INCREMENT,
  `VIN` VARCHAR(45) NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Year` YEAR NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCars`))
ENGINE = InnoDB
AUTO_INCREMENT = 25
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `cocheslab`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cocheslab`.`customers` (
  `idCustomers` INT NOT NULL AUTO_INCREMENT,
  `Customer_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `City` VARCHAR(45) NOT NULL,
  `State_Province` VARCHAR(45) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `Postal` INT NOT NULL,
  PRIMARY KEY (`idCustomers`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `cocheslab`.`salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cocheslab`.`salespersons` (
  `idSalespersons` INT NOT NULL AUTO_INCREMENT,
  `Staff_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Store` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSalespersons`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `cocheslab`.`invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cocheslab`.`invoices` (
  `idInvoices` INT NOT NULL AUTO_INCREMENT,
  `Invoice_Number` INT NOT NULL,
  `Date` DATE NOT NULL,
  `Cars_idCars` INT NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  `Salespersons_idSalespersons` INT NOT NULL,
  PRIMARY KEY (`idInvoices`),
  INDEX `fk_Invoices_Cars1_idx` (`Cars_idCars` ASC) VISIBLE,
  INDEX `fk_Invoices_Salespersons1_idx` (`Salespersons_idSalespersons` ASC) VISIBLE,
  INDEX `fk_Invoices_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Cars1`
    FOREIGN KEY (`Cars_idCars`)
    REFERENCES `cocheslab`.`cars` (`idCars`),
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `cocheslab`.`customers` (`idCustomers`),
  CONSTRAINT `fk_Invoices_Salespersons1`
    FOREIGN KEY (`Salespersons_idSalespersons`)
    REFERENCES `cocheslab`.`salespersons` (`idSalespersons`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
