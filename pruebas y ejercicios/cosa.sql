CREATE TABLE datospersonales (
    secuencia NUMERIC(3) NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    apellido2 VARCHAR(20),
    coddep NUMERIC(3) NOT NULL,
    tipo VARCHAR(1) NOT NULL
);
create table cuentacorriente(
	entidad numeric(4) not null,
    sucursal numeric(4) not null,
    dcontrol numeric(2) not null,
    cuenta numeric(12) not null,
    saldo numeric(8,2) default 0
);
create table curso(
	codcurso numeric(2) not null,
    numhoras numeric(2) not null,
    aula varchar(3) not null
);

alter table curso
add constraint curso_pk primary key(codcurso);

alter table datospersonales
add constraint datospersonales_pk primary key(secuencia, coddep);

alter table datospersonales
add constraint ch_inh_datospersonales check(tipo in ("D", "R"));


CREATE TABLE empleado(
    dni varchar(10) primary key,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    apellido2 VARCHAR(20),
    coddep NUMERIC(3) NOT NULL,
    tipo VARCHAR(1) not null,
    numss varchar(20) not null
);
create table lugar(
	aula varchar(2) primary key,
    descripcion varchar(30) not null
);

alter table curso
add constraint curso_lugar_fk foreign key(aula) references lugar(aula);