#/usr/bin/python3
import random




class Node:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.__repr__

class Stack:

    def __init__(self):
        self.nodes = []

    def __repr__(self):
        self.nodes.reverse()
        arrow = '->'
        return arrow.join(self.nodes)
    def add(self, data):
        node = Node(data)
        self.nodes.append(node)

    def pop(self):
        return self.nodes.pop(-1)

    
if __name__ == '__main__':

    stack = Stack()

    for i in range(10):
        num = random.randint(1, 100)
        stack.add(num)

    print(stack)