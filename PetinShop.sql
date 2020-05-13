-- Database: PetinShop

-- DROP DATABASE "PetinShop";

/* CREATE DATABASE "PetinShop"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1; */
	
create table if not exists Cliente(
	id_Cliente serial primary key,
    nombre varchar(100),
    apellidos varchar(100),
    dni varchar(100) unique not null,
    direccion varchar(100),
    telefono int
);
create table if not exists Sueldo(
	id_Sueldo serial primary key,
    total int,
    base int not null,
    comisiones int default 0
);
create table if not exists Vendedor(
	id_Vendedor serial primary key,
    nombre varchar(100),
    apellidos varchar(100),
    dni varchar(100) unique not null,
    direccion varchar(100),
    telefono int,
	fk_id_Sueldo int not null,
    foreign key (fk_id_Sueldo) references Sueldo(id_Sueldo)
);
create table if not exists Venta(
	id_Venta serial primary key,
    precioTotal float not null
);
create table if not exists Cliente_Vendedor_Venta(
	id_Compra serial primary key,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fk_id_Cliente int not null,
    fk_id_Vendedor int not null,
    fk_id_Venta int not null,
    foreign key (fk_id_Cliente) references Cliente(id_Cliente),
    foreign key (fk_id_Vendedor) references Vendedor(id_Vendedor),
    foreign key (fk_id_Venta) references Venta(id_Venta)
);
create table if not exists Categoria(
	id_Categoria serial primary key,
    nombre varchar(100) unique not null,
    descripcion varchar(500)
);
create table if not exists Proveedor(
	id_Proveedor serial primary key,
    empresa varchar(100),
    cif varchar(100) unique not null,
    direccion varchar(100)
);
create table if not exists Producto(
	id_Producto serial primary key,
    nombre varchar(100)unique not null,
    descripcion varchar(100),
    cantidad int default 0,
    precio float not null,
    altura float,
    anchura float,
    peso float,
    fk_id_Categoria int not null,
    fk_id_Proveedor int not null,
    foreign key (fk_id_Categoria) references Categoria(id_Categoria),
    foreign key (fk_id_Proveedor) references Proveedor(id_Proveedor)
);
create table if not exists Venta_Producto(
	id_Venta_Producto serial primary key,
	fk_id_Producto int not null,
    fk_id_Venta int not null,
    foreign key (fk_id_Venta) references Venta(id_Venta),
    foreign key (fk_id_Producto) references Producto(id_Producto)
);

--------------------------------------------------------------------------

INSERT INTO Proveedor (empresa,cif,direccion) VALUES ('BigMat', 'B45697713', 'C/Alcala 234');
INSERT INTO Proveedor (empresa,cif,direccion) VALUES ('A2Project', 'M12345678', 'C/Pedro Salinas 13');
INSERT INTO Proveedor (empresa,cif,direccion) VALUES ('ComerCity', 'L64758392', 'C/Antonio Puertas 55');
INSERT INTO Proveedor (empresa,cif,direccion) VALUES ('DRH', 'P432111456', 'C/Peloponeso 28');

INSERT INTO Categoria (nombre, descripcion) VALUES ('Comida','Las mejores comidas para tus mascotas, saludables y perfectas para su dieta.');
INSERT INTO Categoria (nombre, descripcion) VALUES ('Accesorios','Abrigos, collares, arneses... etc. Lleva a tu mascota con los mejores accesorios.');
INSERT INTO Categoria (nombre, descripcion) VALUES ('Juguetes','¿Tu mascota se aburre? Dale una sorpresa con estos juguetes que le encantaran y se lo pasaran en grande.');

INSERT INTO Producto (nombre, descripcion, cantidad, precio, altura, anchura, peso, fk_id_Categoria, fk_id_Proveedor) 
	VALUES ('Pienso','Comida para perros',100,24.99,10,5,10,1,1);
INSERT INTO Producto (nombre, descripcion, cantidad, precio, altura, anchura, peso, fk_id_Categoria, fk_id_Proveedor) 
	VALUES ('Lata salmon','Comida para gatos',100,14.99,5,2,2,1,2);
INSERT INTO Producto (nombre, descripcion, cantidad, precio, altura, anchura, peso, fk_id_Categoria, fk_id_Proveedor) 
	VALUES ('Arnes K9','Arnes para perros',50,31.99,30,40,1,2,3);
INSERT INTO Producto (nombre, descripcion, cantidad, precio, altura, anchura, peso, fk_id_Categoria, fk_id_Proveedor) 
	VALUES ('Chubasquero','Abrigo de lluvia para perros',20,61.99,80,80,3,2,4);
INSERT INTO Producto (nombre, descripcion, cantidad, precio, altura, anchura, peso, fk_id_Categoria, fk_id_Proveedor) 
	VALUES ('Raton Robotico','Raton de juguete para gato',50,17.99,10,10,0.5,3,4);
INSERT INTO Producto (nombre, descripcion, cantidad, precio, altura, anchura, peso, fk_id_Categoria, fk_id_Proveedor) 
	VALUES ('Parque infantil','Parque infantil para pajaros',20,13.99,20,20,2,3,1);
  
INSERT INTO Sueldo (base, comisiones, total)
	VALUES (1800, 500, 2300);
INSERT INTO Sueldo (base, comisiones, total)
	VALUES (1100, 350, 1450);    
  
INSERT INTO Vendedor (nombre, apellidos, dni, direccion, telefono,fk_id_Sueldo) 
	VALUES ('Alejandro','Martinez Herreros','45612378C','C/Manuel Becerra 1',654654654,1);
INSERT INTO Vendedor (nombre, apellidos, dni, direccion, telefono,fk_id_Sueldo) 
	VALUES ('Luis','Borrallo','75648325L','C/Malmoe 5',666077789,2);
    
INSERT INTO Cliente  (nombre, apellidos, dni, direccion, telefono) 
	VALUES ('Oscar','Ledesma','33322111C','C/Falsa 123',600500103);
INSERT INTO Cliente  (nombre, apellidos, dni, direccion, telefono) 
	VALUES ('Alberto','Esteban','12312312T','C/Retamar 21',65478932);
INSERT INTO Cliente  (nombre, apellidos, dni, direccion, telefono) 
	VALUES ('Francisco','Garzó','66666666L','C/Altotajo 44',66987451);
    


INSERT INTO Venta (precioTotal) VALUES (39.98);
INSERT INTO Venta (precioTotal) VALUES (94.97);
INSERT INTO Venta (precioTotal) VALUES (13.99);

INSERT INTO Cliente_Vendedor_Venta (fk_id_Cliente,fk_id_Vendedor, fk_id_Venta) VALUES (2,1,1);
INSERT INTO Cliente_Vendedor_Venta (fk_id_Cliente,fk_id_Vendedor, fk_id_Venta) VALUES (3,1,2);
INSERT INTO Cliente_Vendedor_Venta (fk_id_Cliente,fk_id_Vendedor, fk_id_Venta) VALUES (1,2,3);
    
INSERT INTO Venta_Producto (fk_id_Producto,fk_id_Venta) VALUES (1,1);
INSERT INTO Venta_Producto (fk_id_Producto,fk_id_Venta) VALUES (3,1);
INSERT INTO Venta_Producto (fk_id_Producto,fk_id_Venta) VALUES (2,2);
INSERT INTO Venta_Producto (fk_id_Producto,fk_id_Venta) VALUES (5,2);
INSERT INTO Venta_Producto (fk_id_Producto,fk_id_Venta) VALUES (4,2);
INSERT INTO Venta_Producto (fk_id_Producto,fk_id_Venta) VALUES (6,3);
 