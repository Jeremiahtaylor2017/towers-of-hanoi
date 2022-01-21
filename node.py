class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node  # Remove prev node for singly linked lists and queues

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):  # Remove function for singly linked lists and queues
        self.prev_node = prev_node

    def get_prev_node(self):  # Remove function for singly linked lists and queues
        return self.prev_node

    def get_value(self):
        return self.value
