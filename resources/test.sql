-- for mysql sql.
-- user: tester
-- pwd: 123456

CREATE TABLE IF NOT EXISTS `test` (
	`id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增ID',
	`content` varchar(255) NOT NULL DEFAULT '' COMMENT '内容',
	`create_time` timestamp NOT NULL DEFAULT '1980-01-01 00:00:00',
  	`update_time` timestamp NOT NULL DEFAULT '1980-01-01 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;