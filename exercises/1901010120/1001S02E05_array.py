a = [0,1,2,3,4,5,6,7,8,9]
a.reverse()
print(a)


a1=(str(i) for i in a )
b="".join(a1)
print(b)
c = b[2:8]
print(c)

d=c[::-1]
print(d)

e=int(d)
print(e)

print("十进制",e)
print("二进制",bin(e))
print("八进制",oct(e))
print("十六进制",hex(e))