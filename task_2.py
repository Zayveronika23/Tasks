'''
Реализация на основе списка.
Абстрактная модель, которую можно легко изменить и внедрить.
'''


class Queue1:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def get_element(self):
        return self.queue[0]

    def pop(self):
        el = self.queue.pop(0)
        return el

    def is_empty(self):
        return not self.queue

    def get_queue(self):
        return self.queue


'''
Реализация с помощью связанного списка.
Используется 2 класса, более конкретная реализация,
имеет больше вариантов модернизации.
'''


class Node:
    def __init__(self, current_item, nex_item=None):
        self.current_item = current_item
        self.next_item = nex_item

    def __str__(self):
        return str(self.current_item)


class Queue2:
    def __init__(self):
        self.head = None
        self.last = None

    def push(self, item):
        item = Node(item)
        if not self.head:
            self.head = item
        else:
            self.last.next_item = item
        self.last = item

    def get_element(self):
        return self.head

    def pop(self):
        el = self.head
        self.head = el.next_item
        return el

    def is_empty(self):
        return not self.head

    def get_queue(self):
        el = self.head
        while self.last.next_item != el:
            current_value = el
            el = current_value.next_item
            print(current_value)


'''
Методы push, get_element, is_empty имеют констную сложность.
Метод pop в первом случае имеет линейную сложность,
а во втором постоянную. Метод get_queue в пером случае
имеет константную сложность, а во втором линейную.
'''
