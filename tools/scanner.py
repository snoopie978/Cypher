import socket
from concurrent.futures import ThreadPoolExecutor


tool_name = "scanner"


def scan_port(ip, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        sock.close()

        if result == 0:
            return port

    except:
        pass


    return None



def scanner():

    print("")
    print("====================================")
    print("       CYPHER NETWORK SCANNER")
    print("====================================")


    ip = input("Target IP: ")

    start_port = int(input("Starting port: "))
    end_port = int(input("Ending port: "))


    print("")
    print("Scanning...")
    print("")


    open_ports = []


    with ThreadPoolExecutor(max_workers=100) as executor:

        ports = range(start_port, end_port + 1)

        results = executor.map(
            lambda port: scan_port(ip, port),
            ports
        )


        for port in results:

            if port:
                open_ports.append(port)
                print(f"[OPEN] {port}")


    print("")
    print("Scan Complete")

    print("Open Ports:", open_ports)

    print("====================================")



def run():
    scanner()