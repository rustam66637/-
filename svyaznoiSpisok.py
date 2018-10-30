class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item): #добавление нового узла в конец списка
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self): #метод отладочного вывода списка
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val): #найти нужный узел по заданному значению
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def clear(self): #метод очистки всего содержимого
        self.__init__()

    def delete(self, val): #метод удаления одного узла по его значению
        node = self.head
        pred = None
        while node != None:
            if node.value == val:
                if self.tail.value == val:
                    self.tail = pred
                if pred == None:
                    self.head = node.next
                else:
                    pred.next = node.next
                return
            else:
                pred = node
            node = node.next

    def deleteAll(self, val): #метод удаления всех узлов по конкретному значению
        node = self.head
        pred = None
        while node != None:
            if node.value == val:
                if self.tail.value == val:
                    self.tail = pred
                if pred == None:
                    self.head = node.next
                else:
                    pred.next = node.next
            else:
                pred = node
            node = node.next

    def findAll(self, val): #метод поиска всех узлов по конкретному значению
        node = self.head
        i = 0
        s = dict()
        while node is not None:
            if node.value == val:
                s[i] = node.value
            node = node.next
            i += 1
        return s

    def size(self): #метод вычисления длины списка
        node = self.head
        s = 0
        while node != None:
            s += 1
            node = node.next
        return s

    def insert(self, i, x): #метод вставки узла после заданного узла
        if self.head == None:
            self.tail = self.head = Node(x) # проверка на пустой список
            return
        if i == 0: #если позиция 0
            self.head = Node(x, self.head)
            return
        node = self.head
        s=0
        while s!=None:
            s+=1
            if s == i:
                node.next = Node(x, node.next)
                if node.next.next == None:
                    self.tail = node.next
                break
            node = node.next

    def func(s, d): #функция, которая получает на вход два связанных списка, состоящие из целых значений, и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков
        if s.size()==d.size():
            node1=s.head
            node2=d.head
            s=[]
            while node1!=None:
                s.append(node1.value+node2.value)
                node1=node1.next
                node2=node2.next
            return s
