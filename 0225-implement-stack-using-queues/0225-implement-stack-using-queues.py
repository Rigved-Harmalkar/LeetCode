class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        return

    def pop(self) -> int:
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            popped_value = self.q1.pop(0)
            self.q1,self.q2 = self.q2, self.q1
            return popped_value
        return -1

        

    def top(self) -> int:
        if self.q1:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            top_value = self.q1[0]
            self.q2.append(self.q1.pop(0))
            self.q1,self.q2 = self.q2, self.q1
            return top_value
        return -1
        
    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()