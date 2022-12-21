from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) # /dev/ic2-1
flag = True

print ("Digite 1 para ON ou 0 para OFF")

while flag:
	ledstate = input(">>>> ")
	if ledstate == "1":
		bus.write_byte(addr, 0x1)
	elif ledstate == "0":
		bus.write_byte(addr, 0x0)
	elif ledstate == "adc":
		data = bus.read_i2c_block_data(addr, 0, 2)
		print(f"{data[0] * 256 + data[1]}")
	else:
		flag = False
