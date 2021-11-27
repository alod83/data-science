-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Creato il: Nov 27, 2021 alle 10:47
-- Versione del server: 10.4.21-MariaDB
-- Versione PHP: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Animals`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `Animals_nested`
--

CREATE TABLE `Animals_nested` (
  `animal_id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `left_value` int(11) NOT NULL,
  `right_value` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `Animals_nested`
--

INSERT INTO `Animals_nested` (`animal_id`, `name`, `left_value`, `right_value`) VALUES
(1, 'Animal', 1, 26),
(2, 'Mammal', 2, 9),
(3, 'Bird', 10, 17),
(4, 'Fish', 18, 25),
(5, 'Cat', 3, 4),
(6, 'Dog', 5, 6),
(7, 'Lion', 7, 8),
(8, 'Pheasant', 11, 12),
(9, 'Parrot', 13, 14),
(10, 'Eagle', 15, 16),
(11, 'Shark', 19, 20),
(12, 'ClownFish', 21, 22),
(13, 'Swordfish', 23, 24);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `Animals_nested`
--
ALTER TABLE `Animals_nested`
  ADD PRIMARY KEY (`animal_id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `Animals_nested`
--
ALTER TABLE `Animals_nested`
  MODIFY `animal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
