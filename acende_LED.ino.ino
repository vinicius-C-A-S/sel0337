#include <Wire.h>

// Devine LED e comunicação com a RasPi
const int pino_led = LED_BUILTIN;
const int conversor = A1;

void setup() {
	// Endereço do barramento I2C 
	Wire.begin(0x8);
	//ver se está recebendo dados "event" se estiver está em receive, se não request
	Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
  
  Serial.begin(9600);

	// Controla/define os parametro de liga e desliga do LED
	pinMode(pino_led, OUTPUT);
	digitalWrite(pino_led, LOW);

  pinMode(conversor, INPUT);
}

// Ao receber dados da RasPi começa a enviar a informação de controle pro LED no Arduino 
void receiveEvent(int contagem) { // loop while para receber info da RasPi
	while (Wire.available()) 
	{ 
		char c = Wire.read(); // lê o byte como character c
		digitalWrite(pino_led, c);
	}
}

void requestEvent()
{
  int valor_conv = analogRead(conversor);
  Wire.write(highByte(valor_conv));
  Wire.write(lowByte(valor_conv));
  Serial.println(valor_conv);
}

void loop() 
{
	delay(200);
}
