# SISTEMA DE TARJETA QROBUS
costo = 11.00
limite = 2

# La coma es necesaria para que Python la reconozca como tupla de un solo elemento
fechas = ("XX/YY/ZZ",)


# PARTE 1 - DATOS DE LA TARJETA
def hacer_datos(nombre, saldo):
    datos = {
        "nombre": nombre,
        "saldo": saldo,
        "deuda": 0,
        "viajes": 0
    }

    # return regresa los datos para poder utilizarlos fuera de la función
    return datos


def mostrar(datos):
    print("QROBUS")
    print(f"Nombre: {datos['nombre']}")
    print(f"Saldo: ${datos['saldo']:.2f}")
    print(f"Deuda: ${datos['deuda']:.2f}")
    print(f"Viajes a crédito: {datos['viajes']}")


# PARTE 2 - HISTORIAL
def agregar_historial(lista, texto):
    fecha = fechas[0]
    dato = (fecha, texto)

    # Agrega los datos
    lista.append(dato)


# PARTE 3 - COBRO DEL VIAJE

def cobrar(datos, lista):
    if datos["saldo"] >= costo:
        # Si el saldo es suficiente, se descuenta el costo del viaje
        datos["saldo"] = datos["saldo"] - costo

        print("Viaje aceptado.")
        print(f"Saldo restante: ${datos['saldo']:.2f}")

        # Se registra el viaje en el historial
        agregar_historial(lista, f"Viaje pagado - ${costo:.2f}")

    else:
        # Si no hay suficiente saldo, se revisa si todavía puede utilizar sus dos "vidas extra"

        if datos["viajes"] < limite:
            # Se suma el costo del viaje a la deuda
            datos["deuda"] = datos["deuda"] + costo

            # Se suma 1 a los viajes a crédito utilizados
            datos["viajes"] = datos["viajes"] + 1

            print("Saldo insuficiente, pero el viaje fue aceptado")
            print(f"Deuda: ${datos['deuda']:.2f}")

            # Se calcula cuántas oportunidades quedan
            print(
                f"Oportunidades restantes: "
                f"{limite - datos['viajes']}"
            )

            # Se guarda el movimiento
            agregar_historial(
                lista,
                f"Viaje a crédito - ${costo:.2f}")

        else:
            # Si ya utilizó las 2 oportunidades, no puede viajar
            print("Tarjeta bloqueada")
            print(f"Debe pagar ${datos['deuda']:.2f}")

            # Se guarda también el viaje rechazado
            agregar_historial(
                lista,
                "Viaje rechazado")


# PARTE 4 - RECARGA

def recargar(datos, lista):
    while True:

        print("RECARGA")

        # Lista con las denominaciones aceptadas
        monedas = [1, 2, 5, 10, 20, 50, 100, 200, 500]

        # Aquí se va acumulando el valor total de las monedas y billetes
        recarga = 0

        # for recorre cada denominación de la lista
        for dinero in monedas:

            # Este while sirve para volver a preguntar si el usuario mete un valor incorrecto
            while True:
                try:
                    cantidad = int(
                        input(f"¿Cuántos de ${dinero}? ")
                    )

                    # NO PERMITE DINERO NEGATIVO!!!
                    if cantidad < 0:
                        print("No puede ingresar números negativos")
                        continue

                    # Se multiplica la denominación por la cantidad
                    recarga = recarga + dinero * cantidad
                    break

                except ValueError:
                    # Si escribe letras o algo que no sea un entero, el programa no se rompe
                    print("Escriba un número entero")

        # No se puede hacer una recarga de $0
        if recarga == 0:
            print("Debe ingresar al menos una moneda o billete")

            # Regresa al inicio del menú de recarga
            continue
        print(f"Total: ${recarga:.2f}")

        # Revisa si el usuario tiene una deuda
        if datos["deuda"] > 0:

            # Guarda el valor de la deuda antes de modificarlo
            deuda = datos["deuda"]
            if recarga >= datos["deuda"]:
                recarga = recarga - datos["deuda"]
                datos["deuda"] = 0
                datos["viajes"] = 0
                datos["saldo"] = datos["saldo"] + recarga
                print("Se pagó el adeudo.")
                print("Tarjeta desbloqueada.")
                print(f"Saldo: ${datos['saldo']:.2f}")
                # Se registra la operación
                agregar_historial(
                    lista,
                    f"Recarga y pago de deuda de ${deuda:.2f}"
                )
            else:
                datos["deuda"] = datos["deuda"] - recarga
                print(
                    f"Deuda restante: ${datos['deuda']:.2f}"
                )
                # Se registra el abono
                agregar_historial(
                    lista,
                    f"Abono de ${recarga:.2f} a la deuda"
                )

        else:
            datos["saldo"] = datos["saldo"] + recarga

            print(f"Nuevo saldo: ${datos['saldo']:.2f}")

            agregar_historial(
                lista,
                f"Recarga normal - ${recarga:.2f}"
            )
        break


# PARTE 5 - VER HISTORIAL
def ver_historial(lista):

    if len(lista) == 0:
        print("No hay operaciones")

    else:
        for i in range(len(lista)):

            # Saca los dos valores de la tupla
            fecha, texto = lista[i]

            # Muestra la posición, la fecha y la operación
            print(f"{i + 1}. {fecha} - {texto}")


# PARTE 6 - ARCHIVOS
def guardar(lista):

    try:
        # "a" significa agregar información al archivo
        # with hace que el archivo se cierre automáticamente

        with open(
            "historial_qrobus.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            # Recorremos todas las operaciones de la lista
            for dato in lista:
                fecha, texto = dato

                # write escribe texto dentro del archivo
                archivo.write(
                    f"{fecha} - {texto}\n"
                )

        print("Historial guardado")

    except PermissionError:
        # Este error aparece si no se tiene permiso para escribir en el archivo
        print("No se pudo guardar el archivo")


def leer():

    try:
        # "r" significa leer el archivo

        with open(
            "historial_qrobus.txt",
            "r",
            encoding="utf-8"
        ) as archivo:

            # read() obtiene todo el contenido
            texto = archivo.read()

        print("HISTORIAL GUARDADO")
        print(texto)

    except FileNotFoundError:
        # Este error aparece si el archivo no existe
        print("El archivo no existe")

    except PermissionError:
        # Este error aparece si no se tiene permiso para leer
        print("No se pudo leer el archivo")


# PARTE 7 - MENÚ
def menu(datos, lista):

    while True:

        print("TARJETA QROBUS")
        print("1. Hacer viaje")
        print("2. Recargar")
        print("3. Ver tarjeta")
        print("4. Ver historial")
        print("5. Guardar historial")
        print("6. Leer historial")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cobrar(datos, lista)

        elif opcion == "2":
            recargar(datos, lista)

        elif opcion == "3":
            mostrar(datos)

        elif opcion == "4":
            ver_historial(lista)

        elif opcion == "5":
            guardar(lista)

        elif opcion == "6":
            leer()

        elif opcion == "7":
            print("Gracias por utilizar Qrobus")


            break

        else:
            print("Opción no válida")


# PARTE 8 - INICIO DEL PROGRAMA
print("SISTEMA QROBUS")

nombre = input("Escriba su nombre: ")
while True:

    try:
        saldo = float(
            input("Inserte saldo actual: $")
        )

        # Se revisa que no sea negativo
        if saldo < 0:
            print("El saldo no puede ser negativo")

            # Regresa a pedir el saldo
            continue

        # break termina el ciclo porque el saldo es válido
        break

    except ValueError:
        # Si se escriben letras, se controla el error
        print("Escriba un número válido")

datos = hacer_datos(nombre, saldo)

# Se crea una lista vacía para guardar el historial
lista = []

print("Tarjeta creada correctamente")
mostrar(datos)
menu(datos, lista)