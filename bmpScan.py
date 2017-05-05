try:
	import time
	import sys
	from datetime import datetime
	import Adafruit_BMP.BMP085 as BMP180
	sensor = BMP180.BMP085()

	while (True):
		data = open("BMP180.dat", "a")
		data.write("Date: {}\n".format(str(datetime.now())))
		data.write("Temperature: {0:02f} *C\n".format(sensor.read_temperature()))
		data.write("Air pressure: {0:02f} Pa\n".format(sensor.read_pressure()))
		data.write("Height (from sea level): {0:02f} m\n".format(sensor.read_altitude()))
		data.write("-----------------------------------\n")
		data.close()
		print("Saved.")
		time.sleep(30)

except ModuleNotFoundError:
	print("Error importing dependencies.\nMake sure Adafruit's BMP Module is installed, then try again.")
	sys.exit()

except IOError:
	print("Error reading/writing to file.\nPlease try again.")
	sys.exit()

except:
	print("Unknown error occurred.\nPlease try again.")
	sys.exit()
