import sys
import datetime

time = datetime.datetime.now()
s1 = sys.argv[1]
s2 = int(sys.argv[2])





output = "The equivalent value in seconds: %s " % ((s1+" ")*s2)

print(output)