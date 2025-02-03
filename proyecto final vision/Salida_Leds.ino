





// Definir los pines de los LEDs rojos
const int ledPin1R = 2;
const int ledPin2R = 3;
const int ledPin3R = 4;

// Definir los pines de los LEDs verdes
const int ledPin1G = 10;
const int ledPin2G = 11;
const int ledPin3G = 12;

void setup() {
  // Configurar los pines de los LEDs rojos como salida
  pinMode(ledPin1R, OUTPUT);
  pinMode(ledPin2R, OUTPUT);
  pinMode(ledPin3R, OUTPUT);

  // Configurar los pines de los LEDs verdes como salida
  pinMode(ledPin1G, OUTPUT);
  pinMode(ledPin2G, OUTPUT);
  pinMode(ledPin3G, OUTPUT);

  digitalWrite(ledPin1R, HIGH);
  digitalWrite(ledPin2R, HIGH);
  digitalWrite(ledPin3R, HIGH);
  // Iniciar la comunicación serial a 9600 baudios
  Serial.begin(9600);
}

void loop() {

  
  if (Serial.available() > 0) {
    // Leer el primer byte recibido
    char signal = Serial.read();
    
    // Comprobar el valor del byte recibido
    switch (signal) {
      case 'A':
        // Apagar el LED rojo 1 y encender el LED verde 1
        digitalWrite(ledPin1R, LOW);
        digitalWrite(ledPin1G, HIGH);
        delay(2000);
        digitalWrite(ledPin1R, HIGH);
        digitalWrite(ledPin1G, LOW);

        break;
      case 'B':

        digitalWrite(ledPin2R, LOW);
        digitalWrite(ledPin2G, HIGH);
        delay(2000);
        digitalWrite(ledPin2R, HIGH);
        digitalWrite(ledPin2G, LOW);
      
        break;
      case 'C':
        digitalWrite(ledPin3R, LOW);
        digitalWrite(ledPin3G, HIGH);
        delay(2000);
        digitalWrite(ledPin3R, HIGH);
        digitalWrite(ledPin3G, LOW);
        // No realizar cambios en los LEDs rojos y verdes
        break;
    }
  }
}