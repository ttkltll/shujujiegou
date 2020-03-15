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

    def insert_value_before(self, node9, param):
        new_node = Node(param, node9)
        # 把原来第8个节点的_next指向这个新的节点，如何找到第8个节点？如果是双向链表就可以利用现在找到的第9个节点。

    def insert_value_to_head(self, i):
        # 插入第一个
        new_node = Node(i, None)
        self._head = new_node
        new_node._next =

        # 第二个
        new_node2 = Node(2, new_node1)
        new_node3 = Node(3, new_node2)




if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)
    node9 = l.find_by_value(9)
    print(node9.data)
    print(l)
    l.insert_value_before(node9, 20)
    print(l)
    l.insert_value_before(node9, 16)
    print(l)
    l.insert_value_before(node9, 16)
    l.delete_by_value(16)
    print(l)
    node11 = l.find_by_index(3)
    print(node11)
    l.delete_by_node(node11)
    l.delete_by_node(l._head)
    l.delete_by_value(13)
    print(l)
    for value in l:
        print(value)
