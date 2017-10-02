# About

This Library is intended for use with any MCP9600 board board available from ncd.io

### Developer information
NCD has been designing and manufacturing computer control products since 1995.  We have specialized in hardware design and manufacturing of Relay controllers for 20 years.  We pride ourselves as being the industry leader of computer control relay products.  Our products are proven reliable and we are very excited to support Particle.  For more information on NCD please visit ncd.io

### Requirements
- The Python SMBus Module: https://pypi.python.org/pypi/smbus-cffi/
- An I2C connection to an MCP9600 board
- Knowledge base for developing and programming with Python.

### Version
1.0.0

### How to use this library

The libary must be imported into your application and an I2C bus must be created with the SMBus module.

Once the library is imported and the I2C Bus created you can create a BMP280 object, pass it the I2C Bus and start to communicate to the chip.  You can optionally pass in a kwarg to the object that contains many configuration options such as filter, scale, sensor_resolution, samples, and many others.

The default values for these configuration option are:
{'address': mcp9600.discover_address(bus), 'sensor_type': 0x00, 'filter': 0x00, 'scale': 0x00, 'sensor_resolution': 0x00, 'adc_resolution': 0x40, 'samples': 0x00, 'mode': 0x00, 'read_register': 0x00}

### Publicly accessible methods
```cpp
get_readings()
```
>This function returns the readings of the sensor in a simple float variable. The configuration options passed in kwargs will
>have a huge effect on these readings and we recommend looking over the datasheet and the example software to get a beter idea.
