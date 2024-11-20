import serial
import threading

# Determine the address and data transfer speed
port = '/dev/ttyACM0'
baudrate = 115200

# Open connection
try:
    stm32 = serial.Serial(port, baudrate, timeout=1)
    print(f"Connected to {port} at {baudrate} baud.")
except Exception as e:
    print(f"Failed to connect: {e}")
    exit()

# Read message
try:
    while True:
        data = stm32.read(2)
        if len(data) == 2:  # Check if there is data in buffer
            value = int.from_bytes(data, byteorder='little', signed=True)
            print(f"Received: {value}")  # Print value
except KeyboardInterrupt:
    print("Exiting...")
finally:
    stm32.close()
    