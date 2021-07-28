import socket
import threading
from queue import Queue

target = "192.168.1.1"


def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except socket.error:
        return False


def fill_queue(port_list):
    new_queue = Queue()
    for port in port_list:
        new_queue.put(port)
    return new_queue


def worker():
    while not queue.empty():
        test_port = queue.get()

        if port_scan(test_port):
            open_ports.append(test_port)


if __name__ == '__main__':
    queue = fill_queue(range(1,100))
    open_ports = []

    thread_list = []
    for i in range(500):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    print("Open threads are: ", open_ports)



