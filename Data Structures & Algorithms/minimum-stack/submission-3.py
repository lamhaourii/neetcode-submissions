class MinStack:

    def __init__(self):
        self.stack=[]
        self.minn=float('inf')
        self.mins= []
        self.mapp={}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<=self.minn:
            self.minn=val
            self.mins.append(self.minn)
        
    def pop(self) -> None:
        top=self.stack.pop()
        if self.minn==top:
            del self.mins[-1]
            self.minn=self.mins[-1] if self.mins else float('inf')
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn if self.minn!=float('inf') else None

        
