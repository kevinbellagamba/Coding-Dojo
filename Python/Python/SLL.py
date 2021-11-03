class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        
    def addFront(self, value):
        runner = Node(value)
        if self.head != None:
            runner.next = self.head
        self.head = runner
        return self

    def addBack(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = Node(value)
            return self

    def printVals(self):
        if self.head == None:
            print("no values")
        else:    
            runner = self.head
            while runner != None:
                print(runner.value)
                runner = runner.next
        return self

    def removeFront(self):
        if self.head != None:
            self.head = self.head.next
        return self

    def count(self):
        runner = self.head
        counter = 0
        while runner != None:
            runner = runner.next
            counter += 1
        print(f'Count: {counter}') 
        return self
            
    def max(self):
        if self.head == None:
            print('no values')
        else:
            runner = self.head
            max = self.head.value
            while runner.next != None:
                if runner.next.value > max:
                    max = runner.next.value
                runner = runner.next
            print(f'Max: {max}')
            return self

    def removeDupes(self):
        if self.head == None:
            print('add values')
            return self
        if self.head.next == None:
            print('single node')
            return self
        newValues = [self.head.value]
        runner = self.head
        while runner.next != None:
            if runner.value not in newValues:
                newValues.append(runner.next.value)
            else:
                while runner.next in newValues:
                    runner.next = runner.next.next
            runner = runner.next
        print(newValues)
        return self

x = SLL()
x.addFront(3)
x.addFront(5)
x.addBack(2)
x.addBack(3)
x.count()
x.max()


x.printVals()
