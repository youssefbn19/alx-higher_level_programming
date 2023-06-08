#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    if (len(sys.argv) == 1):
        print("{}".format(sum))
    else:
        for arg in sys.argv[1:]:
            sum += int(arg)
        print("{}".format(sum))
