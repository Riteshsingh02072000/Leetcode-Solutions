class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack1 = []
        stack2 = []
        top = ''
        for i in expression:
            if i==',':
                continue
            
            elif i==')':
                top = stack1.pop()
                while top!='(':
                    stack2.append(top)
                    top = stack1.pop()
                

                top = stack1.pop() #for operator

                if top == '|':
                    stack1.append('t' if 't' in stack2 else 'f')
                elif top == '&':
                    stack1.append('f' if 'f' in stack2 else 't')
                elif top == '!':
                    stack1.append('f' if 't' in stack2 else 't')

                stack2.clear()
            
            else:
                stack1.append(i)
        
        return True if stack1[0]=='t' else False