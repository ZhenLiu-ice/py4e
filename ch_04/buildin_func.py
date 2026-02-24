import inspect
import builtins

s = "hello world"
print(repr(max(s)))
print(repr(min(s)))
print(len(s))


# 获取所有内置函数
builtin_funcs = [
    name
    for name in dir(builtins)
    if inspect.isbuiltin(getattr(builtins, name)) and not name.startswith("_")
]

for i, func in enumerate(sorted(builtin_funcs), start=1):
    if i % 5 != 0:
        print(func, end="\t")
    else:
        print(func)

print()
