-- MySQL dump 10.13  Distrib 5.7.21, for macos10.13 (x86_64)
--
-- Host: localhost    Database: tour
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('db33fdfb5738');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `like_cnt` int(11) DEFAULT NULL,
  `cmt_cnt` int(11) DEFAULT NULL,
  `clicks` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(256) NOT NULL,
  `content` text NOT NULL,
  `like_degree` enum('0','1','2','3','4','5') DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `comment` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `know`
--

DROP TABLE IF EXISTS `know`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `know` (
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `like_cnt` int(11) DEFAULT NULL,
  `cmt_cnt` int(11) DEFAULT NULL,
  `clicks` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(128) NOT NULL,
  `content` text NOT NULL,
  `tour_route` varchar(256) DEFAULT NULL,
  `advice_time` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `know_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `know`
--

LOCK TABLES `know` WRITE;
/*!40000 ALTER TABLE `know` DISABLE KEYS */;
/*!40000 ALTER TABLE `know` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `question` (
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `content` varchar(256) NOT NULL,
  `dot_time` datetime NOT NULL,
  `cmt_cnt` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `question_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `travel`
--

DROP TABLE IF EXISTS `travel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `travel` (
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `like_cnt` int(11) DEFAULT NULL,
  `cmt_cnt` int(11) DEFAULT NULL,
  `clicks` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `pic_link` varchar(256) DEFAULT NULL,
  `open_time` varchar(128) DEFAULT NULL,
  `advice_time` varchar(128) DEFAULT NULL,
  `phone` varchar(11) NOT NULL,
  `price` varchar(11) DEFAULT NULL,
  `website` varchar(128) DEFAULT NULL,
  `place` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `travel`
--

LOCK TABLES `travel` WRITE;
/*!40000 ALTER TABLE `travel` DISABLE KEYS */;
/*!40000 ALTER TABLE `travel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nick_name` varchar(32) NOT NULL,
  `sex` enum('man','woman') DEFAULT NULL,
  `pic_url` varchar(256) DEFAULT NULL,
  `password` varchar(128) NOT NULL,
  `phone_num` varchar(11) NOT NULL,
  `user_live` varchar(256) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `id_style` enum('user','admin') DEFAULT NULL,
  `private_sign` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nick_name` (`nick_name`),
  UNIQUE KEY `phone_num` (`phone_num`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('2018-10-24 22:15:30','2018-12-16 03:00:36',1,'admin',NULL,NULL,'123456','123456',NULL,'2018-12-16 03:00:36','admin','ooook'),('2018-10-24 23:06:57','2018-11-19 22:41:53',2,'admin2',NULL,NULL,'123','123',NULL,'2018-11-19 22:41:53','admin','oooook'),('2018-10-27 17:04:25','2018-12-16 02:57:54',3,'wo','man','../static/user_head_pic/user1544900274.191731.jpg','123','1234',NULL,'2018-10-27 17:04:57','user','ok'),('2018-10-27 17:37:39','2018-12-16 03:00:02',4,'passion','woman','../static/user_head_pic/user1544900401.804436.jpg','123','110','Beijing','2018-10-29 00:36:32','user','热爱生活的傻缺'),('2018-10-27 17:38:06','2018-12-16 02:59:50',5,'passion_wo','man','../static/user_head_pic/user1544900389.741089.jpg','123456','1234567','Beijing','2018-10-29 00:33:05','user','oooooh');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_know`
--

DROP TABLE IF EXISTS `user_know`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_know` (
  `user_id` int(11) NOT NULL,
  `know_id` int(11) NOT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`,`know_id`),
  KEY `know_id` (`know_id`),
  CONSTRAINT `user_know_ibfk_1` FOREIGN KEY (`know_id`) REFERENCES `know` (`id`),
  CONSTRAINT `user_know_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_know`
--

LOCK TABLES `user_know` WRITE;
/*!40000 ALTER TABLE `user_know` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_know` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-16  3:32:14
