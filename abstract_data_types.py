from collections import Counter

class Node(object):
    def __init__(self, val):
        self.next_node = None
        self.val = val

        
class LinkedList(object):
    
    head = None
    len = 0
    
    def __init__(self, val):
        self.head = Node(val)
        self.len = 1

    def add_node(self, val):
        new_head = Node(val)
        if self.head:
            new_head.next_node = self.head
        self.head = new_head
        self.len += 1
        
    def delete_node(self):
        val = None
        if self.head:
            val = self.head.val
            self.head = self.head.next_node
            self.len -= 1
        return val
    
    def remove_duplicates(self):
        lookup = {}
        previous = None
        n = self.head
        while n is not None:
            try:
                lookup[n.val] += 1
                previous.next_node = n.next_node
                self.len -= 1
            except:
                lookup[n.val] = 1
                previous = n
            n = n.next_node
        
    def remove_duplicates_in_place(self):
        head = self.head

        while head is not None:
            runner = head
            while runner.next_node is not None:
                if runner.next_node.val == head.val:
                    runner.next_node = runner.next_node.next_node
                    self.len -= 1
                else:
                    runner = runner.next_node
            head = head.next_node
  
    def print_vals(self):
        v = []
        n = self.head
        while n is not None:
            v.append(n.val)
            n = n.next_node
        return v
            
    
class Stack(LinkedList):
    def __init__(self):
        self.min = float("inf")
    
    def manage_min(func):
        def inner(*args, **kwargs):
            if func.__name__ == "push":
                if args[1] < args[0].min:
                    args[0].min = args[1]
                    #print(func.__name__, args, kwargs)
            return func(*args, **kwargs)
        return inner
    
    @manage_min
    def push(self, val):
        self.add_node(val)
        
    def pop(self):
        return self.delete_node()
    
    def peek(self):
        return self.head.val if self.head else None

    def is_empty(self):
        return True if not self.head else False

class StackedStacks(object):
    stacks = []
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stacks.append(Stack())
    
    def add_stack(self, val):
        s = Stack()
        s.push(val)
        self.stacks.append(s)
    
    def push(self, val):
        s = self.stacks[-1]
        if s.len == self.capacity:
            self.add_stack(val)
        else:
            s.push(val)
            
    def pop(self, sn=-1):
        try:
            s = self.stacks[sn]
        except IndexError as e:
            return None
        if s.len > 1:
            s = s.pop()
        else:
            s = s.pop()
            del(self.stacks[sn])
        return s
            
    def pop_at(self, sn):
        return self.pop(sn)
        
    
    def print_stacks(self):
        for s in self.stacks:
            print(s.print_vals())
        
class Queue(LinkedList):
    def __init__(self):
        pass
    
    def add(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            n = self.head
            while n.next_node is not None:
                n = n.next_node
            n.next_node = Node(val)

        self.len += 1
    
class Tests(object):
    def test(self):
        linked_list = LinkedList(1)
        linked_list.add_node(2)
        linked_list.add_node(2)
        linked_list.add_node(2)
        linked_list.add_node(3)
        print(linked_list.print_vals())
        print(linked_list.len)
        linked_list.add_node(1)
        print(linked_list.len)
        print(linked_list.print_vals())
        linked_list.remove_duplicates_in_place()
        print(linked_list.print_vals())
        print(linked_list.len)

    def test_stack(self):
        s = Stack()
        s.push(3)
        s.push(-2)
        s.push(2)
        print(s.print_vals())
        print(s.pop())
        print(s.peek())
        print(s.is_empty())
        print(s.pop())
        print(s.peek())
        print(s.is_empty())
        print(s.min)
        
    def test_queue(self):
        q = Queue()
        q.add(1)
        q.add(2)
        q.add(3)
        print(q.print_vals())
        print(q.len)
        
    def test_stacked_stacks(self):
        ss = StackedStacks()
        ss.push(1)
        ss.push(2)
        for i in range(3, 200):
            ss.push(i)
        ss.print_stacks()
        for i in range(10):
            print(ss.pop())
        ss.print_stacks()
        s = ss.pop()
        
        print(ss.pop_at(3))
        ss.print_stacks()
        #while s:
        #    print(s)
        #    s = ss.pop()
