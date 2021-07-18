from functions import *
from createDB import *


createDB()
limpiar()

while True:
    print('Bienvenido/a Al Sistema de Registros de Vacunados\n')
    print('Menu')
    print('1. Registrar Vacunado')
    print('2. Modificar vacunado')
    print('3. Eliminar Vacunado')
    print('4. Exportar lista de Vacunados')
    print('5. configuraciones (Provincias, Marcas de Vacunas)')
    print('6. Salir del programa\n ')
    opcion = int(input('Introduce una opción\n> '))

    if opcion == 1:
        agregarVacunados()
        limpiar()
    elif opcion == 2:
        modificarVacunados()
        limpiar()
    elif opcion == 3:
        eliminarVacuandos()
        limpiar()
    elif opcion == 4:
        exportarVacuandos()
        limpiar()
    elif opcion == 5:
        limpiar()
        print('Submenu (Configuraciones)')
        print('1. Agregar Provincia')
        print('2. Modificar Provincia')
        print('3. Eliminar Provincia')
        print('4. Agregar Marca de Vacuna')
        print('5. Modicar Marca de Vacuna')
        print('6. Eliminar Marca de Vacuna')
        print('7. Volver al Menu Principal')
        print('8. Salir del programa\n ')
        opcionSub = int(input('Introduce una opción\n> '))

        if opcionSub == 1:
            agregarProvincia()
            limpiar()
        elif opcionSub == 2:
            modificarProvincia()
            limpiar()
        elif opcionSub == 3:
            eliminarProvincia()
            limpiar()
        elif opcionSub == 4:
            agregarVacuna()
            limpiar()
        elif opcionSub == 5:
            modificarVacuna()
            limpiar()
        elif opcionSub == 6:
            eliminarVacuna()
            limpiar()
        elif opcionSub == 7:
            False
            limpiar()
        elif opcionSub == 8:
            print('Saliendo del programa....')
            time.sleep(1)
            break