from threading import Thread
from urllib.request import urlopen


class MyThread(Thread):

    def __init__(self, url, name_thread, is_daemon=False):
        super().__init__(name=name_thread, daemon=is_daemon)
        self.url = url

    def run(self) -> None:
        print(f'{self.name} download started {self.url}')
        open_url = urlopen(self.url)
        file_name = self.url[self.url.rfind("/") + 1:]
        with open(file_name, 'wb') as file_:
            file_.write(open_url.read())

        print(f'{self.name} download finished {self.url}')

list_of_links = ["http://www.google.com/images/srpr/logo1w.png",
                 "http://c.files.bbci.co.uk/106B9/production/_114675276_catindex.jpg",
                 "https://download.geany.org/eht16-pubkey_old.txt",
                 'http://www.google.com/images/srpr/logo3w.png', 'http://www.google.com/images/srpr/logo4w.png',
                 'http://www.google.com/images/srpr/logo5w.png', 'http://www.google.com/images/srpr/logo6w.png',
                 'http://www.google.com/images/srpr/logo7w.png', 'http://www.google.com/images/srpr/logo8w.png',
                 'http://www.google.com/images/srpr/logo9w.png', 'http://www.google.com/images/srpr/logo10w.png'
                 ]

for item, link_ in enumerate(list_of_links):
    name = 'Thread %s' % (item + 1)
    thread_ = MyThread(link_, name)
    thread_.start()



