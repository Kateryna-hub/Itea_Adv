class MyList:

    def __init__(self, size):
        self.my_list = [0] * size

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __setitem__(self, index, value):
        self.my_list[index] = value

    def __getitem__(self, index):
        return '{} {}'.format(index, self.my_list[index])

    def __str__(self):
        return str(self.my_list)

    def append(self, element):
        self[len(self):] = [element]

    def pop(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

    def clear(self):
        pass


i = MyList(5)
print(i)

class CustomArray:

    def __init__(self, size, type_):
        self._list = [0] * size
        self._type = type_

    def __getitem__(self, item):
        return self._list[item]

    def __setitem__(self, key, value):

        if isinstance(key, int) and type(value) == self._type:
            self._list[key] = value
        else:
            raise TypeError('Type error')

