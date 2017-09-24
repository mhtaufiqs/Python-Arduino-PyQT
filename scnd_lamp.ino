int ledPin2 = 4;
int ledPin3 = 3;
int ldrPin = A0;
int sensorValue = 0;
void setup() {
Serial.begin(9600);
pinMode(ledPin2, OUTPUT);
pinMode(ledPin3, OUTPUT);
pinMode(ldrPin, INPUT);
}
void loop() {
int ldrStatus = analogRead(ldrPin);
if (ldrStatus <=100) {
digitalWrite(ledPin2, HIGH);
digitalWrite(ledPin3, LOW);
Serial.println("LDR is DARK");
}
else {
digitalWrite(ledPin2, LOW);
digitalWrite(ledPin3, HIGH);
Serial.println("LDR is BRIGHT");
}
}

