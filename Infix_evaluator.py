"""
This is a program that evaluates infix expressions

"""
def precedence(char):
    if char == '+' or char == '-':
        return 1

    if char == '*' or char == '/' or char == '//' or char == '%':
        return 2
    
    if char == '^' or char == '**':
        return 3

def process(a, b, op):

    if op == '**' or op == '^':
        return a ** b
    
    elif op == '+':
        return a + b

    elif op == '-':
        return a-b

    elif op == '*':
        return a * b

    elif op == '/':
        return a / b

    elif op == '%':
        return a % b

operator = []
operand = []

expression = input('Please enter your expression using spaces between all operators: ')

expr_split = expression.split(' ')


for i in expression:

    if i in ['**', '^', '+', '-', '/', '*']:
        
        if not operator:
            operator.append(i)
        else:
            current_prec = precedence(i)
            last_el = operator[-1]
            last_el_prec = precedence(last_el)

            if current_prec >= last_el_prec:
                operator.append(i)
            
            else:
                pass
                

