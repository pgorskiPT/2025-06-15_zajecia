from functools import  singledispatch


@singledispatch
def process(x):
    print("Default:",x)

@process.register(int)
def _(x):
    print("Int:",x)


@process.register(str)
def _(x):
    print("Str:",x)

process(43)
process("hello")