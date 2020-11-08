class Stack:

    def __init__(self):
        self.items = []

    def clear(self):
        self.items.clear()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('Stack is already empty')
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            print('Stack is empty')
        else:
            return self.items[-1]

    def show_items(self):
        print(self.items)


class Queue:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            print('Queue is empty')
        else:
            return self.items[0]

    def clear(self):
        self.items.clear()

    def show_items(self):
        print(self.items[::-1])


class ComplexNum:

    def __init__(self, real=0, image=0):
        self.real = real
        self.image = image

    def __str__(self):
        if self.image >= 0:
            sign = '+'
        else:
            sign = ''
        if self.image == 1:
            return f'({self.real}{sign}j)'
        if self.image == -1:
            return f'({self.real}-j)'
        if self.real != 0 and self.image != 0:
            return f'({self.real}{sign}{self.image}j)'
        elif self.image != 0:
            return f'{self.image}j'
        else:
            return f'{self.real}'

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.image + other.image)

    def __sub__(self, other):
        return ComplexNum(self.real - other.real, self.image - other.image)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.image * other.image,
                          self.real * other.image + other.real * self.image)

    def __truediv__(self, other):
        conjugation = ComplexNum(other.real, -other.image)
        find_denominator = other * conjugation
        denominator = find_denominator.real
        nominator = self * conjugation
        return ComplexNum(nominator.real / denominator, nominator.image / denominator)


one = ComplexNum(3, 4)
two = ComplexNum(0, 5)
tree = ComplexNum(5, 0)
four = ComplexNum(1, 3)
five = ComplexNum(5, -2)
six = ComplexNum(1, 1)
seven = ComplexNum()
print(one)
print(two)
print(tree)
print(four)
print(five)
print(six)
print(seven)
print('-'*10)
print(one + five)
print(one * five)
print(one / five)

# stack1 = Stack()
# stack1.peek()
# stack1.push(5)
# stack1.push('b')
# stack1.push('cat')
# print(stack1.size())
# print(stack1.peek())
# stack1.show_items()
#
# queue1 = Queue()
# queue1.peek()
# queue1.push(5)
# queue1.push('b')
# queue1.push('cat')
# queue1.push('dog')
# print(queue1.size())
# print(queue1.peek())
# queue1.show_items()
# queue1.pop()
# queue1.clear()
# print(queue1.size())
# queue1.show_items()