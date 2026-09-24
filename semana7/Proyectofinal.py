# SISTEMA DE TARJETA QROBUS
# Precio de un viaje
costo = 11.00
# Máximo de viajes que se pueden hacer
# cuando no hay saldo
limite = 2

# PARTE 1 - DATOS DEL USUARIO
# Temas 1, 2, 3, 4, 11 y 12
def hacer_datos(nombre, saldo):

    datos = {
        "nombre": nombre,
        "saldo": saldo,
        "deuda": 0,
        "viajes": 0
    }
    return datos
def mostrar(datos):
    print("QROBUS")
    print(f"Nombre: {datos['nombre']}")
    print(f"Saldo: ${datos['saldo']:.2f}")
    print(f"Deuda: ${datos['deuda']:.2f}")
    print(f"Viajes a crédito: {datos['viajes']}")
# PARTE 2 - COBRAR VIAJE
# Temas 5, 6, 8 y 9
def cobrar(datos, lista):
    print("COBRO")

    if datos["saldo"] >= costo:
        datos["saldo"] = datos["saldo"] - costo
        print("Viaje aceptado.")
        print(f"Se cobraron ${costo:.2f}")
        print(f"Saldo restante: ${datos['saldo']:.2f}")
        lista.append("Viaje pagado")
    else:
        # Si no hay saldo, revisamos las oportunidades
        if datos["viajes"] < limite:
            datos["deuda"] = datos["deuda"] + costo
            datos["viajes"] = datos["viajes"] + 1
            print("Saldo insuficiente, pero el viaje fue aceptado.")
            print(f"Deuda: ${datos['deuda']:.2f}")
            print(
                f"Oportunidades restantes: "
                f"{limite - datos['viajes']}"
            )
            lista.append("Viaje a crédito")
        else:
            print("Tarjeta bloqueada.")
            print("Ya utilizó sus 2 oportunidades.")
            print(
                f"Debe pagar su deuda de "
                f"${datos['deuda']:.2f}"
            )
            lista.append("Viaje rechazado")
# PARTE 3 - RECARGA
# Temas 5, 6 y 15
def recargar(datos, lista):

    print("RECARGA")
    try:
        recarga = float(
            input("Ingrese cantidad a recargar: $")
        )
    except ValueError:
        print("Escriba un número válido.")
        return
    if recarga <= 0:
        print("La recarga debe ser mayor a 0.")
        return
    # Si hay deuda
    if datos["deuda"] > 0:
        # La recarga alcanza para pagarla
        if recarga >= datos["deuda"]:
            recarga = recarga - datos["deuda"]
            datos["deuda"] = 0
            datos["viajes"] = 0

            # Lo que sobra se convierte en saldo
            datos["saldo"] = datos["saldo"] + recarga
            print("Se pagó el adeudo.")
            print("La tarjeta ha sido desbloqueada.")
            print(
                f"Saldo disponible: ${datos['saldo']:.2f}"
            )
            lista.append("Se pagó la deuda")
        else:
            # La recarga no alcanza
            datos["deuda"] = datos["deuda"] - recarga
            print("La recarga no fue suficiente.")
            print(
                f"Deuda restante: ${datos['deuda']:.2f}"
            )

            lista.append("Abono a la deuda")
    else:
        # Si no hay deuda, todo se suma al saldo
        datos["saldo"] = datos["saldo"] + recarga

        print("Recarga realizada correctamente.")
        print(
            f"Nuevo saldo: ${datos['saldo']:.2f}"
        )
        lista.append("Recarga normal")


# PARTE 4 - HISTORIAL
# Tema 9 y Tema 8
def ver_historial(lista):

    print("HISTORIAL")
    if len(lista) == 0:
        print("No hay operaciones.")
    else:
        for i in range(len(lista)):
            print(f"{i + 1}. {lista[i]}")

# PARTE 5 - GUARDAR HISTORIAL
# Temas 17, 18, 19 y 20
def guardar(lista):
    try:
        # "a" = agregar información
        with open(
            "historial_qrobus.txt",
            "a",
            encoding="utf-8"
        ) as archivo:
            for dato in lista:

                archivo.write(dato + "\n")
        print("Historial guardado.")
    except PermissionError:
        print("No se pudo guardar el archivo.")
def leer():
    try:
        with open(
            "historial_qrobus.txt",
            "r",
            encoding="utf-8"
        ) as archivo:
            texto = archivo.read()
        print("HISTORIAL GUARDADO")
        if texto == "":
            print("El archivo está vacío.")
        else:
            print(texto)
    except FileNotFoundError:
        print("Todavía no existe el archivo.")
    except PermissionError:
        print("No se pudo leer el archivo.")

# PARTE 6 - MENÚ
# Temas 5, 6 y 8
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
            print("Gracias por utilizar Qrobus.")
            break
        else:
            print("Opción no válida.")
# PARTE 7 - INICIO DEL PROGRAMA
# Temas 1, 2, 3 y 4

print("SISTEMA QROBUS")
nombre = input("Escriba su nombre: ")
try:
    saldo = float(
        input("Inserte saldo actual: $")
    )
except ValueError:
    print("Saldo inválido.")
    saldo = 0
# Crear los datos de la tarjeta
datos = hacer_datos(nombre, saldo)
# Lista para guardar operaciones
lista = []
print("Tarjeta creada correctamente.")
mostrar(datos)
# Iniciar el sistema
menu(datos, lista)

