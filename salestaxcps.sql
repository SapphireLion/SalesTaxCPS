CREATE DATABASE `salestaxcps` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;

CREATE TABLE `counties` (
  `CountyID` int(3) unsigned zerofill NOT NULL,
  `County` text,
  PRIMARY KEY (`CountyID`),
  UNIQUE KEY `CountyID_UNIQUE` (`CountyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `salestaxcps`.`counties`
(`CountyID`,
`County`)
VALUES
(<{CountyID: }>,
<{County: }>);

CREATE TABLE `salestaxcps` (
  `CountyID` int(3) unsigned zerofill NOT NULL,
  `NetPayment` decimal(32,2) DEFAULT NULL,
  `Removals` int(4) DEFAULT NULL,
  PRIMARY KEY (`CountyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `salestaxcps`.`salestaxcps`
(`CountyID`,
`NetPayment`,
`Removals`)
VALUES
(<{CountyID: }>,
<{NetPayment: }>,
<{Removals: }>);
