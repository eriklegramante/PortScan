from database import PORT_SERVICES

def display_port_services():
    print("Available Port Services:")
    print("-------------------------")
    for port, service in PORT_SERVICES.items():
        print(f"Port {port}: {service}")


display_port_services()