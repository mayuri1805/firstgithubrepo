st = "Hello world"
cnt = len(st)
lst = " "
for i in range(cnt):
    for j in range(i + 1, cnt-1):
        if st[i] != " ":
            if st[i] == st[j]:
                lst = lst + st[i]
                st = st.replace(str(st[i])," ")
                print()
print("duplicate character from string is:-",lst)