#include "steam_blocks.h"

#define GREEN D9
#define YELLOW D10
#define RED D11

void setup() {
  pinMode(GREEN, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(RED, OUTPUT);
  digitalWrite(GREEN, LOW);
  digitalWrite(YELLOW, LOW);
  digitalWrite(RED, LOW);
}

void loop() {
  digitalWrite(GREEN, HIGH);
  delay(3000);
  digitalWrite(GREEN, LOW);
  for (int i=0;i<3;i++) {
    digitalWrite(YELLOW, HIGH);
    delay(500);
    digitalWrite(YELLOW, LOW);
    delay(500);
  }
  digitalWrite(RED, HIGH);
  delay(3000);
  digitalWrite(RED, LOW);  
}
