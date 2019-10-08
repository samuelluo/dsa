"""
Given the head node of a singly linked list, reverse it in-place.

-----------------------------
(1)
prev      curr   next
None      1  ->  2  ->  3

(2)
prev      curr   next
None  <-  1  ->  2  ->  3

(3)       prev
          curr   next
None  <-  1  ->  2  ->  3

(3)              curr
          prev   next
None  <-  1  ->  2  ->  3

"""


class Node(object):
    def __init__(self, val):
        """
        Parameters
        ----------
        val : Any
        next_node : Node
        """
        self.val = val
        self.next_node = None


class LinkedList(object):

    head_node = None
    tail_node = None

    def __init__(self, vals=None, head_node=None, tail_node=None):
        if vals is None and head_node is not None and tail_node is not None:
            self.head_node = head_node
            self.tail_node = tail_node
        elif vals is not None and head_node is None and tail_node is None:
            self.head_node, self.tail_node = self.build_linked_list(vals)

    def __iter__(self):
        self.curr_node = self.head_node
        return self

    def next(self):
        """
        next is for Python 2
        If this is missing:
            TypeError: iter() returned non-iterator of type 'LinkedList'
        """
        if self.curr_node is not None:
            curr_node = self.curr_node
            self.curr_node = self.curr_node.next_node
            return curr_node
        else:
            raise StopIteration

    def __next__(self):
        """
        __next__ is for Python 3
        If this is missing:
            TypeError: iter() returned non-iterator of type 'LinkedList'
        """
        if self.curr_node is not None:
            curr_node = self.curr_node
            self.curr_node = self.curr_node.next_node
            return curr_node
        else:
            raise StopIteration

    def build_linked_list(self, vals):
        if len(vals) == 0:
            return None, None
        head_node = Node(vals[0])
        curr_node = head_node.next_node
        prev_node = head_node
        for val in vals[1:]:
            curr_node = Node(val)
            prev_node.next_node = curr_node
            prev_node = curr_node
            curr_node = curr_node.next_node
        tail = prev_node
        return head_node, tail

    def to_string(self):
        s = "["
        head_node = self.head_node
        while head_node is not None:
            s += str(head_node.val)
            head_node = head_node.next_node
            if head_node is not None:
                s += ", "
        s += "]"
        return s

    def reverse_list(self):
        """
        Reverses the LL in-place.
        Returns a new LL, but the original LL is also reversed.
        """
        prev_node = None
        curr_node = self.head_node
        next_node = None
        new_tail_node = self.head_node

        while curr_node is not None:
            next_node = curr_node.next_node    # move next
            curr_node.next_node = prev_node    # reverse the link
            prev_node = curr_node              # move prev
            curr_node = next_node              # move curr

        self.head_node = prev_node
        self.tail_node = new_tail_node
        ll = LinkedList(head_node=self.head_node, tail_node=self.tail_node)
        return ll


def run_test_case(vals):
    ll = LinkedList(vals=vals)
    i = iter(ll)
    print(ll.to_string())

    output = []
    for node in i:
        output.append(node.val)
    assert output == vals

    output = []
    for node in ll:
        output.append(node.val)
    assert output == vals

    ll = ll.reverse_list()
    print(ll.to_string())
    assert ll.to_string() == str(vals[::-1])

    print('')


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4],
        [1],
        [],
    ]
    for vals in test_cases:
        run_test_case(vals)
