class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['+','-','*','/']
        operands=[]
        for token in tokens:
            if token in operators:
                val2=operands.pop()
                val1=operands.pop()
                result= self.do_operation(token,val1,val2)
                
                operands.append(int(result))
            else:
                operands.append(int(token))
        return operands.pop()

    def do_operation(self, operator, val1, val2):
        if operator=='/':
            return val1/val2
        else:
            return (operator=='+')* (val1+val2)\
                    +(operator=='-')* (val1-val2)\
                    +(operator=='*')* (val1*val2)\