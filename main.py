import socket
import pyfiglet
import sys
import time

pyfiglet.print_figlet('PortScan.py')

def loading_animation(duration=5):
    chars = ["-", "\\", "|", "/"]
    end_time = time.time() + duration 
    while time.time() < end_time:
        for char in chars:
            if time.time() >= end_time:
                break
            sys.stdout.write('\r' + "Carregando " + char + " ")
            sys.stdout.flush()
            time.sleep(1)

loading_animation()

def get_ip_info(ip, port):
    print(f'Conectando ao IP: {ip}, na porta {port}...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    try:
        s.connect((ip, port))
        print(f'Porta {port} aberta em {ip}')
    except:
        print(f'Porta {port} fechada ou incacessível {ip}')
    finally:
        s.close()

get_ip_info(
    ip = input("Digite o IP: "),
    port = int(input("Digite a PORT: "))
)
