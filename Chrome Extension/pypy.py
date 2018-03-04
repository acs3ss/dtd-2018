import sys
# print sys.argv[0] prints test.py
# print sys.argv[1] prints your_var_1

def hello():
    print "Hi" + " " + sys.argv[1]

if __name__ == "__main__":
    hello()