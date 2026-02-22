import socket
import threading

open_ports = []

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    except:
        pass

def main():
    target = input("Enter target IP: ")
    print(f"Scanning target: {target}")

    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nScan complete.")
    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"- {port}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
