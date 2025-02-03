import serial

ser = serial.Serial('COM3', 9600) # Cambia el puerto COM y la velocidad de comunicación según corresponda

while True:
    # Lee la entrada del usuario desde la consola
    user_input = input("Introduce '1' para encender el LED, o '0' para apagarlo: ")

    # Envía el byte correspondiente al puerto serial
    ser.write(user_input.encode())