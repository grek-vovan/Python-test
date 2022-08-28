a=[1,2,3,4,5,6,7]
b=['he','she','it','they','them']

c={b:b for b in b}
d={a: a*1 for a in a}
print(d)
print(c)
