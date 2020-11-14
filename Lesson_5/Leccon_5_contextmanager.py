class File:

    def __init__(self, file_name, file_method):
        self.file = open(file_name, file_method)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with File('text1.txt', 'w') as file:
    file.write('qwerty')
