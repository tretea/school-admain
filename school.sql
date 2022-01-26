-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

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
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `id` int NOT NULL AUTO_INCREMENT,
  `grade_id` int DEFAULT NULL,
  `ClassName` varchar(30) DEFAULT NULL,
  `teacher_id` int DEFAULT NULL,
  `t1_id` int DEFAULT NULL,
  `t2_id` int DEFAULT NULL,
  `t3_id` int DEFAULT NULL,
  `t4_id` int DEFAULT NULL,
  `t5_id` int DEFAULT NULL,
  `Type` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `class_grade` (`grade_id`),
  KEY `teacher_class` (`teacher_id`),
  KEY `t1_class` (`t1_id`),
  KEY `t2_class` (`t2_id`),
  KEY `t3_class` (`t3_id`),
  KEY `t4_class` (`t4_id`),
  KEY `t5_class` (`t5_id`),
  CONSTRAINT `grade_class` FOREIGN KEY (`grade_id`) REFERENCES `grades` (`id`) ON DELETE SET NULL,
  CONSTRAINT `t1_class` FOREIGN KEY (`t1_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL,
  CONSTRAINT `t2_class` FOREIGN KEY (`t2_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL,
  CONSTRAINT `t3_class` FOREIGN KEY (`t3_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL,
  CONSTRAINT `t4_class` FOREIGN KEY (`t4_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL,
  CONSTRAINT `t5_class` FOREIGN KEY (`t5_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL,
  CONSTRAINT `teacher_class` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,1,'2021001',13,14,15,16,17,18,0),(2,1,'2021002',NULL,NULL,NULL,NULL,NULL,NULL,0),(3,1,'2021003',NULL,NULL,NULL,NULL,NULL,NULL,0),(4,2,'2021004',NULL,NULL,NULL,NULL,NULL,NULL,1),(5,2,'2021005',NULL,NULL,NULL,NULL,NULL,NULL,1),(6,2,'2021006',NULL,NULL,NULL,NULL,NULL,NULL,2),(7,3,'2021007',NULL,NULL,NULL,NULL,NULL,NULL,1),(8,3,'2021008',NULL,NULL,NULL,NULL,NULL,NULL,1),(9,3,'2021009',NULL,NULL,NULL,NULL,NULL,NULL,2);
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grades`
--

DROP TABLE IF EXISTS `grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `GradeName` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grades`
--

LOCK TABLES `grades` WRITE;
/*!40000 ALTER TABLE `grades` DISABLE KEYS */;
INSERT INTO `grades` VALUES (1,'高一'),(2,'高二'),(3,'高三');
/*!40000 ALTER TABLE `grades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subjects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `SubjectName` varchar(10) DEFAULT NULL,
  `Type` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjects`
--

LOCK TABLES `subjects` WRITE;
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` VALUES (1,'语文',0),(2,'数学',0),(3,'英语',0),(4,'物理',1),(5,'化学',1),(19,'生物',1),(20,'政治',2),(21,'历史',2),(22,'地理',2);
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `TeacherName` varchar(4) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `subject_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_sub` (`subject_id`),
  CONSTRAINT `teacher_sub` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (13,'李白',100,'男',1),(14,'杜甫',100,'男',1),(15,'李清照',100,'女',1),(16,'祖冲之',100,'男',2),(17,'华罗庚',100,'男',2),(18,'小李子',50,'男',3),(19,'阿米尔汗',50,'男',3),(20,'阿基米德',100,'男',4),(21,'牛顿',100,'男',4),(22,'居里夫人',100,'女',5),(23,'屠呦呦',50,'女',19),(24,'李世民',100,'男',20),(25,'司马迁',100,'男',21),(26,'郦道元',100,'男',22);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-26 11:01:48
