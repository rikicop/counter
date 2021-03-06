BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `count_transaccion` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`cuenta`	varchar ( 100 ) NOT NULL,
	`nombre`	varchar ( 50 ) NOT NULL,
	`movimiento`	varchar ( 100 ) NOT NULL,
	`asiento`	varchar ( 100 ) NOT NULL,
	`banco`	varchar ( 100 ) NOT NULL,
	`codant`	varchar ( 100 ) NOT NULL,
	`ctaabono`	varchar ( 100 ) NOT NULL,
	`ctacargo`	varchar ( 100 ) NOT NULL,
	`moneda`	varchar ( 100 ) NOT NULL,
	`nivel`	varchar ( 100 ) NOT NULL,
	`proyecto`	varchar ( 100 ) NOT NULL,
	`oficina`	varchar ( 100 ) NOT NULL
);

INSERT INTO `count_cincuenta` (cuenta,nombre,movimiento,asiento,banco,codant,ctaabono,ctacargo,moneda,nivel,proyecto,oficina) VALUES ('7651','CAJA CHICA','si','si','5656456','','','','001','si','',''),
 ('654422','REMESA INEDITA','si','si','','','','','001','si','','004'),
 ('74252','CAJA RENDIDORA','si','si','','','','','001','si','','1222'),
 ('4323455','CAJA CHICA','si','si','','','','','001','si','','234234'),
 ('531121','REMESA FAMILIAR','SI','','','','','','','','','42111'),
 ('0123','CAJA PEQUEÑA','si','si','','','','','001','si','','002'),
 ('76511','REMESA FAMILIAR','SI','','','','','','','','','0044451'),
 ('43200','CAJA GRANDE','si','si','','','','','001','si','','1222'),
 ('52097','CAJA CHICA','si','si','','','','','001','si','','0044451'),
 ('46116','REMESA FAMILIAR','SI','','','','','','','','','0045'),
 ('432842','CAJA PEQUEÑA','si','si','','','','','003','si','','77777'),
 ('61151','CAJA','SI','','','','','','','','','0044451'),
 ('23414','REMESA FAMILIAR','SI','','','','','','','','','0044451'),
 ('7641','CAJA','SI','','','','','','','','','77777'),
 ('7651975','CAJA','SI','','','','','','','','','0045'),
 ('432412','REMESA FAMILIAR','si','si','','','','','001','si','','77777'),
 ('764125','CAJA','No','','','','','','','','','0044451'),
 ('012351','CAJA ELECTRICA','SI','','','','','','','','','002'),
 ('726456','CAJA','SI','','','','','','','','','1222'),
 ('22611','REMESA','No','','','','','','','','','1222'),
 ('432163','CAJA CHICA','SI','','','','','','','','','1222'),
 ('1764543','CAJA','SI','','','','','','','','','004511'),
 ('1526','CAJA','SI','','','','','','','','','1222'),
 ('472','REMESA FAMILIAR','SI','','','','','','','','','1222'),
 ('7420','CAJA','SI','','','','','','','','','77777'),
 ('83541','CAJA','SI','','','','','','','','','0044451'),
 ('432165','CAJA','SI','','','','','','','','','0044451'),
 ('8251','REMESA FAMILIAR','SI','','','','','','','','','002'),
 ('94','CAJA CHICA','SI','','','','','','','','','0044451'),
 ('844','CAJA','No','','','','','','','','','0045'),
 ('840','CAJA','SI','','','','','','','','','12'),
 ('73','CAJA','SI','','','','','','','','','002'),
 ('921','CAJA CHICA','SI','','','','','','','','','0044451'),
 ('8311','CAJA','SI','','','','','','','','','004'),
 ('72','CAJA','SI','','','','','','','','','0021'),
 ('21','REMESA FAMILIAR','SI','','','','','','','','','1222'),
 ('491','REMESA','SI','','','','','','','','','77'),
 ('271','CAJA','SI','','','','','','','','','0029'),
 ('40','CAJA CHICA','SI','','','','','','','','','77'),
 ('61','CAJA','SI','','','','','','','','','0021'),
 ('510','CAJA','SI','','','','','','','','','0043'),
 ('401','CAJA','No','','','','','','','','','054'),
 ('41012','CAJA CHICA','SI','','','','','','','','','0045'),
 ('518','CAJA','SI','','','','','','','','','1002'),
 ('151','CAJA CHICA','SI','','','','','','','','','77'),
 ('765198','REMESA FAMILIAR','SI','','','','','','','','','1222'),
 ('16','CAJA','SI','','','','','','','','','1222'),
 ('598','CAJA','SI','','','','','','','','','0034'),
 ('772','REMESA','SI','','','','','','','','','65'),
 ('41073','REMESA FAMILIAR','No','','','','','','','','','0302'),
 ('5867','CAJA','SI','','','','','','','','','0045'),
 ('2','REMESA FAMILIAR','SI','','','','','','','','','002'),
 ('6754','CAJA','No','','','','','','','','','0027'),
 ('740','CAJA','SI','','','','','','','','','14'),
 ('626','CAJA','SI','','','','','','','','','0023'),
 ('7401','REMESA FAMILIAR','SI','','','','','','','','','12'),
 ('81','CAJA','SI','','','','','','','','','71'),
 ('413','CAJA CHICA','SI','','','','','','','','','0023'),
 ('7254','CAJA CHICA','SI','','6546','','','','','','',''),
 ('6124','CAJA','No','','','','','','','','','12');

CREATE VIEW `registros` AS SELECT * FROM count_transaccion;
COMMIT;
