import threading
from servpy import Server


def main():
    rdp = Server()
    # print(f'Running.... {threading.current_thread()}')
    rdp.run(verbose=False)


def threads(thread: int):
    thread_list = []
    for _ in range(thread):
        t = threading.Thread(target=main)
        thread_list.append(t)
        t.start()

    for thread_ in thread_list:
        thread_.join()


if __name__ == '__main__':
    threads(100)
