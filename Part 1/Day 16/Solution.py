
with open('input.txt') as f:
    code = f.read()[:-1]



def decode(code):
    newNum = ''
    htob = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'
    }
    for x in code:
        newNum += htob[x]
    return newNum

code = decode(code)
sum= 0
def parse(data):
    global sum
    version = int(data[:3],2)
    sum += version
    data = data[3:]

    tid = int(data[:3],2)
    data = data[3:]
    if tid == 4:
        t = ""
        while True:
            t += data[1:5]
            cnt = data[0]
            data= data[5:]
            if cnt == '0':
                break
    else:
        ltid = data[0]
        data = data[1:]
        if ltid == '0':
            l = data[:15]
            data = data[15:]
            subpacketl = int(l,2)
            subpackets = data[:subpacketl]
            while subpackets:
                subpackets = parse(subpackets)
            data = data[subpacketl:]
        else:
            l = data[:11]
            data = data[11:]
            qty = int(l,2)
            for i in range(qty):
                data = parse(data)
    return data

parse(code)
print(sum)