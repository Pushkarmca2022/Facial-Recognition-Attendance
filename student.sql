-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2021 at 01:52 PM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `dep` varchar(250) NOT NULL,
  `course` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `sem` varchar(255) NOT NULL,
  `id` int(10) NOT NULL,
  `name` varchar(250) NOT NULL,
  `divison` varchar(250) NOT NULL,
  `roll` varchar(250) NOT NULL,
  `gen` varchar(250) NOT NULL,
  `dob` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `phone` varchar(250) NOT NULL,
  `address` varchar(250) NOT NULL,
  `teacher` varchar(250) NOT NULL,
  `photo` varchar(250) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`dep`, `course`, `year`, `sem`, `id`, `name`, `divison`, `roll`, `gen`, `dob`, `email`, `phone`, `address`, `teacher`, `photo`) VALUES
('coumputer', 'MCA', '2019', 'Semester-1', 1, 'pushakar', 'a', '1', 'Male', '12/12/12', 'pushkar@gmail.com', '123', 'g', 'sir', 'yes'),
('coumputer', 'MCA', '2020', 'Semester-1', 2, 'Golu', 'a', '2', 'Male', '12/12/12', 'g', '5', 'g', 'sir', 'yes'),
('coumputer', 'MCA', '2019', 'Semester-1', 3, 'bx', 'a', '3', 'Male', '12/12/12', 'kdsfjl', '11', '11', 'ow', 'yes'),
('it', 'MCA', '2019', 'Semester-2', 4, 'govi', 'firs', '5', 'Other', '12/12/12', 'govi@gmail.com', '243', 'f', 'ff', 'yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
