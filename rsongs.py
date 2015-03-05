import sys
from select import select

def request_song():
    timeout = 15
    print "Enter something:"

    rlist, _, _ = select([sys.stdin],[],[],timeout)
    if rlist:
        s = sys.stdin.readline()
        s.split("\n")
        return s
    else:
        return None
