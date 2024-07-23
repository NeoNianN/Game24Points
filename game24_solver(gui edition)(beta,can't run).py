import tkinter as tk
from tkinter import messagebox

# ... 留下原有的chunk类和操作函数 ...
class chunk(object):
    def __init__(self, number, text=None):
        self.total = number
        if text is None:
            self.text = str(number)
        else:
            self.text = text
    import tkinter as tk
from tkinter import messagebox

# ... 留下原有的chunk类和操作函数 ...
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

def number_input_gui():
    global numbers_entry
    try:
        numbers = [int(numbers_entry[i].get()) for i in range(4)]
        return numbers
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字！")
        return []

def solve_puzzle():
    numbers = number_input_gui()
    if len(numbers) != 4:
        return

    initial = [chunk(number) for number in numbers]
    initial.sort()
    open.add(tuple(initial))

    # Execute the solution search
    while len(open) > 0:
        chunks = open.pop()
        if chunks not in closed:
            operate(chunks)
        closed.add(chunks)

    result = "\n".join(str(c) for c in closed if abs(c[0].total - target) < threshold)
    if result:
        result_text.set(result)
    else:
        result_text.set("没有找到解决方案")

# 创建主窗口
root = tk.Tk()
root.title("24点游戏求解器")

# 创建输入框
numbers_entry = []
for i in range(4):
    label = tk.Label(root, text=f"数字 {i+1}: ")
    entry = tk.Entry(root)
    label.grid(row=i, column=0)
    entry.grid(row=i, column=1)
    numbers_entry.append(entry)

# 创建按钮
solve_button = tk.Button(root, text="求解", command=solve_puzzle)
solve_button.grid(row=5, columnspan=2)

# 创建结果标签
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.grid(row=6, columnspan=2)

# 初始化集合
closed = set()
open = set()

# 开始主循环
root.mainloop()
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

def number_input_gui():
    global numbers_entry
    try:
        numbers = [int(numbers_entry[i].get()) for i in range(4)]
        return numbers
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字！")
        return []

def solve_puzzle():
    numbers = number_input_gui()
    if len(numbers) != 4:
        return

    initial = [chunk(number) for number in numbers]
    initial.sort()
    open.add(tuple(initial))

    # Execute the solution search
    while len(open) > 0:
        chunks = open.pop()
        if chunks not in closed:
            operate(chunks)
        closed.add(chunks)

    result = "\n".join(str(c) for c in closed if abs(c[0].total - target) < threshold)
    if result:
        result_text.set(result)
    else:
        result_text.set("没有找到解决方案")

# 创建主窗口
root = tk.Tk()
root.title("24点游戏求解器")

# 创建输入框
numbers_entry = []
for i in range(4):
    label = tk.Label(root, text=f"数字 {i+1}: ")
    entry = tk.Entry(root)
    label.grid(row=i, column=0)
    entry.grid(row=i, column=1)
    numbers_entry.append(entry)

# 创建按钮
solve_button = tk.Button(root, text="求解", command=solve_puzzle)
solve_button.grid(row=5, columnspan=2)

# 创建结果标签
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.grid(row=6, columnspan=2)

# 初始化集合
closed = set()
open = set()

# 开始主循环
root.mainloop()