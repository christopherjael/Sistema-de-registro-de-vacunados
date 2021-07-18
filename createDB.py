import sqlite3

#CREACION DE LA BASE DE DATOS Y LAS TABLAS
connection = sqlite3.connect('dbVacuna.db')
cursor = connection.cursor()

def createDB():

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Vacunas(
        ID_Vacuna INT AUTO_INCREMENT,
        Nombre VARCHAR(50) NOT NULL,
        PRIMARY KEY (ID_Vacuna)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Provincias(
        ID_Provincia INT AUTO_INCREMENT,
        Nombre VARCHAR(50) NOT NULL,
        PRIMARY KEY(ID_Provincia)
    );
    ''')
    

    cursor.execute('''  
    CREATE TABLE IF NOT EXISTS Vacunados(
        Cedula VARCHAR(13),
        Nombre VARCHAR(50) NOT NULL,
        Apellido VARCHAR(50) NOT NULL,
        Telefono VARCHAR(12) NOT NULL,
        ID_Vacuna INT NOT NULL,
        ID_Provincia INT NOT NULL,
        Fecha_Primera_Dosis DATE NOT NULL,
        Fecha_Segunda_Dosis DATE NULL,
        Fecha_Tercera_Dosis DATE NULL,
        PRIMARY KEY(Cedula)
        CONSTRAINT fk_Vacuna FOREIGN KEY (ID_Vacuna) REFERENCES Vacunas(ID_Vacuna),
        CONSTRAINT fk_Provincia FOREIGN KEY (ID_Provincia) REFERENCES Provincias(ID_Provincia)
    );
    ''')

    connection.commit()
    pass
