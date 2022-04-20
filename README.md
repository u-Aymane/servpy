# ServPy

ServPy is a Python library that allows you to bruteforce and find (ssh, ftp, windows) server in the internet by checking open ports

## Installation
Install Nmap

https://nmap.org/download.html

Use the package manager [pip](https://pypi.org/project/servpy/) to install servpy.

```bash
pip install servpy
```

## Usage

```python
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

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)