-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2019 at 04:25 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `entry_manage`
--

-- --------------------------------------------------------

--
-- Table structure for table `host`
--

CREATE TABLE `host` (
  `Name` varchar(20) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `host`
--

INSERT INTO `host` (`Name`, `Phone`, `Email`, `Address`) VALUES
('pragya', '111', 'aaaa', 'aaa'),
('ppp', '555', 'ppp', 'ppp'),
('Puchu', '7894561222', 'pouchu@gmail.com', 'agra');

-- --------------------------------------------------------

--
-- Table structure for table `visitor`
--

CREATE TABLE `visitor` (
  `Name` varchar(20) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Host` varchar(20) NOT NULL,
  `Check-in` timestamp NULL DEFAULT NULL,
  `Check_out` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `visitor`
--

INSERT INTO `visitor` (`Name`, `Address`, `Phone`, `Email`, `Host`, `Check-in`, `Check_out`) VALUES
('Nidhi', 'delhi', '7534126987', 'nidhi@gmail.com', 'pragya', '2019-12-01 02:08:16', '2019-12-01 02:09:41'),
('Pragya', 'Kanpur', '8349380737', 'pragya123@gmail.com', 'Santosh', '2019-11-30 23:34:04', '0000-00-00 00:00:00'),
('Pushpa', 'lko', '4567891230', 'pushpa123@gmail.com', 'Pragya', '2019-11-30 23:42:31', '0000-00-00 00:00:00'),
('Santosh', 'Kanpur', '1234567890', 'santosh123@gmail.com', '', '2019-11-29 13:32:37', '2019-11-30 23:35:06'),
('santosh', 'agra', '4567891239', 'santosh@gmail.com', 'pragya', '2019-12-01 02:17:49', '0000-00-00 00:00:00'),
('Vishal', 'lko', '4567891233', 'vishal@123', 'santosh', '2019-11-30 23:37:36', '0000-00-00 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `visitor`
--
ALTER TABLE `visitor`
  ADD PRIMARY KEY (`Name`,`Phone`,`Host`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
