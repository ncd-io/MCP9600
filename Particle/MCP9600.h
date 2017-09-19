
#include "spark_wiring_i2c.h"
#include "spark_wiring.h"


//Thermocouble Sensor configuration register
#define MCP9600_SENSOR_CONFIG 0x05

#define MCP9600_TYPE_K 0x00
#define MCP9600_TYPE_J 0x10
#define MCP9600_TYPE_T 0x20
#define MCP9600_TYPE_N 0x30
#define MCP9600_TYPE_S 0x40
#define MCP9600_TYPE_E 0x50
#define MCP9600_TYPE_B 0x60
#define MCP9600_TYPE_R 0x70

#define MCP9600_FILTER_0 0x00
#define MCP9600_FILTER_1 0x01
#define MCP9600_FILTER_2 0x02
#define MCP9600_FILTER_3 0x03
#define MCP9600_FILTER_4 0x04
#define MCP9600_FILTER_5 0x05
#define MCP9600_FILTER_6 0x06
#define MCP9600_FILTER_7 0x07

//Device configuration register
#define MCP9600_DEVICE_CONFIG 0x06

#define MCP9600_SENSOR_RESOLUTION_0625 0x00
#define MCP9600_SENSOR_RESOLUTION_25 0x80

#define MCP9600_ADC_RESOLUTION_18 0x00
#define MCP9600_ADC_RESOLUTION_16 0x20
#define MCP9600_ADC_RESOLUTION_14 0x40
#define MCP9600_ADC_RESOLUTION_12 0x60

#define MCP9600_SAMPLES_1 0x00
#define MCP9600_SAMPLES_2 0x04
#define MCP9600_SAMPLES_4 0x08
#define MCP9600_SAMPLES_8 0x0C
#define MCP9600_SAMPLES_16 0x10
#define MCP9600_SAMPLES_32 0x14
#define MCP9600_SAMPLES_64 0x18
#define MCP9600_SAMPLES_128 0x1C

#define MCP9600_NORMAL 0x00
#define MCP9600_SHUTDOWN 0x01
#define MCP9600_BURST 0x02

//Status register
#define MCP9600_STATUS 0x04

#define MCP9600_BURST_COMPLETE 0x80
#define MCP9600_TEMP_UPDATED 0x40
#define MCP9600_INPUT_RANGE_EXCEEDED 0x20

//Read registers
#define MCP9600_HOT_JUNCTION 0x00
#define MCP9600_JUNCTIONS_DELTA 0x01
#define MCP9600_COLD_JUNCTION 0x02

//Scales
#define TEMP_CELSIUS 0x00
#define TEMP_FAHRENHEIT 0x01
#define TEMP_KELVIN 0x02

/*
 * Alert registers and statuses have been omitted for brevity
 */

class MCP9600{
public:
    int discover();

    int address = 0x64;
    void init();
    int scale = TEMP_FAHRENHEIT;
    
    double readTemp();
    double temp;
    
    int sensor = MCP9600_TYPE_K;
    int filter = MCP9600_FILTER_0;
    
    int sensor_resolution = MCP9600_SENSOR_RESOLUTION_0625;
    int adc_resolution = MCP9600_ADC_RESOLUTION_14;
    int samples = MCP9600_SAMPLES_1;
    int mode = MCP9600_NORMAL;
    
    int read_register = MCP9600_HOT_JUNCTION;
private:
    void begin();
    int readByte(int reg);
    void readBuffer(int reg, int *buff, int len);
    void writeByte(int reg, int data);
};
