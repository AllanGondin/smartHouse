use gerenciador;


CREATE TABLE disp_infos(
  `cod_id` VARCHAR(50),
  `nome_dispositivo` VARCHAR(50),
  `ip_dispositivo` VARCHAR(50),
  `comodo` VARCHAR(50),
  PRIMARY KEY (`cod_id`))

CREATE TABLE quarto_2(
  `cod_id` VARCHAR(50),
  `nome_dispositivo` VARCHAR(50),
  `ip_dispositivo` VARCHAR(50),
  `status_dispositivo` VARCHAR(10),
  PRIMARY KEY (`cod_id`)
  )


CREATE TABLE quarto_1(
  `cod_id` VARCHAR(50),
  `nome_dispositivo` VARCHAR(50),
  `ip_dispositivo` VARCHAR(50),
  `status_dispositivo` VARCHAR(10),
  PRIMARY KEY (`cod_id`))
  

CREATE TABLE sala(
  `cod_id` VARCHAR(50),
  `nome_dispositivo` VARCHAR(50),
  `ip_dispositivo` VARCHAR(50),
  `status_dispositivo` VARCHAR(10),
  PRIMARY KEY (`cod_id`))
  


CREATE TABLE cozinha(
  `cod_id` VARCHAR(50),
  `nome_dispositivo` VARCHAR(50),
  `ip_dispositivo` VARCHAR(50),
  `status_dispositivo` VARCHAR(10),
  PRIMARY KEY (`cod_id`))
  
  CREATE TABLE garagem(
  `cod_id` VARCHAR(50),
  `nome_dispositivo` VARCHAR(50),
  `ip_dispositivo` VARCHAR(50),
  `status_dispositivo` VARCHAR(10),
  PRIMARY KEY (`cod_id`))
  
   CREATE TABLE lavanderia(
  `cod_id` VARCHAR(50) NOT NULL,
  `nome_dispositivo` VARCHAR(50),
  `ip_dispositivo` VARCHAR(50),
  `status_dispositivo` VARCHAR(10),
  PRIMARY KEY (`cod_id`))