import serial
import binascii


class OBD2():
	def __init__(self, device, baud_rate=115200):
		self.ser = serial.Serial(device, baud_rate, timeout=1)

	def convert_data(self, data):
		return data.splitlines()[-3:-2][0].rstrip()

	def send_command(self, command):
		self.ser.write(command + ' \r')

	def retrieve_response(self):
		return self.convert_data(self.ser.readline())

selected_device = False
while True:
	if not selected_device:
		device = raw_input('Enter device: ')
		baud_rate = raw_input('Enter baud rate: ')
		obd2 = OBD2(device, baud_rate)

		selected_device = True

	command = raw_input('>>> ')
	obd2.send_command(command)

	print obd2.retrieve_response()
