import serial

ser = serial.Serial('COM4', 9600) # Cambia el puerto COM y la velocidad de comunicación según corresponda

while True:
    # Lee la entrada del usuario desde la consola
    user_input = input("Introduce 'A' para encender el LED, 'B' para apagarlo o 'C' para realizar otra acción: ")

    # Envía el byte correspondiente al puerto serial
    if user_input.upper() in ['A', 'B', 'C']:
        ser.write(user_input.upper().encode())
    else:
        print("Entrada inválida. Introduce 'A', 'B' o 'C'.")