import inspect
import builtins

s = "hello world"
print(repr(max(s)))
print(repr(min(s)))
print(len(s))

builtin_funcs = [
    name for name in dir(builtins)
    if inspect.isbuiltin(getattr(builtins, name)) and not name.startswith("_")
]

# 计算最长函数名，确定列宽
max_len = max(len(name) for name in builtin_funcs)
col_width = max_len + 2  # 加一些间距

# 每行显示5列
cols = 5
for i, func in enumerate(sorted(builtin_funcs), start=1):
    print(func.ljust(col_width), end="")
    if i % cols == 0:
        print()
print()
