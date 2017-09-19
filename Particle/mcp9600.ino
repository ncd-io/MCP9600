// This #include statement was automatically added by the Particle IDE.
#include "MCP9600.h"

MCP9600 tempSens;

void setup() {
    tempSens.address = tempSens.discover();
    tempSens.init();
    Particle.variable("temp", tempSens.temp);
}

int last_checked = 0;
void loop() {
    int now = millis();
    if(now-last_checked > 1000){
        last_checked = now;
        tempSens.readTemp();
    }
}
