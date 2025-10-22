class stack():
    def __init__(self):
        self.data = []
        self.top = -1
        self.max = 15

    def push(self, value):
        if self.top+1 == self.max:
            raise OverflowError("full")
        self.top+= 1
        self.data.insert(self.top,value)

    def pop(self):
        if self.top == -1:
            raise IndexError("lsit empty")
        del self.data[self.top]
        self.top-=1

    def peek(self):
    #if not self.is_empty():
    # return self.data[len(self.data) - 1]
        if self.top == -1:
    #When the stack is empty
            raise IndexError("Cannot peek from an empty stack.")
        print("Peek the top")
        return self.data[self.top]

    def length(self):
#return len(self.data)
        return self.top + 1
    
    def print_message(self):
        print("The stack size is " + str(self.length()) + " The top element is " +
        str(self.peek()))
    def print_all(self):
        #print(self.data)
        while self.top != -1:
            print(self.pop()) #doesnt work no return

    def remove_adjacent(self, input_str):
        print("\nThe input string is: ", input_str)
        result = ""
        for character in input_str:
            if self.length() > 0 and self.peek() == character:
                self.pop()
            else:
                self.push(character)
            s_temp = stack()
            while self.length() > 0:
                element = self.pop()
                s_temp.push(element)
            while s_temp.length() > 0:
                result = result + s_temp.pop()
                print("\nThe string after removing adjacent duplicates is: ", result)
        return result
    def bracket_check(self, input_str):
        print("\nThe input string is: ", input_str)
        pairs = {')': '(', '}': '{', ']': '['}
        for character in input_str:
#Push into stack if character is an opening bracket
            if character in pairs.values():
                self.push(character)
#If character is a closing bracket, check if match and if stack empty
            elif character in pairs:
                if self.length() == 0 or self.peek() != pairs[character]:
                    return False
# Pop the top element from stack
                self.pop()
#Return True if stack is empty, else False
        return self.length() == 0



class queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = -1
        self.max = 15

    def enqueue(self,value):
        if self.tail == self.max:
            raise OverflowError("full")
        self.tail +=1
        self.data.insert(self.tail, value)

    def dequeue(self):
        if self.tail == -1:
            raise IndexError("lsit empty")
        temp =self.head
        while temp < self.tail:
            temp +=1
            self.data[temp-1] = self.data[temp]
        del self.data[temp]
        self.tail -=1

    def peek(self):
        if self.tail == -1:
            raise IndexError("list empty")
        return self.data[self.head]

    def len(self):
        return self.tail +1

    def reverse(self):
        print("\nBefore reverse, the queue is ", self.data)
        stac = stack()
        while self.length() > 0:
            element = self.dequeue()
            stac.push(element)
        while stac.length() > 0:
            element = stac.pop()
            self.enqueue(element)
        print("\nThe reversed queue is ", self.data)




class CircularQueue:
    def __init__(self):
    #The main difference is that we reuse the space, or we say, we define different rules to update the head and tail
        self.data = []
        self.head = 0
        self.tail = 0
        self.max_size = 5
    def enqueue(self, newData):
        if self.tail - self.head == self.max_size:
    #When the circular queue is full
            raise OverflowError("Cannot insert into a full circular queue.")
        print("Enqueue the data " + str(newData))
        ind_tail = self.tail % self.max_size
        self.tail += 1
        self.data.insert(ind_tail, newData)
    def dequeue(self):
        if self.tail == self.head:
        #When the circular queue is empty - i.e. tail and head pointing to the same entry
#Reset the circular queue when it is empty
            self.data = []
            self.head = 0
            self.tail = 0
            raise IndexError("Cannot delete from an empty circular queue.")
        ind_head = self.head % self.max_size
        self.head += 1
        removed = self.data[ind_head]
        print("Dequeue the data " + str(removed))
        print("Now the new head is " + str(self.head) + " The index used for the head is " + str(ind_head))
        return removed

    def peek(self):
        if self.tail == self.head:
    #When the circular queue is empty
            raise IndexError("Can't peek from an empty queue")
        print("Peek the head")
        ind_head = self.head % self.max_size
        return self.data[ind_head]
    def length(self):
        return self.tail - self.head

    def print_message(self):
        print("The circular queue size is " + str(self.length()) + " The first element is " + str(self.peek()) + " The head ind is now " + str(self.head) + "The tail ind is now " + str(self.tail))

    def print_all(self):
        while self.tail != self.head:
            print(self.dequeue())

















def main():
    q = queue()
    q.enqueue(5)
    print(q.peek())

if __name__ == "__main__":
    main()
