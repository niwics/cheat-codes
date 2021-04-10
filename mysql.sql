CREATE TABLE `players` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `player` ENUM('roger','rafa','nole') NOT NULL,
  `notes` TEXT DEFAULT NULL,
  `start_date` DATE NOT NULL,
  `titles` SMALLINT(4) NOT NULL,
  `date_created` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`player`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ALTER TABLE
ALTER TABLE players MODIFY `titles` TINYINT NOT NULL;
ALTER TABLE players ADD COLUMN `no1_weeks` TINYINT NOT NULL AFTER `titles`;