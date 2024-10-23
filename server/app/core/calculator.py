class RPNCalculator:
    def __init__(self):
        self.stack = []

    def evaluate(self, expression: list[str]) -> dict:
        """
        Evaluate a Reverse Polish Notation (RPN) expression.
        Supports +, -, *, / operations. Returns a result or error.
        """
        try:
            for i in expression:
                if i.isdigit():
                    self.stack.append(int(i))
                else:
                    if len(self.stack) < 2:
                        return {"error": "Invalid operation: insufficient values"}
                    b = self.stack.pop()
                    a = self.stack.pop()
                    if i == '+':
                        self.stack.append(a + b)
                    elif i == '-':
                        self.stack.append(a - b)
                    elif i == '*':
                        self.stack.append(a * b)
                    elif i == '/':
                        if b == 0:
                            return {"error": "Division by zero"}
                        self.stack.append(a / b)
                    else:
                        return {"error": f"Invalid operator: {i}"}

            if len(self.stack) != 1:
                return {"error": "Too many values left in the stack"}
            
            return {"result": self.stack.pop()}

        except Exception as e:
            return {"error": str(e)}

# Example of input : {"operation": ["3", "4", "+", "2", "*", "1", "+"]}