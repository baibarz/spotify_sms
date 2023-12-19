import serial
import time

# Configure serial port for GSM modem
#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser = serial.Serial('COM2', 9600, timeout=1)

def send_at_command(command, delay=0.5):
    try:
        ser.write((command+'\r\n').encode())
        time.sleep(delay)
        response = ser.readlines()
        print(f"Command: {command}, Response: {response}")  # Logging the command and response
        return response
    except serial.SerialException as e:
        print(f"Serial exception: {e}")
        return None

def init_modem():
    if send_at_command('AT') != None:  # Check modem connection
        print("Modem connected successfully.")
        send_at_command('AT+CMGF=1')  # Set SMS text mode
        send_at_command('AT+CMGD=1,4')  # Delete all messages
    else:
        print("Failed to connect to the modem.")

def delete_sms(index):
    send_at_command(f'AT+CMGD={index}')

def send_sms_response(message, recipient_number):
    send_at_command('AT+CMGS="' + recipient_number + '"')
    ser.write(message.encode() + b"\r")
    ser.write(bytes([26]))  # ASCII code for CTRL+Z
