class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(self.root, new_node)

    def _insert_node(self, node, new_node):
        if new_node.value < node.value:
            if node.left is None:
                node.left = new_node
            else:
                self._insert_node(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert_node(node.right, new_node)

    def search(self, value):
        return self._search_node(self.root, value)

    def _search_node(self, node, value):
        if node is None:
            return False

        if value == node.value:
            return True
        elif value < node.value:
            return self._search_node(node.left, value)
        else:
            return self._search_node(node.right, value)

    def remove(self, value):
        self.root = self._remove_node(self.root, value)

    def _remove_node(self, node, value):
        if node is None:
            return None

        if value == node.value:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp_node = self._find_min_node(node.right)
                node.value = temp_node.value
                node.right = self._remove_node(node.right, temp_node.value)
        elif value < node.value:
            node.left = self._remove_node(node.left, value)
        else:
            node.right = self._remove_node(node.right, value)

        return node

    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def traverse_in_order(self):
        result = []
        self._traverse_in_order_node(self.root, result)
        return result

    def _traverse_in_order_node(self, node, result):
        if node is not None:
            self._traverse_in_order_node(node.left, result)
            result.append(node.value)
            self._traverse_in_order_node(node.right, result)
