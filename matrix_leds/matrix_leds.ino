//First search and install MD_MAX72XX

#include <MD_MAX72xx.h>
#include "steam_blocks.h"

#define MAX_DEVICES 1
#define CLK_PIN   D9
#define DATA_PIN  D11
#define CS_PIN    D10

MD_MAX72XX mx = MD_MAX72XX(MD_MAX72XX::PAROLA_HW, DATA_PIN, CLK_PIN, CS_PIN, MAX_DEVICES);

void setup() {
   mx.begin();
}

void loop() {
    for (int x=0;x<8;x++) {
        for (int y=0;y<8;y++) {
            mx.setPoint(y, x, 1);
            delay(1000);
            mx.setPoint(y, x, 0);
        }
    }
}
