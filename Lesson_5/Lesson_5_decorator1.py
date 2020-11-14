from threading import Thread
from urllib.request import urlopen


def arg_thread_decor(name_, daemon_=True):

    def thread_decor(func):
        #print(name_, daemon_)

        def wrapper(*args):
            thread_ = Thread(target=func, args=args, name=name_, daemon=daemon_)
            name = thread_.getName()
            thread_.start()
            print(f'{name} started')
            thread_.join()
            print(f'{name} stopped')
            return print('download completed')
        return wrapper
    return thread_decor


@arg_thread_decor('thread1', False)
def download_(url, file_name):
    open_url = urlopen(url)
    file_ = open(file_name, "wb")
    file_.write(open_url.read())
    file_.close()


download_("http://www.google.com/images/srpr/logo1w.png", 'file1.png')
