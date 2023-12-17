# sms_handler.py

import serial
import time

# Configure serial port for GSM modem
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def send_at_command(command, delay=0.5):
    ser.write((command+'\r\n').encode())
    time.sleep(delay)
    response = ser.readlines()
    return response

def init_modem():
    send_at_command('AT')  # Check modem connection
    send_at_command('AT+CMGF=1')  # Set SMS text mode
    send_at_command('AT+CMGD=1,4')  # Delete all messages

def delete_sms(index):
    send_at_command(f'AT+CMGD={index}')
