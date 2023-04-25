# String Slicing and Concatination

st = "Hellow world"

print(st)
print(type(st))
print(st[0])
print(st[4])
print(len(st))
for i in range(len(st)):
    print(st[i])


# Slice

print(st[:6])
print(st[3:])
print(st[6:11])
print(st[::2])
print(st[::-1])
print(st[:5:-1])
print(st[4::-1])

# Format

st = "Hellow python how are you ?"
print(st)
course = "java"
dt= 12.67
st ="Hellow " + course+ "how are you ?"
print(st)
st = f"Hellow {course} how are {dt} ?"
print(st)
st = f"Hellow %f how are ?"%{dt}
print(st)
st = f"Hellow {course} how are {dt} ?"
print()
st =f"Hellow %s how are %f ? your marks %d"%(course,dt,50)
print(st)


# String escape

st = "hellow world"
print(st)
st1 = "hellow world"
print(st1)
st1 = "hellow \nworld"
print(st1)
st1 = "hellow \tworld"
print(st1)
st1 = "hellow \bworld"
print(st1)
st1 = "hellow \\new world"
print(st1)
st1 = "hellow  \"new\" world"
print(st1)
st1 = 'hellow  \'new\' world'
print(st1)
st1='/\/\/\/\\'
print(st1)
st1='\\" \\n \\t \\'
print(st1)


