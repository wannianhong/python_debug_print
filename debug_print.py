import binascii

test = "\xab\xcd\xef\x11\x001111111111111111111111111111111111111111111111111111111"


def print_data(data):
    tlist = []
    tasc = []
    i = 0
    for v in data:
        tlist.append("%02X " % ord(v))
        if v.isprintable():
            tasc.append("%s" % v)
        else:
            tasc.append(".")
        i = i + 1
        if (i % 16) == 0:
            pt = "".join(tlist)
            pt += "".join(tasc)
            print("%s" % pt)
            tlist.clear()
            tasc.clear()


print_data(test)
