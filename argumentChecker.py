# Gives priority of operators
def priority(op):
    p = {3: "!",
         2: "&",
         1: "|",
         0: ['>', '<']
         }
    for i in range(4):
        if op in p[i]:
            return i


def infixToPostfix(eq):
    eq.append(')')
    eq.insert(0, '(')

    op = ['&', '|', '!', '>', '<']
    pf = []
    stack = []

    for i in eq:
        if str(i) not in op and i not in ['(', ')']:
            pf.append(i)

        elif i == "(":
            stack.append(i)

        elif i == ")":
            while stack[-1] != '(':
                item = stack.pop()
                pf.append(item)
            stack.pop()

        elif i in op:
            while True:
                if stack[-1] == "(":
                    stack.append(i)
                    break

                elif priority(stack[-1]) < priority(i):
                    stack.append(i)
                    break

                elif priority(stack[-1]) >= priority(i):
                    op = stack.pop()
                    pf.append(op)

    pf.append('$')
    return pf


def evaluate(eq):
    pf = infixToPostfix(eq)
    op = ['&', '|', '!', '>', '<', '(', ')']
    print(pf)
    output = None
    stack = []
    if len(pf) > 2:
        for i in pf:
            if i == '$':
                break

            elif i not in op:
                stack.append(i)

            else:

                if i == '&':
                    b = stack.pop()
                    a = stack.pop()
                    output = a and b
                    stack.append(output)

                elif i == '|':
                    b = stack.pop()
                    a = stack.pop()
                    output = a or b
                    stack.append(output)

                elif i == '!':
                    b = stack.pop()
                    output = not b
                    stack.append(output)

                elif i == '>':
                    b = stack.pop()
                    a = stack.pop()
                    output = (not a) or b
                    stack.append(output)

    #             elif i == '&':
    #                 output = a & b
    else:
        return pf[0]

    return output

# decimal to binary


def binary(num, cols):
    binary = []
    while (num > 1):
        if num % 2 == 0:
            binary.append(False)
        else:
            binary.append(True)
        num = num // 2

    if num != 0:
        binary.append(True)

    while (len(binary) < cols):
        binary.append(False)

    binary.reverse()
    return binary


def argumentChecker(arg):
    try:
        # removing spaces from userinput
        arg = [i for i in list(arg) if i != " "]
        arg = "".join(arg)
        print(arg)

        # spliting premises and conclusion
        arg = arg.split('@')
        premises = list(arg[0])
        conclusion = list(arg[1])
        print(premises, conclusion)

        # finding variables
        op = ['&', '|', '!', '>', '<', "(", ")"]
        var = []
        for i in range(len(arg)):
            ele = list(arg[i])
            for j in ele:
                if j not in op and j != ',':
                    if j not in var:
                        var.append(j)
        print(var)

        # Generate Truth Table
        cols = len(var)
        rows = 2**len(var)
        TT = []

        for i in range(rows):
            TT.append(binary(i, cols))
        TT.reverse()
        print(TT)

        # solving all propostions
        list_premises = "".join(premises).split(',')
        evaluated = []

        for i in list_premises:
            i = list(i)
            single_col = []
            temp = i.copy()
            for j in range(rows):
                i = temp.copy()
                for k in range(len(i)):
                    if i[k] in var:
                        i[k] = TT[j][var.index(i[k])]

                single_col.append(evaluate(i))
            evaluated.append(single_col)
        print(evaluated)

        # Solving conlusion
        eval_conclusion = []
        temp2 = conclusion.copy()
        for i in range(rows):
            conclusion = temp2.copy()
            for j in range(len(conclusion)):
                if conclusion[j] in var:
                    conclusion[j] = TT[i][var.index(conclusion[j])]
            eval_conclusion.append(evaluate(conclusion))
        eval_conclusion

        valid = True
        for i in range(rows):
            check = True
            for j in range(len(evaluated)):
                if evaluated[j][i] != True:
                    check = False

            if check:
                if eval_conclusion[i] == True:
                    print(i+1, True)
                else:
                    print(i+1, eval_conclusion[i])
                    valid = False
        if valid:
            print("Valid Argument")
            return True
        else:
            print("Invalid Argument")
            return False
    except Exception as e:
        print(e)
        return "Error"
