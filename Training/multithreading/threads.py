import threading


def first():
    for i in range(50):
        print("djes to")


def second():
    for i in range(50):
        print("eo")


t1 = threading.Thread(target=first)
t1.start()

t2 = threading.Thread(target=second)
t2.start()