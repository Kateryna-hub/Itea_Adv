from threading import Thread
from urllib.request import urlopen
from functools import wraps


def repeat(number_=1):

    def thread_decor(func):

        def wrapper(*args):
            thread_ = Thread(target=func, args=args)
            thread_.start()
            print(f'{item} started')
            thread_.join()
            print(f'{name} downloaded')
            return thread_
        return wrapper

    return thread_decor


list_of_links = ["http://www.google.com/images/srpr/logo1w.png", "http://www.google.com/images/srpr/logo2w.png",
                 'http://www.google.com/images/srpr/logo3w.png', 'http://www.google.com/images/srpr/logo4w.png',
                 'http://www.google.com/images/srpr/logo5w.png', 'http://www.google.com/images/srpr/logo6w.png',
                 'http://www.google.com/images/srpr/logo7w.png', 'http://www.google.com/images/srpr/logo8w.png',
                 'http://www.google.com/images/srpr/logo9w.png', 'http://www.google.com/images/srpr/logo10w.png'
                 ]

number = len(list_of_links)


@repeat(number)
def download_(url, file_name):
    open_url = urlopen(url)
    file_ = open(file_name, "wb")
    file_.write(open_url.read())
    file_.close()


n = 0
for item in list_of_links:
    n += 1
    name = 'logo' + str(n) + '.png'
    download_(item, name)

