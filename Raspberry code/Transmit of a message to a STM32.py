import serial

# Determine the address and data transfer speed
port = '/dev/ttyACM0'  
baudrate = 115200

# Connect with STM32
try:
    stm32 = serial.Serial(port, baudrate, timeout=1)
    print(f"Connected to {port} at {baudrate} baud.")
except Exception as e:
    print(f"Failed to connect: {e}")
    exit()

# Data transmit
try:
    message = "4000\n"  # Message to send
    stm32.write(message.encode())  # Encode the string in bytes and send
    print(f"Sent: {message}")
except Exception as e:
    print(f"Error while sending: {e}")
finally:
    stm32.close()