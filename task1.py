import socket

def port_scanner(host, start_port, end_port):
    print(f"Сканируем хост: {host} от порта {start_port} до {end_port}")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Тайм-аут на подключение
        try:
            sock.connect((host, port))
        except (socket.timeout, socket.error):
            print(f"Порт {port} закрыт")
        else:
            print(f"Порт {port} открыт")
        finally:
            sock.close()

if __name__ == "__main__":
    target_host = input("Введите хост для сканирования (например, 127.0.0.1): ")
    start = int(input("Введите начальный порт: "))
    end = int(input("Введите конечный порт: "))
    port_scanner(target_host, start, end)
