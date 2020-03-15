"""
    1) Insertion, deletion and search of singly-linked list;
    2) Assumes int type for data in list nodes.

    Author: Wenru
"""
from typing import Optional


class Node:

    def __init__(self, data: int, next_node=None):
        self.data = data
        self._next = next_node


class SinglyLinkedList:

    def __init__(self):
        self._head = None


    def find_by_value(self, value: int) -> Optional[Node]:
        p = self._head
        while p and p.data != value:
            p = p._next
        return p
    def find_node_by_node(self, new_node:Node, node:Node):

        if self._head == node:
            new_node._next = node
            self._head = new_node

        else:
            current = self._head
            while current._next != node:
                current = current._next
            current._next = new_node
            new_node._next = node
    def insert_value_before(self, node:Node, param):
        new_node = Node(param)
        # 在一个节点之前插入一个节点？先找到这个值的节点，在一个节点之前插入一个节点。先创建这个节点，再:new_node._next = node,再把node之前的节点指向这个节点。node._before._next = new_node.问题是怎么得到之前那个节点？如果是双向链表就好了。
        # 要找到第8个节点，只能用for循环，直到node._next = 现在这个找到的第几个节点。还要分几种情况，这个节点是头节点呢？
        # 把原来第8个节点的_next指向这个新的节点，如何找到第8个节点？如果是双向链表就可以利用现在找到的第9个节点。
        self.find_node_by_node(new_node,node)

    def insert_value_to_head(self, value):
        # 插入第一个
        new_node = Node(value)
        new_node._next = self._head
        self._head = new_node

    def delete_by_value(self, param):
        # 删除一个节点，给定一个值，先调函数找到这个节点，然后把它之后的节点node = 这个节点之前的节点. _next。如果找到这个节点呢，之前函数都已经写好了。
        node = self.find_by_value(param)
        if self._head == node:
            self._head = node._next
        else:
                current = self._head
                while current._next != node:
                    current = current._next
                current._next = node._next




if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)
    node9 = l.find_by_value(9)
    print(node9.data)
    l.insert_value_before(node9, 20)
    l.insert_value_before(node9, 16)
    l.insert_value_before(node9, 16)
    node16 = l.find_by_value(16)
    print(node16.data)
    l.delete_by_value(16)
    l.find_by_value(16)


""" 
    
    print(l)
    node11 = l.find_by_index(3)
    print(node11)
    l.delete_by_node(node11)
    l.delete_by_node(l._head)
    l.delete_by_value(13)
    print(l)
    for value in l:
        print(value)
"""