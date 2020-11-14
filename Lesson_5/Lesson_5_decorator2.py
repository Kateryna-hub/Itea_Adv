from threading import Thread
from urllib.request import urlopen
from functools import wraps


def repeat(list_=[]):

    def thread_decor(func):

        @wraps(func)
        def wrapper(*args):
            for item in list_:
                filename = item[item.rfind("/") + 1:]
                thread_ = Thread(target=func, args=(item, filename))
                print(f'{thread_.getName()} started')
                thread_.start()
                print(f'{item}')
                thread_.join()
                print(f'{thread_.getName()} stopped')
            return thread_
        return wrapper

    return thread_decor


list_of_links = ["http://www.google.com/images/srpr/logo1w.png",
                 "http://c.files.bbci.co.uk/106B9/production/_114675276_catindex.jpg",
                 "https://download.geany.org/eht16-pubkey_old.txt",
                 'http://www.google.com/images/srpr/logo3w.png', 'http://www.google.com/images/srpr/logo4w.png',
                 'http://www.google.com/images/srpr/logo5w.png', 'http://www.google.com/images/srpr/logo6w.png',
                 'http://www.google.com/images/srpr/logo7w.png', 'http://www.google.com/images/srpr/logo8w.png',
                 'http://www.google.com/images/srpr/logo9w.png', 'http://www.google.com/images/srpr/logo10w.png'
                 ]


@repeat(list_of_links)
def download_(url, file_name):
    open_url = urlopen(url)
    file_ = open(file_name, "wb")
    file_.write(open_url.read())
    file_.close()


download_()
