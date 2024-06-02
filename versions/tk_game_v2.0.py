import tkinter as tk
from easygui import *
from PIL import Image, ImageTk
from random import *
from time import *

numbers = 4
target = 24
threshold = .0000001
solver_ans = ""
card_nums = []

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


def hints(n1, n2, n3, n4, is_quick_check=False):
    operations = (add, multiply, subtract, divide)
    global closed_set
    closed_set = set()
    global open_set
    open_set = set()
    global solver_ans
    solver_ans = ""

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
            if(is_quick_check == True and solver_ans != ""):
                break
        closed_set.add(chunks)
        
    return solver_ans


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
            return "答错！"
    except SyntaxError:
        clear_entry()
        return "错误：表达式语法错误。"
    except NameError:
        clear_entry()
        return "错误：表达式中有未定义的变量或函数名。"
    except Exception as e:
        return f"错误：{e}"


def load_image(file):
    return ImageTk.PhotoImage(Image.open(file).resize((250, 250)))


def update_image():
    global image_files
    image_files = ["", "", "", ""]
    suit_list = ["_of_hearts.png", "_of_spades.png", "_of_diamonds.png", "_of_clubs.png"]
    
    number_check_ok = False
    while(number_check_ok == False):
        global card_nums
        card_nums.clear()
        for i in range(4):
            if selected_mode.get() == 'easy':
                num = str(randint(1, 9))
            else:
                num = str(randint(1, 13))
            suit = randint(0, 3)
            image_files[i] = "Game_24_Images\\HQ_pokercards\\" + num + suit_list[suit]
            card_nums.append(num)
            #Check if the four numbers are solvable, if not update to next numbers
        ans = hints(card_nums[0], card_nums[1], card_nums[2], card_nums[3], True)
        if ans != "":
            number_check_ok = True

    global images
    images = [load_image(file) for file in image_files]
    global labels
    labels = [tk.Label(root, image=img) for img in images]
    for i, label in enumerate(labels):
        label.grid(row=1, column=i)


# def insert_and_clear(ans):
#     entry.insert(0, ans)
#     root.after(1000, clear_entry)

def clear_label():
    ver_label = tk.Label(root, text="                                         ")
    ver_label.grid(row=3, column=3) 
    
def on_button_click(index):
    global solver_ans
    global score
    if index == 1:
        enter = entry.get()
        ans = check(enter, card_nums[0], card_nums[1], card_nums[2], card_nums[3])
        if ans == "正确！":
            score += 1
            clear_label()
            ver_label = tk.Label(root, text="恭喜你，答对了！继续下一题。", fg="green")
            ver_label.grid(row=3, column=3)
            update_image()
        elif ans == "答错！":
            score -= 1
            clear_label()
            ver_label = tk.Label(root, text="很遗憾，答错了！" + "上一算式：" + enter, fg="red")
            ver_label.grid(row=3, column=3)
        else:
            clear_label()
            ver_label = tk.Label(root, text = ans, fg="red")
            ver_label.grid(row=3, column=3)
    elif index == 2:
        update_image()
        clear_entry()
    elif index == 3:
        # TODO: disable the button
        if entry.get() != "":
            clear_entry()
        buttons[index - 1]["state"] = "disabled"
        ans = hints(card_nums[0], card_nums[1], card_nums[2], card_nums[3])
        hint = solver_ans.split('\n')
        hintn = randint(0, len(hint) - 1)
        msg = hint[hintn]
        if selected_mode.get() == 'easy':
            msg = msg[0:15]
        else:
            msg = msg[0:12]
        entry.insert(0, msg)
        # TODO: Clear open_set, close_set, solver_ans
        open_set = set()
        close_set = set()
        solver_ans = ""
        # TODO: enable the button
        buttons[index - 1]["state"] = "normal"

#################################################################################################
#################################################################################################
# 创建主窗口
root = tk.Tk()
root.title("24点游戏                                                                                                                                                       by: 杭州市文理小学四年级24点小组    version: 2.0")

# Create score board
score = 0
score_label0 = tk.Label(root, text="得分：")
score_label0.grid(row=0, column=0)
score_label = tk.Label(root, text=str(score))
score_label.grid(row=0, column=1)

# Create mode selection buttons (easy mode and hard mode)
selected_mode = tk.StringVar()
mode_list = (('简单模式', 'easy'), ('复杂模式', 'hard'))
r_idx = 2 # Third column for mode selection buttons
for mode in mode_list:
    r = tk.Radiobutton(
        root,
        text=mode[0],
        value=mode[1],
        variable=selected_mode
    )
    r.grid(row=0, column=r_idx)
    if(r_idx == 2):
        r.select() # 默认选中第一个选项，即简单模式
    r_idx += 1
    
# Create 4 game cards
update_image()

# Create expression input box
entry = tk.Entry(root)
entry.grid(row=2, column=0, columnspan=4, sticky="ew")

# Add buttons
btn_names = [f"", f"表达式运行计算", f"太难了，重新翻一组牌吧", f"实在太难了，给我点提示吧"]
buttons = [tk.Button(root, text=btn_names[i], command=lambda i=i: on_button_click(i)) for i in range(1, 4)]
for i, button in enumerate(buttons):
    button.grid(row=3, column=i)
    
clear_label()
clear_entry()
root.mainloop()