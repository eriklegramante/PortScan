from database import PORT_SERVICES
from colorama import Fore, Style 

def display_port_services():
    print("Available Port Services:")
    print("-------------------------")
    for port, service in PORT_SERVICES.items():
        print(f"Port {port}: {service}")

def print_port_status(port, status):
    service = PORT_SERVICES.get(port, "Unknown Service")
    if status:
        print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port} - {service}")
    else:
        print(f"{Fore.RED}[CLOSED]{Style.RESET_ALL} Port {port} - {service}")

display_port_services()
