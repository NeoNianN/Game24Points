from easygui import *
from random import *

def hints(numbers):
    #根据提供的四个数字生成表达式
    expressions = [];
    for i in range(0,4):
        for j in range(0,4):
            if i != j:
                for k in range(0,4):
                    if k != i and k != j:
                        for l in range(0,4):
                            if l != i and l != j and l != k:
                                expressions.append(str(numbers[i]) + " + " + str(numbers[j]) + " + " + str(numbers[k]) + " + " + str(numbers[l]));
def check(expression,n1,n2,n3,n4):
    if expression == None or expression == False:
        exit(0);
    if expression == "hints":
        numbers = [int(n1),int(n2),int(n3),int(n4)];
        hexp = hints(numbers);
        enterbox(str(n1) + "  " + str(n2) + "  " + str(n3) + "  " + str(n4), "Play 24 points game",hexp);
    if expression == "switch":
        return "switch is ready";
    if expression == "":
        return "empty!";
    if not str(n1) in expression or not str(n2) in expression or not str(n3) in expression or not str(n4) in expression:
        return "please use the given numbers!";
    try:
        # 尝试计算表达式的值
        result = eval(expression)
        if result == 24:
            return "correct";
        else:
            return "wrong";        # 如果表达式导致除以零的错误，返回相应的错误信息
        return "错误：不能除以零。"
    except SyntaxError:
        # 如果表达式语法错误，返回相应的错误信息
        return "错误：表达式语法错误。"
    except NameError:
        # 如果表达式中有未定义的变量或函数名，返回相应的错误信息
        return "错误：表达式中有未定义的变量或函数名。"
    except Exception as e:
        # 捕获其他所有异常，并返回异常信息
        return f"错误：{e}"

def game():
    cc = ccbox("Lets'play 24 points game.Please write the expression for the 4 numbers operation.\nIf you want hints or want switch? Just enter it.\nshall I continue?","Play 24 points game");
    if cc == None or cc == False:
        exit(0);
    while (True):
        num1 = randint(1,9);
        num2 = randint(1,9);
        num3 = randint(1,9);
        num4 = randint(1,9);
        expression = enterbox(str(num1) +"  "+ str(num2) +"  "+ str(num3) +"  "+ str(num4),"Play 24 points game");
        c = check(expression,num1,num2,num3,num4);
        msgbox(c,"play 24 points game");

game();