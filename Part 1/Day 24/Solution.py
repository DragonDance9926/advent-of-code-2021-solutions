
with open("input.txt") as f:
    a = f.read().split('\n')[:-1]


x = 0
y = 0
z = 0
w = 0
check = 99598963999960
valid = False

while (not valid):
    check = str(check)
    if "0" in check:
        check = check.replace("0", "1")
    digit = 0
    w = 0
    x = 0
    y = 0
    z = 0
    for line in a:
        lines = line.split()
        if lines[0] == "inp":
            exec(f"{lines[1]}=int(check[digit])")
            digit += 1
        if lines[0] == "add":
            exec(f"{lines[1]} = {lines[1]} + {lines[2]}")
        if lines[0] == "mul":
            exec(f"{lines[1]} = {lines[1]} * {lines[2]}")
        if lines[0] == "div" and lines[2] != '0':
            exec(f"{lines[1]} = {lines[1]} // {lines[2]}")
        if lines[0] == "mod":
            exec(f"{lines[1]} = {lines[1]} % {lines[2]}")
        if lines[0] == "eql":
            exec(f"{lines[1]} = int({lines[1]} == {lines[2]})")
    if z == 0:
        valid = True
        print(check)
    else:
        check = int(check) +1




