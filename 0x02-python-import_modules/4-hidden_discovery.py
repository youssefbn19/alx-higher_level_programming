#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    for n in dir(hidden):
        if n[0] != '_':
	        print("{}".format(n))
