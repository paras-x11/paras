-- MySQL dump 10.13  Distrib 8.0.39, for Win64 (x86_64)
--
-- Host: localhost    Database: module5
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cno` int NOT NULL,
  `cname` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `rating` int NOT NULL,
  `sno` int DEFAULT NULL,
  PRIMARY KEY (`cno`),
  KEY `sno` (`sno`),
  CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`sno`) REFERENCES `sales_person` (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (201,'hoffman','london',100,1001),(202,'giovanne','rome',200,1003),(203,'liu','san jose',300,1002),(204,'grass','barcelona',100,1002),(206,'clemens','london',300,1007),(207,'pereira','rome',100,1004);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `e_id` int NOT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `joining_date` datetime DEFAULT NULL,
  `department` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`e_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'john','abraham',1000000,'2013-01-01 12:00:00','banking'),(2,'michael','clarke',800000,'2013-01-01 12:00:00','insurance'),(3,'roy','thomas',700000,'2013-02-01 12:00:00','banking'),(4,'tom','jose',600000,'2013-02-01 12:00:00','insurance'),(5,'jerry','pinto',650000,'2013-02-01 12:00:00','insurance'),(6,'philip','mathew',750000,'2013-01-01 12:00:00','service'),(7,'testname1','123',650000,'2013-01-01 12:00:00','service'),(8,'testname2','456',600000,'2013-02-01 12:00:00','insurance');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam`
--

DROP TABLE IF EXISTS `exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam` (
  `roll_no` int NOT NULL,
  `s_code` varchar(10) NOT NULL,
  `marks` int NOT NULL,
  `p_code` varchar(5) DEFAULT NULL,
  KEY `roll_no` (`roll_no`),
  CONSTRAINT `exam_ibfk_1` FOREIGN KEY (`roll_no`) REFERENCES `student` (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam`
--

LOCK TABLES `exam` WRITE;
/*!40000 ALTER TABLE `exam` DISABLE KEYS */;
INSERT INTO `exam` VALUES (1,'cs11',50,'cs'),(1,'cs12',60,'cs'),(2,'ec101',66,'ec'),(2,'ec102',70,'ec'),(3,'ec101',45,'ec'),(3,'ec102',50,'ec');
/*!40000 ALTER TABLE `exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incentive`
--

DROP TABLE IF EXISTS `incentive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incentive` (
  `emp_ref_id` int NOT NULL,
  `incentive_date` date DEFAULT NULL,
  `incentive_amount` int DEFAULT NULL,
  KEY `emp_ref_id` (`emp_ref_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incentive`
--

LOCK TABLES `incentive` WRITE;
/*!40000 ALTER TABLE `incentive` DISABLE KEYS */;
INSERT INTO `incentive` VALUES (1,'2013-02-01',5000),(2,'2013-02-01',3000),(3,'2013-02-01',4000),(1,'2013-01-01',4500),(2,'2013-01-01',3500);
/*!40000 ALTER TABLE `incentive` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_person`
--

DROP TABLE IF EXISTS `sales_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_person` (
  `sno` int NOT NULL,
  `sname` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `comm` float DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_person`
--

LOCK TABLES `sales_person` WRITE;
/*!40000 ALTER TABLE `sales_person` DISABLE KEYS */;
INSERT INTO `sales_person` VALUES (1001,'peel','london',0.12),(1002,'serres','san jose',0.13),(1003,'axerlrod','new york',0.1),(1004,'motika','london',0.11),(1007,'rafkin','barelona',0.15);
/*!40000 ALTER TABLE `sales_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `roll_no` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `branch` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'jay','computer sciene'),(2,'suhani','electronic and com'),(3,'kriti','electronic and com');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-15  9:58:16
