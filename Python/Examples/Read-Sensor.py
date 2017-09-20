#import smbus for i2c communications
import smbus
import time
#import the chip library
import mcp9600

# Get I2C bus, this is I2C Bus 1
bus = smbus.SMBus(1)
#kwargs is a Python set that contains the address of your device as well as desired range and bandwidth
#since this device uses a somewhat imprecise way of defining an address we built a a function you can call before
#    object instantiation to find the address of the device. This function is only accurate when there are no other
#    I2C devices on the bus (there can be, but they can't have an address between 96 and 104. 0x60 through 0x68 for hex heads)
#refer to the chip's datasheet to determine what value you need for the kwargs to suit your project
#the address can be set statically by simply setting kwargs['address'] to the board's address. discover_address() is just for convenience.
#the kwargs below is set with all of the default values
kwargs = {'address': mcp9600.discover_address(bus), 'sensor_type': 0x00, 'filter': 0x00, 'scale': 0x00, 'sensor_resolution': 0x00, 'adc_resolution': 0x40, 'samples': 0x00, 'mode': 0x00, 'read_register': 0x00}
#create the MCP9600 object from the MCP9600 library and pass it the kwargs and com bus.
#the object requires that you pass it the bus object so that it can communicate and share the bus with other chips/boards if necessary
mcp9600 = mcp9600.MCP9600(bus, kwargs)
while True:
     #print out the readings.
     #the readings will be return as a float in whatever scale/unit of measurement you initialized the board with in kwargs.
     #Scaling/Unit of measurement will be Celsius unless set as something else in kwargs before intialization.
    print mcp9600.take_readings()
    #this sleep is not required
    time.sleep(.25)
