import os
from sqlite3.dbapi2 import enable_shared_cache
import time
import sqlite3
import webbrowser
from prettytable import PrettyTable,from_db_cursor

x = PrettyTable()

connection = sqlite3.connect('dbVacuna.db')
cursor = connection.cursor()

def limpiar():
    os.system('cls')

#PROVINCIAS
def verProvincias():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Provincias ORDER BY ID_Provincia ASC')
    x = from_db_cursor(cursor)
    print(x)
    pass

def agregarProvincia():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    print('Lista de Provincias')
    verProvincias()
    print('Agregar Provincias')
    idProvincia = int(input('Introduce el ID de la Provincia, o presiona ENTER para cancelar\n> '))
    nombreProvincia = input('Introduce el nombre de la Provincia, o presiona ENTER para cancelar\n> ')
    if nombreProvincia == '' or idProvincia == 0:
        return False
    else:
        cursor.execute(f"INSERT INTO Provincias VALUES ({idProvincia},'{nombreProvincia}')")
        connection.commit()
        print('Registro Completado')
        input('Presione ENTER para continuar')
        pass
    pass

def modificarProvincia():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    print('Modificar provincia')
    print('Lista de Provincia')
    verProvincias()
    idProvincia = int(input('Introduce el ID de la Provincia, o presiona ENTER para cancelar\n> '))
    nombreProvincia = input('Introduce el Nuevo Nombre de Provincia\n> ')
    if nombreProvincia == '':
        return False
    else:
        cursor.execute(f"UPDATE Provincias SET Nombre = '{nombreProvincia}' WHERE ID_Provincia = {idProvincia}")
        connection.commit()
        print('Provincia Modificada')
        input('Presione ENTER para continuar')
        pass
    pass

def eliminarProvincia():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    print('Eliminar provincia')
    print('Lista de Provincia')
    verProvincias()
    idProvincia = int(input('Introduce el ID de la Provincia, o presiona ENTER para cancelar\n> '))
    if idProvincia == '':
        return False
    else:
        cursor.execute(f'DELETE FROM Provincias WHERE ID_Provincia = {idProvincia}')
        connection.commit()
        print('Provincia Eliminada')
        input('Presione ENTER para continuar')
        pass
    pass






#VACUNAS
def verVacunas():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Vacunas ORDER BY ID_Vacuna ASC')
    x = from_db_cursor(cursor)
    print(x)
    pass

def agregarVacuna():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    print('Lista de Vacunas')
    verVacunas()
    print('Agregar Marca de Vacuna')
    idVacuna = int(input('Introduce el ID de la Vacuna, o presiona ENTER para cancelar\n> '))
    nombreVacuna= input('Introduce el nombre de la Vacuna, o presiona ENTER para cancelar\n> ')
    if nombreVacuna == '':
        return False
    else:
        cursor.execute(f"INSERT INTO Vacunas VALUES ({idVacuna},'{nombreVacuna}')")
        connection.commit()
        print('Registro Completado')
        input('Presione ENTER para continuar')
        pass
    pass

def modificarVacuna():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    print('Lista de Vacunas')
    verVacunas()
    print('Modificar Marca de Vacunas')
    idVacuna = int(input('Introduce el ID de la Vacuna, o presiona ENTER para cancelar\n> '))
    nombreVacuna = input('Introduce el Nuevo Nombre de Vacuna\n> ')
    if nombreVacuna == '':
        return False
    else:
        cursor.execute(f"UPDATE Vacunas SET Nombre = '{nombreVacuna}' WHERE ID_Vacuna = {idVacuna}")
        connection.commit()
        print('Marce de Vacuna Modificada')
        input('Presione ENTER para continuar')
        pass
    pass

def eliminarVacuna():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    print('Eliminar Vacuna')
    print('Lista de Vacunas')
    verVacunas()
    idVacuna = int(input('Introduce el ID de la Vacuna, o presiona ENTER para cancelar\n> '))
    if idVacuna == '':
        return False
    else:
        cursor.execute(f'DELETE FROM Vacunas WHERE ID_Vacuna = {idVacuna}')
        connection.commit()
        print('Vacuna Eliminada')
        input('Presione ENTER para continuar')
        pass
    pass


#VACUNADOS
def verVacunados():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Vacunados ORDER BY Nombre ASC')
    x = from_db_cursor(cursor)
    print(x)
    pass

def agregarVacunados():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    verVacunados()
    print('Registrar Vacunado/a')
    cedulaVacunado = input('Introduce la Cedula de Identidad del Vacunado\n >')
    usuarioExiste = False
    for rows in cursor.execute(f"SELECT Cedula, Nombre FROM Vacunados WHERE Cedula = '{cedulaVacunado}'"):
        if len(rows) > 0:
            usuarioExiste = True
            pass
        pass

    if usuarioExiste:
        print('El Usuario Ya existe, por lo que puede Agregar la fecha de la Nueva Dosis')
        fe_seg_dosiscedulaVacunado = input('Introduce la Fecha de las Segunda dosis del Vacunado: (ni aun tiene esta, no es necesario poner la fecha)\n >')
        fe_ter_dosiscedulaVacunado = input('Introduce la Fecha de la Tercera dosis del Vacunado: (ni aun tiene esta, no es necesario poner la fecha)\n >')

        if fe_seg_dosiscedulaVacunado == "":
            fe_seg_dosiscedulaVacunado = 'NULL'

        if fe_ter_dosiscedulaVacunado == '':
            fe_ter_dosiscedulaVacunado = 'NULL'

        cursor.execute(f"UPDATE Vacunados SET Fecha_Segunda_Dosis = '{fe_seg_dosiscedulaVacunado}', Fecha_Tercera_Dosis = '{fe_ter_dosiscedulaVacunado}' WHERE Cedula = '{cedulaVacunado}'")
        connection.commit()
    else:
        nombreVacunado = input('Introduce el Nombre del Vacunado\n >')
        apellidoVacunado = input('Introduce el Apellido del Vacunado\n >')
        telefonoVacunado = input('Introduce el Numero de Telefono del Vacunado\n >')
        verVacunas()
        id_vacunaVacunado = int(input('Introduce el ID de la Vacuna aplicada al Vacunado\n >'))
        verProvincias()
        id_provinciacedulaVacunado = int(input('Introduce la Provincia donde se le aplico la Vacuna al Vacunado\n >'))
        fe_pri_dosisVacunado = input('Introduce la Fecha de la Primera dosis del Vacunado\n >')
        fe_seg_dosiscedulaVacunado = input('Introduce la Fecha de las Segunda dosis del Vacunado: (ni aun tiene esta, no es necesario poner la fecha)\n >')
        fe_ter_dosiscedulaVacunado = input('Introduce la Fecha de la Tercera dosis del Vacunado: (ni aun tiene esta, no es necesario poner la fecha)\n >')

        if fe_seg_dosiscedulaVacunado == "":
            fe_seg_dosiscedulaVacunado = 'NULL'

        if fe_ter_dosiscedulaVacunado == '':
            fe_ter_dosiscedulaVacunado = 'NULL'

        cursor.execute(f"""
        INSERT INTO Vacunados 
        VALUES ('{cedulaVacunado}', '{nombreVacunado}','{apellidoVacunado}', '{telefonoVacunado}',{id_vacunaVacunado}, {id_provinciacedulaVacunado},'{fe_pri_dosisVacunado}', '{fe_seg_dosiscedulaVacunado}', '{fe_ter_dosiscedulaVacunado}')
        """)
        connection.commit()
        print('Registro Completado')
        input('Presione ENTER para continuar')
    pass

def modificarVacunados():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    verVacunados()
    print('Modificar Vacunados')
    cedulaVacunado = input('Introduce la Cedula de Identidad del Vacunado que quiere moficiar\n >')
    usuarioExiste = False
    for rows in cursor.execute(f"SELECT Cedula, Nombre FROM Vacunados WHERE Cedula = '{cedulaVacunado}'"):
        if len(rows) > 0:
            usuarioExiste = True
            pass
        pass

    if usuarioExiste:
        nombreVacunado = input('Introduce el Nombre del Vacunado\n >')
        apellidoVacunado = input('Introduce el Apellido del Vacunado\n >')
        telefonoVacunado = input('Introduce el Numero de Telefono del Vacunado\n >')
        verVacunas()
        id_vacunaVacunado = int(input('Introduce el ID de la Vacuna aplicada al Vacunado\n >'))
        verProvincias()
        id_provinciacedulaVacunado = int(input('Introduce la Provincia donde se le aplico la Vacuna al Vacunado\n >'))
        fe_pri_dosisVacunado = input('Introduce la Fecha de la Primera dosis del Vacunado\n >')
        fe_seg_dosiscedulaVacunado = input('Introduce la Fecha de las Segunda dosis del Vacunado: (ni aun tiene esta, no es necesario poner la fecha)\n >')
        fe_ter_dosiscedulaVacunado = input('Introduce la Fecha de la Tercera dosis del Vacunado: (ni aun tiene esta, no es necesario poner la fecha)\n >')

        if fe_seg_dosiscedulaVacunado == "":
            fe_seg_dosiscedulaVacunado = 'NULL'

        if fe_ter_dosiscedulaVacunado == '':
            fe_ter_dosiscedulaVacunado = 'NULL'

        cursor.execute(f"""
        UPDATE Vacunados 
        SET 
        Nombre = '{nombreVacunado}', 
        Apellido = '{apellidoVacunado}', 
        Telefono = '{telefonoVacunado}', 
        ID_Vacuna = {id_vacunaVacunado}, 
        ID_Provincia= {id_provinciacedulaVacunado}, 
        Fecha_Primera_Dosis = '{fe_pri_dosisVacunado}',
        Fecha_Segunda_Dosis = '{fe_seg_dosiscedulaVacunado}',
        Fecha_Tercera_Dosis = '{fe_ter_dosiscedulaVacunado}'
        WHERE Cedula = '{cedulaVacunado}'""")
        connection.commit()
        print('Modificacion Completado')
        input('Presione ENTER para continuar')
    else:
        print('El Vacunado No existe, Intente otra vez con otro')
        input('')
        pass
    pass

def eliminarVacuandos():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    verVacunados()
    print('Eliminar Vacunados')
    cedulaVacunado = input('Introduce la Cedula de Identidad del Vacunado que quiere moficiar\n >')
    usuarioExiste = False
    for rows in cursor.execute(f"SELECT Cedula, Nombre FROM Vacunados WHERE Cedula = '{cedulaVacunado}'"):
        if len(rows) > 0:
            usuarioExiste = True
            pass
        pass
    if usuarioExiste:
        cursor.execute(f"DELETE FROM Vacunados WHERE Cedula = '{cedulaVacunado}'")
        connection.commit()
        print('Eliminacion Completado')
        input('Presione ENTER para continuar')
    else:
        print('El Vacunado No existe, Intente otra vez con otro')
        input('')
        pass
    pass


#EXPORTAR LISTA DE VACUNADOS DE
def exportarVacuandos():
    connection = sqlite3.connect('dbVacuna.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * 
    FROM Vacunados 
    ORDER BY Nombre ASC""")
    x = from_db_cursor(cursor)
    tablaVacunados = x.get_html_string(attributes={"class":"table table table-striped table-bordered"})
    html = f"""
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <title>Vacunados</title>
    </head>

    <body>
    <h3 class="text-center">Lista de Vacunados</h3>
    <div class="container">
        {tablaVacunados}
    </div>
    </body>

    </html>
    """
    f = open('index.html', 'w')
    f.write(html)
    f.close
    webbrowser.open('index.html')
    pass