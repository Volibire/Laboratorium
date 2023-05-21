from Zadanie_Stack import Stack


def k(elem):
    operand_stak = Stack()
    token_list = elem.split()
    for token in token_list:
        if token in "0123456789":
            operand_stak.push(float(token))

        else:
            operand2 = operand_stak.pop()
            operand1 = operand_stak.pop()
            result = math(token, operand1, operand2)
            operand_stak.push(result)
        return operand_stak.pop()

a = k("7 8 + 9 11 - 90 *")
print(a)



def math(operator,op1,op2):
    if operator == '**':
        return op1 ** op2
    elif operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2
    elif operator == '+':
        return op1 + op2
    elif operator == '-':
        return op1 - op2