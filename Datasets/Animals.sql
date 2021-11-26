-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Creato il: Nov 26, 2021 alle 20:15
-- Versione del server: 10.4.21-MariaDB
-- Versione PHP: 7.3.31

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
-- Struttura della tabella `species`
--

CREATE TABLE `Animals` (
  `animal_id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `description` text DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `species`
--

INSERT INTO `Animals` (`animal_id`, `name`, `description`, `parent_id`) VALUES
(1, 'Animal', NULL, NULL),
(2, 'Mammal', NULL, 1),
(3, 'Bird', NULL, 1),
(4, 'Fish', NULL, 1),
(5, 'Cat', NULL, 2),
(6, 'Dog', NULL, 2),
(7, 'Lion', NULL, 2),
(8, 'Pheasant', NULL, 3),
(9, 'Parrot', NULL, 3),
(10, 'Eagle', NULL, 3),
(11, 'Shark', NULL, 4),
(12, 'Clownfish', NULL, 4),
(13, 'Swordfish', NULL, 4);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `species`
--
ALTER TABLE `Animals`
  ADD PRIMARY KEY (`animal_id`),
  ADD KEY `parent_child` (`parent_id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `species`
--
ALTER TABLE `Animals`
  MODIFY `animal_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `species`
--
ALTER TABLE `Animals`
  ADD CONSTRAINT `parent_child` FOREIGN KEY (`parent_id`) REFERENCES `species` (`animal_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
