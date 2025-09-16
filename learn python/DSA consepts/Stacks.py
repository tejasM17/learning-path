# A stack is a data structure that can hold many elements.

# [1, 2, 3, 4]

# Methods :
# push()pop()peek()isEmpty()size()

# Push: Adds a new element on the stack.
# Pop: Removes and returns the top element from the stack.
# Peek: Returns the top element on the stack.
# isEmpty: Checks if the stack is empty.
# Size: Finds the number of elements in the stack.

# Push
stack = []
stack.append("a")
stack.append("b")
stack.append("c")

print(f"stack : {stack}")

# Pop
element = stack.pop()
print(f"Pop element : {element},\nstak : {stack}")

# Peek
topelemnet = stack[-1]
print(f"Top element : {topelemnet}")

# isEmpty
isempty = not bool(stack)
print(f"is empty : {isempty}")

#  Size
print(f"length : {len(stack)}")


# But to explicitly create a data structure for stacks, with basic operations,
#  we should create a stack class instead. This way of creating stacks in Python
#  is also more similar to how stacks can be created in other programming languages
#  like C and Java.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


myStack = Stack()

myStack.push("a")
myStack.push("b")
myStack.push("c")
myStack.push("d")

print(f"myStack : {myStack.stack}")

print(
    f" pop : {myStack.pop()} \n peek : {myStack.peek()} \n isempty : {myStack.isEmpty()} \n size : {myStack.size()}"
)
