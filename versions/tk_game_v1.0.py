import tkinter as tk
from easygui import *
from PIL import Image, ImageTk
from random import *
import itertools
from time import *

numbers = 4
target = 24
score = 0
threshold = .0000001
solver_ans = ""


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
            global solver_ans
            solver_ans += str(chunks[0]) + "\n"

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
                        open_set.add(tuple(newChunks))


def hints(n1, n2, n3, n4):
    operations = (add, multiply, subtract, divide)
    global closed_set
    closed_set = set()
    global open_set
    open_set = set()
    initial = []
    initial.append(chunk(int(n1)))
    initial.append(chunk(int(n2)))
    initial.append(chunk(int(n3)))
    initial.append(chunk(int(n4)))
    initial.sort()

    open_set.add(tuple(initial))

    # Execute the solution search
    while len(open_set) > 0:
        # TODO remove debugging line input("open: {} closed: {}".format(len(open), len(closed)))
        chunks = open_set.pop()
        if chunks not in closed_set:
            operate(chunks)
        closed_set.add(chunks)


# 创建主窗口
root = tk.Tk()
root.title("24点游戏")


def is_valid_expression(expression):
    try:
        eval(''.join(expression))
        return True
    except:
        return False

def clear_entry():
    entry.delete(0, tk.END)

def check(expression, n1, n2, n3, n4):
    if expression == "":
        clear_entry()
        return "请输入表达式。"
    if not str(n1) in expression or not str(n2) in expression or not str(n3) in expression or not str(n4) in expression:
        clear_entry()
        return "请用给出的数字。"
    try:
        # 尝试计算表达式的值
        result = eval(expression)
        if result == 24:
            clear_entry()
            return "正确！"
        else:
            return "错误！"
    except SyntaxError:
        clear_entry()
        return "错误：表达式语法错误。"
    except NameError:
        clear_entry()
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
    image_files = ["", "", "", ""]
    for i in range(4):
        if i == 0:
            f = str(randint(1, 4))
            num1 = str(randint(1, 9))
            if num1 == "1":
                if f == "1":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "hearts.png"
                if f == "2":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "spades.png"
                if f == "3":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "diamonds.png"
                if f == "4":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "clubs.png"
            else:
                if f == "1":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num1 + "_of_" + "hearts.png"
                if f == "2":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num1 + "_of_" + "spades.png"
                if f == "3":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num1 + "_of_" + "diamonds.png"
                if f == "4":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num1 + "_of_" + "clubs.png"
        if i == 1:
            num2 = str(randint(1, 9))
            f = str(randint(1, 4))
            if num2 == "1":
                if f == "1":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "hearts.png"
                if f == "2":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "spades.png"
                if f == "3":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "diamonds.png"
                if f == "4":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "clubs.png"
            else:
                if f == "1":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num2 + "_of_" + "hearts.png"
                if f == "2":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num2 + "_of_" + "spades.png"
                if f == "3":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num2 + "_of_" + "diamonds.png"
                if f == "4":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num2 + "_of_" + "clubs.png"
        if i == 2:
            num3 = str(randint(1, 9))
            f = str(randint(1, 4))
            if num3 == "1":
                if f == "1":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "hearts.png"
                if f == "2":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "spades.png"
                if f == "3":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "diamonds.png"
                if f == "4":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "clubs.png"
            else:
                if f == "1":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num3 + "_of_" + "hearts.png"
                if f == "2":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num3 + "_of_" + "spades.png"
                if f == "3":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num3 + "_of_" + "diamonds.png"
                if f == "4":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num3 + "_of_" + "clubs.png"
        if i == 3:
            num4 = str(randint(1, 9))
            f = str(randint(1, 4))
            if num4 == "1":
                if f == "1":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "hearts.png"
                if f == "2":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "spades.png"
                if f == "3":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "diamonds.png"
                if f == "4":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + "ace" + "_of_" + "clubs.png"
            else:
                if f == "1":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num4 + "_of_" + "hearts.png"
                if f == "2":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num4 + "_of_" + "spades.png"
                if f == "3":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num4 + "_of_" + "diamonds.png"
                if f == "4":
                    image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num4 + "_of_" + "clubs.png"
    global images
    images = [load_image(file) for file in image_files]
    global labels
    labels = [tk.Label(root, image=img) for img in images]
    for i, label in enumerate(labels):
        label.grid(row=1, column=i)

def insert_and_clear(ans):
    entry.insert(0, ans)
    #root.after(1000, clear_entry)

# Create score board
score_label0 = tk.Label(root, text="得分：")
score_label0.grid(row=0, column=0)
score_label = tk.Label(root, text=str(score))
score_label.grid(row=0, column=1)
# Create 4 game cards
choose_image()
# 创建文本输入框
entry = tk.Entry(root)
entry.grid(row=2, column=0, columnspan=4, sticky="ew")

def on_button_click(index):
    global solver_ans
    global score
    if index == 1:
        print(entry.get())
        ans = check(entry.get(), num1, num2, num3, num4)
        if ans == "正确！":
            entry.insert(0, "恭喜你，答对了！继续下一题")
            score += 1
            score_label = tk.Label(root, text=str(score))
            score_label.grid(row=0, column=1)
            insert_and_clear(ans)
            choose_image()
        else:
            insert_and_clear(ans)
    elif index == 2:
        choose_image()
        clear_entry()
    elif index == 3:
        # TODO: disable the button
        if entry.get() != "":
            clear_entry()
        buttons[index - 1]["state"] = "disabled"
        ans = hints(num1, num2, num3, num4)
        hint = solver_ans.split('\n')
        if len(solver_ans) == 0:
            insert_and_clear("这道题无解，下一题")
            choose_image()
        else:
            msg = ""
            hintn = 0
            while (msg == ""):
                hintn = randint(0, len(hint) - 1)
                msg = hint[hintn]
            entry.insert(0, msg)
        # TODO: Clear open_set, close_set, solver_ans
        open_set = set()
        close_set = set()
        solver_ans = ""
        # TODO: enable the button
        buttons[index - 1]["state"] = "normal"


btn_names = [f"", f"表达式运行计算", f"想不出来，重新翻一组牌", f"太难了，提示我下吧"]
buttons = [tk.Button(root, text=btn_names[i], command=lambda i=i: on_button_click(i)) for i in range(1, 4)]

for i, button in enumerate(buttons):
    button.grid(row=3, column=i)

clear_entry()
root.mainloop()
