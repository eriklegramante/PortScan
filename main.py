import socket
import pyfiglet
import sys
import time
from colorama import Fore, Style
import concurrent.futures

pyfiglet.print_figlet('PortScan.py') 


def loading_animation(duration=3.5): #animação de carregamento
    chars = ["-", "\\", "|", "/"]
    end_time = time.time() + duration 
    while time.time() < end_time:
        for char in chars:
            if time.time() >= end_time:
                break
            sys.stdout.write('\r' + "Loading " + char + " ")
            sys.stdout.flush()
            time.sleep(0.1)

def get_ip_info(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        s.close()
        return port, True
    except:
        s.close()
        return port, False


def separator(): #organizar console
    print("\n" + "-" * 50 + "\n")

while True: 
    try:
        separator()
        choose = int(input("[1] - Specific port\n[2] - Test all ports(6000)\n[3] - Choose ports\n[4] - Exit\nOption: "))
    except ValueError:
        separator()
        print(f"{Fore.RED}It looks like you typed something wrong... have you tried using numbers?{Style.RESET_ALL}")
        continue

    if choose == 1:
        separator()
        ip = input("[IP]: ")
        port = int(input("[PORT]: "))
        _, status = get_ip_info(ip, port)
        separator()
        if status:
            print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port}")
        else:
            print(f"{Fore.RED}[CLOSED]{Style.RESET_ALL} Port {port}")
        
    elif choose == 2:
        separator()
        ip = input("[IP]: ")
        loading_animation(1)
        separator()
        start_time = time.time()

        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(get_ip_info, ip, port) for port in range(1, 6000)]
            for future in concurrent.futures.as_completed(futures):
                port, status = future.result()
                if status:
                    results.append(port)
                    print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port}")
                else:
                    print(f"{Fore.RED}[CLOSED]{Style.RESET_ALL} Port {port}")

        separator()
        print(f"Scan finished in {time.time() - start_time:.2f} seconds.")
        if results:
            print(f"Open ports: {', '.join(map(str, results))}")
        else:
            print("No open ports found.")
    
    elif choose == 3:
        separator()
        ip = input("[IP]: ")
        ports = input("[PORTS] (separated by commas): ")
        ports = [int(p.strip()) for p in ports.split(",")]

        separator()
        for port in ports:
            _, status = get_ip_info(ip, port)
            if status:
                print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port}")
            else:
                print(f"{Fore.RED}[CLOSED]{Style.RESET_ALL} Port {port}")

    elif choose == 4:
        separator()
        print("Exiting...")
        break
#scanme.nmap.org <---- domain test