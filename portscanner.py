import socket

def portscan(ip, start_port=1, end_port=1024, timeout=0.1):
    """
    Scans a range of ports on a given IP address.

    Args:
        ip (str): The IP address to scan.
        start_port (int): The starting port number for the scan. Defaults to 1.
        end_port (int): The ending port number for the scan. Defaults to 1024.
        timeout (float): The timeout in seconds for each connection attempt. Defaults to 0.1.

    Returns:
        None
    """
    print(f'\nStarting a scan on {ip}\n')
    open_ports = []
    for port in range(start_port, end_port+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            result = s.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
                print(f'Port {port} is open')
            else:
                print(f'Port {port} is closed or filtered')
        except socket.error as e:
            print(f'Error connecting to port {port}: {e}')
        finally:
            s.close()
    print(f'\nScan complete. {len(open_ports)} port(s) are open.')

# Call the function with the user's IP address and desired port range
portscan("your ip address", start_port=1, end_port=65535)
