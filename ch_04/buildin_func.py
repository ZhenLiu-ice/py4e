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

# 按字母排序并打印
for func in sorted(builtin_funcs):
    print(func)
