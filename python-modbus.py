from pymodbus.client import ModbusTcpClient
import keyboard 
import time 

server_ip = "192.168.3.5"
server_port = 502

client = ModbusTcpClient(server_ip, server_port)

client.connect()

unit_id = 1  
address = 301
count = 2  

while True:
    if keyboard.is_pressed("q"): 
        break
    
    result = client.read_holding_registers(address, count, unit=unit_id)

    if result.isError():
        print("Hata:", result)
    else:
        print("Okunan Veri:", result.registers)
    
    time.sleep(0.5)

client.close()
