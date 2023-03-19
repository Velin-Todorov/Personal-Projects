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
    
    a = int(a)
    b = int(b)

    if op == '**' or op == '^':
        return b ** a
    
    elif op == '+':
        return a + b

    elif op == '-':
        return a-b if a > b else b -a

    elif op == '*':
        return a * b

    elif op == '/':
        if b != 0:
            return a / b
        return 0

    elif op == '%':
        return a % b

operator = []
operand = []

expression = input('Please enter your expression using spaces between all operators: ')

expr_split = expression.split(' ')

for i in expr_split:
    if i in ['0', '1','2','3','4','5','6','7','8','9', '10']:
        operand.append(i)

    elif i == '(':
        operator.append(i)


    elif i == ')':
        while True:
            
            if not operator or not operand:
                break

            op = operator.pop()

            if op == '(':
                break

            a = operand.pop()
            b = operand.pop()

            res = process(a, b, op)
            operand.append(res)


    elif i in ['**', '^', '+', '-', '/', '*', '//']:
        if not operator:
            operator.append(i)
        
        else:
            current_prec = precedence(i)
            last_el = operator[-1]

            if last_el == '(':
                operator.append(i)
                continue


            last_el_prec = precedence(last_el)

            if operator:
                if current_prec >= last_el_prec:
                    operator.append(i)
            
                elif current_prec < last_el_prec:
                    if operand:
                        while True:
                            
                            if not operator:
                                break

                            current_el = operator.pop()

                            if operator:
                                last = operator[-1]
                                if precedence(last) < precedence(current_el):
                                    break
                            
                            a = operand.pop()
                            b = operand.pop()
                            res = process(a, b, current_el)
                            operand.append(res)

                    operator.append(i)

if operator:
    while operator:
        a = operand.pop()
        b = operand.pop()
        op = operator.pop()
        operand.append(process(a, b, op))

print(operand.pop())
