import re
def details(s):
    a=re.split('0',s)
    # print(a)
    b=[]
    for i in a:
        if i!="":
            b.append(i)
    print(f"first_name: {b[0]}")
    print(f"Last_name: {b[1]}")
    print(f"id: {b[2]}")
s="John000Wick000054"
details(s)