"""
Реализовать алгоритм двоичного дерево поиска

Бинарное дерево поиска (BST) — это дерево, в котором все узлы следуют указанным
ниже свойствам. Левое поддерево узла имеет ключ, меньший или равный ключу его
родительского узла. Правое поддерево узла имеет ключ больше, чем ключ его
родительского узла. Таким образом, BST делит все свои поддеревья на два сегмента:
левое поддерево и правое поддерево и может быть определено как -
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)


https://tproger.ru/translations/binary-search-tree-for-beginners/
"""


class BinaryTree:
    left_subtree = None
    right_subtree = None
    key: int

    def __init__(self, key):
        self.key = key

    def add(self, key):
        if self.key >= key:
            if self.left_subtree is None:
                self.left_subtree = BinaryTree(key)
            else:
                self.left_subtree.add(key)
        else:
            if self.right_subtree is None:
                self.right_subtree = BinaryTree(key)
            else:
                self.right_subtree.add(key)

    def __str__(self, count=0, lst=[]):
        lst.append(f"{' ' * count * 2}{self.key}\n")
        if self.left_subtree is not None:
            self.left_subtree.__str__(count + 1)
        if self.right_subtree is not None:
            self.right_subtree.__str__(count + 1)

        return ''.join(lst)

# bool Contains(T value)
#
# bool Remove(T value)
#
# void PreOrderTraversal(Action action)
#
# void PostOrderTraversal(Action action)
#
# void InOrderTraversal(Action action)
#
# IEnumerator GetEnumerator()
#
# System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator()
#
# void Clear()
#
# public int Count


if __name__ == '__main__':

    bt = BinaryTree(5)

    bt.add(3)
    bt.add(14)
    bt.add(6)
    bt.add(7)
    bt.add(13)
    bt.add(2)
    bt.add(4)

    print(bt)
