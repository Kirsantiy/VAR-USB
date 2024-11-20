import serial
import threading
import time

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
                print(f"Received from {port}: {value}")
    except KeyboardInterrupt:
        print(f"Exiting {port}...")
    finally:
        stm32.close()
        print(f"Connection to {port} closed.")


def send_to_stm32(port, baudrate, value):
    try:
        # Open connection
        stm32 = serial.Serial(port, baudrate, timeout=1)
        print(f"Connected to {port} for sending at {baudrate} baud.")
    except Exception as e:
        print(f"Failed to connect to {port} for sending: {e}")
        return

    try:
        # Sending data repeatedly
        while True:
            data = value.to_bytes(2, byteorder='little', signed=True)
            stm32.write(data)
            print(f"Sent to {port}: {value}")
            time.sleep(1)  # Adjust delay as needed
    except KeyboardInterrupt:
        print(f"Exiting sending to {port}...")
    finally:
        stm32.close()
        print(f"Sending connection to {port} closed.")

# Ports settings
ports = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2', '/dev/ttyACM3']
baudrate = 115200

# Values to send to each STM32
values_to_send = [4000, 5000, 6000, 7000]

# Threads for reading
read_threads = []

# Threads for sending
send_threads = []

# Create and start threads for reading and sending
for i, port in enumerate(ports):
    # Start reading thread
    read_thread = threading.Thread(target=read_from_stm32, args=(port, baudrate))
    read_thread.start()
    read_threads.append(read_thread)

    # Start sending thread
    send_thread = threading.Thread(target=send_to_stm32, args=(port, baudrate, values_to_send[i]))
    send_thread.start()
    send_threads.append(send_thread)

# Wait for all threads to complete
try:
    for thread in read_threads + send_threads:
        thread.join()
except KeyboardInterrupt:
    print("Main program exiting...")