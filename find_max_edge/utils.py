import sys
import datetime



time = datetime.datetime.now()
s1 = int(sys.argv[1])
s2 = int(sys.argv[2])



if s1 <= 0 or s2 <= 0:
    output = "The maximum edge of triangle for the sides: %d, %d is: Error,You entered either zero or less than zero, not valid  at time: %s" % (s1, s2, time)
else:
    max_length = s1 + s2 - 1
    output = "The area of triangle for the sides: %d, %d is: %s produced at time: %s" % (s1, s2,  max_length, time)



print(output)