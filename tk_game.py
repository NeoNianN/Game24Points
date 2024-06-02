import tkinter as tk
from easygui import *
from PIL import Image, ImageTk
from random import *
import itertools
from time import *

# ! /usr/bin/env python3

numbers = 4
target = 24
threshold = .0000001


class chunk(object):
    def __init__(self, number, text=None):
        self.total = number
        if text is None:
            self.text = str(number)
        else:
            self.text = text

    # For sorting
    def __lt__(self, other):
        return self.total < other.total

    def __eq__(self, other):
        return self.text == other.text

    def __hash__(self):
        return hash(self.text)

    def __str__(self):
        return self.text

numbers = 4
target = 24
threshold = .0000001


class chunk(object):
    def __init__(self, number, text=None):
        self.total = number
        if text is None:
            self.text = str(number)
        else:
            self.text = text

    # For sorting
    def __lt__(self, other):
        return self.total < other.total

    def __eq__(self, other):
        return self.text == other.text

    def __hash__(self):
        return hash(self.text)

    def __str__(self):
        return self.text


def add(a, b):
    newTotal = a.total + b.total
    newText = "(" + a.text + " + " + b.text + ")"
    return chunk(newTotal, newText)


def multiply(a, b):
    newTotal = a.total * b.total
    newText = "(" + a.text + " * " + b.text + ")"
    return chunk(newTotal, newText)


def subtract(a, b):
    newTotal = a.total - b.total
    newText = "(" + a.text + " - " + b.text + ")"
    return chunk(newTotal, newText)


def divide(a, b):
    newTotal = a.total / b.total
    newText = "(" + a.text + " / " + b.text + ")"
    return chunk(newTotal, newText)


operations = [add, multiply, subtract, divide]


def operate(chunks):
    # Some divisions will not return integers, but let's assume that's okay.

    if len(chunks) == 1:
        # All compressed down to one chunk
        if (chunks[0].total - target < threshold) and \
                (target - chunks[0].total < threshold):
            print(chunks[0])

    else:
        # Some chunks still remain
        for chunk1 in chunks:
            chunksM1 = list(chunks)  # Makes a copy
            chunksM1.remove(chunk1)
            for chunk2 in chunksM1:
                chunksM2 = chunksM1.copy()
                chunksM2.remove(chunk2)
                for operation in operations:
                    try:
                        newChunk = operation(chunk1, chunk2)
                    except ZeroDivisionError:
                        pass  # Nothing specific to do; just don't make the recursive call.
                    else:
                        newChunks = chunksM2.copy()
                        newChunks.append(newChunk)
                        newChunks.sort()  # Should be O(n) because it was already sorted
                        open.add(tuple(newChunks))


def number_input(prompt):
    num = input(prompt)
    try:
        return int(num)
    except:
        return number_input("Not a valid number. Try again: ")

def hints(n1,n2,n3,n4):
    operations = (add, multiply, subtract, divide)
    closed = set()
    open = set()
    initial = []
    initial.append(chunk(int(n1)))
    initial.append(chunk(int(n2)))
    initial.append(chunk(int(n3)))
    initial.append(chunk(int(n4)))
    initial.sort()

    open.add(tuple(initial))

    # Execute the solution search
    while len(open) > 0:
        # TODO remove debugging line input("open: {} closed: {}".format(len(open), len(closed)))
        chunks = open.pop()
        if chunks not in closed:
            operate(chunks)
        closed.add(chunks)

# 创建主窗口
root = tk.Tk()
root.title("24点游戏")
def is_valid_expression(expression):
    try:
        eval(''.join(expression))
        return True
    except:
        return False

def check(expression,n1,n2,n3,n4):
    if expression == "":
        entry.delete(0, tk.END)
        return "请输入表达式。"
    if not str(n1) in expression or not str(n2) in expression or not str(n3) in expression or not str(n4) in expression:
        entry.delete(0, tk.END)
        return "请用给出的数字。"
    try:
        # 尝试计算表达式的值
        result = eval(expression)
        if result == 24:
            entry.delete(0, tk.END)
            return "正确！"
        else:
            entry.delete(0, tk.END)
            return "错误！"
    except SyntaxError:
        entry.delete(0, tk.END)
        return "错误：表达式语法错误。"
    except NameError:
        entry.delete(0, tk.END)
        return "错误：表达式中有未定义的变量或函数名。"
    except Exception as e:
        return f"错误：{e}"
def load_image(file):
    return ImageTk.PhotoImage(Image.open(file).resize((200, 200)))
def choose_image():
    global image_files
    global i
    global num1
    global num2
    global num3
    global num4
    image_files = ["","","",""]
    for i in range(4):
        if i == 0:
            f = str(randint(1, 4))
            num1 = str(randint(1, 9))
            if f == "1":
                image_files[i] = "Game_24_Images\\H" + num1 + ".png"
            if f == "2":
                image_files[i] = "Game_24_Images\\S" + num1 + ".png"
            if f == "3":
                image_files[i] = "Game_24_Images\\D" + num1 + ".png"
            if f == "4":
                image_files[i] = "Game_24_Images\\C" + num1 + ".png"
        if i == 1:
            num2 = str(randint(1, 9))
            f = str(randint(1, 4))
            if f == "1":
                image_files[i] = "Game_24_Images\\H" + num2 + ".png"
            if f == "2":
                image_files[i] = "Game_24_Images\\S" + num2 + ".png"
            if f == "3":
                image_files[i] = "Game_24_Images\\D" + num2 + ".png"
            if f == "4":
                image_files[i] = "Game_24_Images\\C" + num2 + ".png"
        if i == 2:
            num3 = str(randint(1, 9))
            f = str(randint(1, 4))
            if f == "1":
                image_files[i] = "Game_24_Images\\H" + num3 + ".png"
            if f == "2":
                image_files[i] = "Game_24_Images\\S" + num3 + ".png"
            if f == "3":
                image_files[i] = "Game_24_Images\\D" + num3 + ".png"
            if f == "4":
                image_files[i] = "Game_24_Images\\C" + num3 + ".png"
        if i == 3:
            num4 = str(randint(1, 9))
            f = str(randint(1, 4))
            if f == "1":
                image_files[i] = "Game_24_Images\\H" + num4 + ".png"
            if f == "2":
                image_files[i] = "Game_24_Images\\S" + num4 + ".png"
            if f == "3":
                image_files[i] = "Game_24_Images\\D" + num4 + ".png"
            if f == "4":
                image_files[i] = "Game_24_Images\\C" + num4 + ".png"
    global images
    images = [load_image(file) for file in image_files]
    global labels
    labels = [tk.Label(root, image=img) for img in images]
    for i, label in enumerate(labels):
        label.grid(row=0, column=i)

def clear_entry():
    entry.delete(0, tk.END)

def insert_and_clear(ans):
    entry.insert(0, ans)
    root.after(3000, clear_entry)

choose_image()
# 创建文本输入框
entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=4, sticky="ew")
def on_button_click(index):
    if index == 1:
        print(entry.get())
        ans = check(entry.get(),num1,num2,num3,num4)
        if ans == "正确！":
            entry.insert(0, "恭喜你，答对了！继续下一题")
            insert_and_clear(ans)
            choose_image()
        else:
            insert_and_clear(ans)
    elif index == 2:
        choose_image()
    elif index == 3:
        ans = hints(num1,num2,num3,num4)
        entry.insert(0,ans)

btn_names = [f"", f"表达式运行计算", f"想不出来，重新翻一组牌", f"太难了，提示我下吧"]
buttons = [tk.Button(root, text=btn_names[i], command=lambda i=i: on_button_click(i)) for i in range(1, 4)]

for i, button in enumerate(buttons):
    button.grid(row=2, column=i)

entry.delete(0, tk.END)
root.mainloop()