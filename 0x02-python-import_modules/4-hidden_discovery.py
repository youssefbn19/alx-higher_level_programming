#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid
    for n in dir(hid):
        if n[0] != '_':
            print("{}".format(n))
