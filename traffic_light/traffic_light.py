from arduino import *

GREEN=D9
YELLOW=D10
RED=D11

pinMode(GREEN, OUTPUT)
pinMode(YELLOW, OUTPUT)
pinMode(RED, OUTPUT)
digitalWrite(GREEN, LOW)
digitalWrite(YELLOW, LOW)
digitalWrite(RED, LOW)

while True:
    digitalWrite(GREEN, HIGH);
    delay(3000);
    digitalWrite(GREEN, LOW);
    for i in range(3):
        digitalWrite(YELLOW, HIGH);
        delay(500);
        digitalWrite(YELLOW, LOW);
        delay(500);

    digitalWrite(RED, HIGH);
    delay(3000);
    digitalWrite(RED, LOW); 