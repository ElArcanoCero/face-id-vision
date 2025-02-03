int ledPins[] = {2, 3, 4, 5}; // Pines de los 4 LEDs
int currentLed = 0; // LED actual que está encendido
int ledOnTime = 20000; // Tiempo que el LED se mantiene encendido en milisegundos

int ledPin = 9; // Pin de la cinta LED
int brightness = 0; // Variable para almacenar el brillo actual
int fadeAmount = 5; // Cantidad de incremento o decremento del brillo
int interval = 200; // Intervalo de tiempo para cambiar el brillo (en milisegundos)
int contador = 0; //

unsigned long previousMillis = 0; // Variable para almacenar el tiempo anterior (en milisegundos)
unsigned long currentMillis = 0; // Variable para almacenar el tiempo actual (en milisegundos)

void setup() {
  Serial.begin(9600);
  
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT); // Configura los pines de los LEDs como salidas digitales
    digitalWrite(ledPins[i], LOW); // Apaga todos los LEDs
  }
  pinMode(ledPin, OUTPUT); // Configura el pin de la cinta LED como salida digital
  analogWrite(ledPin, brightness); // Establece el brillo inicial en 0
}

void loop() {
  if (Serial.available() > 0) {

    int c = Serial.read();
    Serial.print(c);
    if (c == '1') {
      
      // Enciende el LED actual y la cinta LED al mismo tiempo
      digitalWrite(ledPins[currentLed], HIGH); // Enciende el LED actual
      contador++;
      previousMillis = millis(); // Almacena el tiempo actual en la variable previousMillis
      while (1) { // Repite mientras el LED esté encendido
        currentMillis = millis();
        analogWrite(ledPin, brightness); // Establece el brillo actual en la cinta LED
        brightness = brightness + fadeAmount; // Incrementa o decrementa el brillo actual
        if (brightness <= 0 || brightness >= 255) { // Si el brillo alcanza los límites
          fadeAmount = -fadeAmount; // Cambia la dirección de incremento/decremento del brillo
        }
        delay(interval); // Espera el intervalo de tiempo antes de cambiar el brillo
        if (Serial.available() > 0){
        break;
        }
        if (c =='0') {
        break;
      
      }
      }
      digitalWrite(ledPins[currentLed], LOW); // Apaga el LED actual
      analogWrite(ledPin, 0); // Apaga la cinta LED
      currentLed = (currentLed + 1) % 4; // Avanza al siguiente LED circularmente
      delay(200); // Espera un breve momento antes de encender el siguiente LED
      contador++;
      
      
    }
  }
}