CREATE TABLE `rj_period_tb` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `period_name` VARCHAR(10) NOT NULL COMMENT 'Period name/term used for the period (e.g 2H2020)',
    `period_start_date`DATETIME NOT NULL COMMENT 'Start date of the period',
    `period_end_date` DATETIME NOT NULL COMMENT 'End date of the period',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `rj_system_tb` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `system_name` VARCHAR(100) NOT NULL COMMENT 'System name',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `rj_system_status_tb` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `period_id` INT(10) UNSIGNED NOT NULL COMMENT 'rj_period_tb.id',
    `system_id` INT(10) UNSIGNED NOT NULL COMMENT 'rj_system_tb.id',
    `sup` FLOAT COMMENT 'System Usability Percentage',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `rj_system_defects_tb` (
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `system_status_id` INT(10) UNSIGNED NOT NULL COMMENT 'rj_system_status_tb.id',
    `defect_description` VARCHAR(256) NOT NULL COMMENT 'Defect description',
    `date_reported` DATETIME NOT NULL COMMENT 'Date defect was reported',
    `date_fixed_released` DATETIME NOT NULL COMMENT 'Date fix for the defect was released',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;