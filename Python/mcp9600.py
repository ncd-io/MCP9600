# Thermocouble Sensor configuration register
MCP9600_SENSOR_CONFIG = 0x05
 
MCP9600_TYPE_K = 0x00
MCP9600_TYPE_J = 0x10
MCP9600_TYPE_T = 0x20
MCP9600_TYPE_N = 0x30
MCP9600_TYPE_S = 0x40
MCP9600_TYPE_E = 0x50
MCP9600_TYPE_B = 0x60
MCP9600_TYPE_R = 0x70
 
MCP9600_FILTER_0 = 0x00
MCP9600_FILTER_1 = 0x01
MCP9600_FILTER_2 = 0x02
MCP9600_FILTER_3 = 0x03
MCP9600_FILTER_4 = 0x04
MCP9600_FILTER_5 = 0x05
MCP9600_FILTER_6 = 0x06
MCP9600_FILTER_7 = 0x07

# Device configuration register
MCP9600_DEVICE_CONFIG = 0x06

MCP9600_SENSOR_RESOLUTION_0625 = 0x00
MCP9600_SENSOR_RESOLUTION_25 = 0x80

MCP9600_ADC_RESOLUTION_18 = 0x00
MCP9600_ADC_RESOLUTION_16 = 0x20
MCP9600_ADC_RESOLUTION_14 = 0x40
MCP9600_ADC_RESOLUTION_12 = 0x60

MCP9600_SAMPLES_1 = 0x00
MCP9600_SAMPLES_2 = 0x04
MCP9600_SAMPLES_4 = 0x08
MCP9600_SAMPLES_8 = 0x0C
MCP9600_SAMPLES_16 = 0x10
MCP9600_SAMPLES_32 = 0x14
MCP9600_SAMPLES_64 = 0x18
MCP9600_SAMPLES_128 = 0x1C

MCP9600_NORMAL = 0x00
MCP9600_SHUTDOWN = 0x01
MCP9600_BURST = 0x02

# Status register
MCP9600_STATUS = 0x04

MCP9600_BURST_COMPLETE = 0x80
MCP9600_TEMP_UPDATED = 0x40
MCP9600_INPUT_RANGE_EXCEEDED = 0x20

# Read registers
MCP9600_HOT_JUNCTION = 0x00
MCP9600_JUNCTIONS_DELTA = 0x01
MCP9600_COLD_JUNCTION = 0x02

# Scales
TEMP_CELSIUS = 0x00
TEMP_FAHRENHEIT = 0x01
TEMP_KELVIN = 0x02

class MCP9600():
    def __init__(self, smbus, kwargs = {}):
        self.__dict__.update(kwargs)
        if not hasattr(self, 'address'):
            self.address = discover_address(smbus)
        if not hasattr(self, 'sensor_type'):
            self.sensor_type = MCP9600_TYPE_K
        if not hasattr(self, 'filter'):
            self.filter = MCP9600_FILTER_0
        if not hasattr(self, 'scale'):
            self.scale = TEMP_CELSIUS
        if not hasattr(self, 'sensor_resolution'):
            self.sensor_resolution = MCP9600_SENSOR_RESOLUTION_0625
        if not hasattr(self, 'adc_resolution'):
            self.adc_resolution = MCP9600_ADC_RESOLUTION_14
        if not hasattr(self, 'samples'):
            self.samples = MCP9600_SAMPLES_1
        if not hasattr(self, 'mode'):
            self.mode = MCP9600_NORMAL
        if not hasattr(self, 'read_register'):
            self.read_register = MCP9600_HOT_JUNCTION
        self.smbus = smbus
        
    def take_readings(self):
        if(self.smbus.read_byte_data(self.address, (MCP9600_STATUS) & MCP9600_TEMP_UPDATED) == 0):
            return 'something'
        data = self.smbus.read_i2c_block_data(self.address, self.read_register, 2)
        temperature = (((data[0] & 0x7F) * 16) + (float(data[1]) / 16))
        if data[0] & 0x80:
            temperature = 1024 - temperature
        temperature = self.convert_temperature(temperature)
        return temperature
        
    def convert_temperature(self, temperature):
        if self.scale == TEMP_FAHRENHEIT:
            return (float(temperature) *1.8)+32
        elif self.scale == TEMP_KELVIN:
            return temperature + 273.15;
        return temperature
    
def discover_address(bus):
    for address in range(96, 104):
        try:
            if(bus.read_byte_data(address, 0x00)):
                return address
        except:
            continue
