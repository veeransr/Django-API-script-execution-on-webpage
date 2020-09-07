import sys
import datetime

time = datetime.datetime.now()
s1 = int(sys.argv[1])
s2 = int(sys.argv[2])
s3 = int(sys.argv[3])
s4 = int(sys.argv[4])


days = s1 * 3600 * 24
hours = s2 * 3600
minutes = s3 * 60
seconds = s4

time1 = int(days + hours + minutes + seconds)

output = "The equivalent value in seconds: %d" % time1

print(output)