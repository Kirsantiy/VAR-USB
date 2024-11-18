import serial

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
        if stm32.in_waiting > 0:  # Check if there is data in buffer
            data = stm32.readline().decode().strip()  # Read the string
            print(f"Received: {data}")  # Print data
except KeyboardInterrupt:
    print("Exiting...")
finally:
    stm32.close()