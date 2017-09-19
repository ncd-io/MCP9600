#include "MCP9600.h"


void MCP9600::init(){
    begin();
    writeByte(MCP9600_SENSOR_CONFIG, sensor | filter);
    writeByte(MCP9600_DEVICE_CONFIG, sensor_resolution | adc_resolution | samples | mode);
}

double MCP9600::readTemp(){
    if(readByte(MCP9600_STATUS) & MCP9600_TEMP_UPDATED == 0){
        return temp;
    }
    
    int data[2];
    readBuffer(read_register, data, 2);
    
    temp = (((data[0] & 0x7F) * 16) + (data[1] / 16));
    
    if(data[0] & 0x80) temp = 1024 - temp;
    
    if(scale == TEMP_FAHRENHEIT) temp = (temp *1.8)+32;
    if(scale == TEMP_KELVIN) temp += 273.15;
    
    return temp;
}

//I2C Utility functions

void MCP9600::begin(){
    if ( !Wire.isEnabled() ) {
        Wire.begin();
    }
}

int MCP9600::discover(){
    begin();
    for(int i = 96; i < 104; i++){
        Wire.beginTransmission(i);
        if(Wire.endTransmission() == 0){
            address = i;
            return i;
        }
    }
    return 256;
}

void MCP9600::writeByte(int reg, int data){
    Wire.beginTransmission(address);
    Wire.write(reg);
    if(data < 256) Wire.write(data);
    Wire.endTransmission();
}

int MCP9600::readByte(int reg){
    writeByte(reg, 256);
    Wire.requestFrom(address, 1);
    return Wire.read();
}

void MCP9600::readBuffer(int reg, int *buff, int len){
    writeByte(reg, 256);
    Wire.requestFrom(address, len);
    for(int i=0;i<len;i++){
        buff[i] = Wire.read();
    }
}
