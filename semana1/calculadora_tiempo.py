nombre = input("Bienvenido a tu calculadora de tiempo, por favor, ingresa tu nombre: ")

rs = float(input("¿Cuántas horas dedicas diariamente a redes sociales? "))
ms = float(input("¿Cuántas horas dedicas diariamente a mensajería? "))
sm = float(input("¿Cuántas horas dedicas diariamente a servicios de streaming? "))
vjs = float(input("¿Cuántas horas dedicas diariamente a los videojuegos? "))
el = float(input("¿Cuántas horas dedicas diariamente al estudio en línea? "))

tiempo_total = rs + ms + sm + vjs + el

porcentaje = (tiempo_total / 24) * 100

print(f"Hola! {nombre}, tu tiempo total es de {tiempo_total} horas y tu porcentaje calculado es de {porcentaje}%")

