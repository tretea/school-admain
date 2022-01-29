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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,1,'2021001',36,37,38,40,45,43,0),(2,1,'2021002',37,38,39,41,42,44,0),(3,1,'2021003',38,36,37,38,39,43,0),(4,2,'2021004',NULL,NULL,NULL,NULL,NULL,NULL,1),(5,2,'2021005',NULL,NULL,NULL,NULL,NULL,NULL,1),(6,2,'2021006',NULL,NULL,NULL,NULL,NULL,NULL,2),(7,3,'2021007',NULL,NULL,NULL,NULL,NULL,NULL,1),(8,3,'2021008',NULL,NULL,NULL,NULL,NULL,NULL,1),(9,3,'2021009',NULL,NULL,NULL,NULL,NULL,NULL,2);
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `class_id` int DEFAULT NULL,
  `time` varchar(30) DEFAULT NULL,
  `week` varchar(5) DEFAULT NULL,
  `weeknum` varchar(2) DEFAULT NULL,
  `classnum` varchar(5) DEFAULT NULL,
  `sub_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `class_course` (`class_id`),
  KEY `sub_course` (`sub_id`),
  CONSTRAINT `class_course` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sub_course` FOREIGN KEY (`sub_id`) REFERENCES `subjects` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (1,1,'2021-2022年第一学期','第一周','周一','第一大节',1),(2,1,'2021-2022年第一学期','第一周','周二','第二大节',2),(3,1,'2021-2022年第一学期','第一周','周一','第三大节',1),(4,1,'2021-2022年第一学期','第一周','周三','第二大节',1),(5,1,'2021-2022年第一学期','第一周','周二','第四大节',1),(6,1,'2021-2022年第一学期','第一周','周四','第一大节',1),(7,1,'2021-2022年第一学期','第一周','周五','第四大节',1),(11,1,'2021-2022年第一学期','第一周','周一','第二大节',2),(12,1,'2021-2022年第一学期','第一周','周一','第四大节',3),(13,1,'2021-2022年第一学期','第一周','周三','第一大节',4),(14,1,'2021-2022年第一学期','第一周','周三','第四大节',5),(15,1,'2021-2022年第一学期','第一周','周四','第三大节',19),(16,1,'2021-2022年第一学期','第一周','周五','第一大节',2),(17,1,'2021-2022年第一学期','第一周','周五','第三大节',5),(18,2,'2021-2022年第一学期','第一周','周一','第二大节',1),(19,2,'2021-2022年第一学期','第一周','周一','第四大节',2),(20,2,'2021-2022年第一学期','第一周','周二','第一大节',3),(21,2,'2021-2022年第一学期','第一周','周二','第三大节',4),(22,2,'2021-2022年第一学期','第一周','周四','第三一大节',5),(23,2,'2021-2022年第一学期','第一周','周四','第四大节',19),(24,2,'2021-2022年第一学期','第一周','周五','第一大节',2),(25,2,'2021-2022年第一学期','第一周','周五','第二大节',3),(26,2,'2021-2022年第一学期','第一周','周三','第二大节',5),(27,2,'2021-2022年第一学期','第一周','周三','第三大节',4);
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
-- Table structure for table `scores`
--

DROP TABLE IF EXISTS `scores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `scores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `time` varchar(30) DEFAULT NULL,
  `score` int DEFAULT NULL,
  `stu_id` int DEFAULT NULL,
  `sub_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stu_score` (`stu_id`),
  KEY `sub_score` (`sub_id`),
  CONSTRAINT `stu_score` FOREIGN KEY (`stu_id`) REFERENCES `students` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sub_score` FOREIGN KEY (`sub_id`) REFERENCES `subjects` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scores`
--

LOCK TABLES `scores` WRITE;
/*!40000 ALTER TABLE `scores` DISABLE KEYS */;
INSERT INTO `scores` VALUES (1,'2021-2022年第一学期',100,1,1),(2,'2021-2022年第一学期',100,1,2),(3,'2021-2022年第一学期',100,1,3),(4,'2021-2022年第一学期',100,2,1),(5,'2021-2022年第一学期',100,2,2),(6,'2021-2022年第一学期',100,2,3),(7,'2021-2022年第一学期',100,3,1),(8,'2021-2022年第一学期',100,3,2),(9,'2021-2022年第一学期',100,3,3),(10,'2021-2022年第一学期',100,4,1),(11,'2021-2022年第一学期',100,4,2),(12,'2021-2022年第一学期',100,4,3);
/*!40000 ALTER TABLE `scores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idcard` int NOT NULL,
  `name` varchar(4) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `class_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `class_stu` (`class_id`),
  CONSTRAINT `class_stu` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,21001001,'孙同学',21,'男',1),(2,21001002,'李同学',21,'女',1),(3,21002001,'张同学',21,'男',2),(4,21002002,'赵同学',21,'女',2);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (36,'老王',36,'男',1),(37,'老樊',26,'女',2),(38,'老秦',43,'女',3),(39,'小曾',28,'男',1),(40,'小波',26,'男',4),(41,'小陈',24,'男',20),(42,'老周',47,'男',21),(43,'小孙',24,'男',19),(44,'小陈',24,'男',22),(45,'小魏',24,'女',5);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(10) NOT NULL,
  `password` varchar(30) NOT NULL,
  `Type` int NOT NULL,
  `t_id` int DEFAULT NULL,
  `s_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t_user` (`t_id`),
  KEY `s_user` (`s_id`),
  CONSTRAINT `s_user` FOREIGN KEY (`s_id`) REFERENCES `students` (`id`) ON DELETE CASCADE,
  CONSTRAINT `t_user` FOREIGN KEY (`t_id`) REFERENCES `teachers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (5,'21001001','123456',2,NULL,1),(6,'21001002','123456',2,NULL,2),(7,'21002001','123456',2,NULL,3),(8,'21002002','123456',2,NULL,4),(9,'admin','123456',0,NULL,NULL),(10,'laowang','123456',1,36,NULL),(11,'laofan','123456',1,37,NULL),(12,'laoqin','123456',1,38,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-29 20:45:49
