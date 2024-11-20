import serial
import threading

# Function for data reception from one STM32
def read_from_stm32(port, baudrate):
    try:
        # Open connection
        stm32 = serial.Serial(port, baudrate, timeout=1)
        print(f"Connected to {port} at {baudrate} baud.")
    except Exception as e:
        print(f"Failed to connect to {port}: {e}")
        return

    try:
        # Data reading
        while True:
            data = stm32.read(2)  # Read 2 bytes
            if len(data) == 2:
                value = int.from_bytes(data, byteorder='little', signed=True)
                print(f"Received from {port}: {value}\n")
    except KeyboardInterrupt:
        print(f"Exiting {port}...")
    finally:
        stm32.close()
        print(f"Connection to {port} closed.")

# Ports settings
ports = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2', '/dev/ttyACM3']
baudrate = 115200

# threads list
threads = []

# Create and start a thread for each STM32
for port in ports:
    thread = threading.Thread(target=read_from_stm32, args=(port, baudrate))
    thread.start()
    threads.append(thread)

# waiting for the end
try:
    for thread in threads:
        thread.join()
except KeyboardInterrupt:
    print("Main program exiting...")
    