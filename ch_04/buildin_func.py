import inspect
import builtins

s = "hello world"
print(repr(max(s)))
print(repr(min(s)))
print(len(s))


# 获取所有内置函数
builtin_funcs = [
    name for name in dir(builtins) if inspect.isbuiltin(getattr(builtins, name))
]

for i, func in enumerate(sorted(builtin_funcs)):
    if i % 9 !=0 and  not func.startswith("_"):
        print(func, end='\t')
    else:
        print(func)
print()
