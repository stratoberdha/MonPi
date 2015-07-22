# Need to import the plotting package:
import matplotlib.pyplot as plt
import numpy as np

# Read the file.
f2 = open('network.txt', 'r')
f3 = open('memory.txt', 'r')
f4 = open('cpu.txt', 'r')

# read the whole file into a single variable, which is a list of every row of the file.
linebw = f2.readlines()
linemo = f3.readlines()
linecp = f4.readlines()

# initialize some variable to be lists:
# bandwidth
x1 = []
y1 = []
# memory
x12 = [] 
y12 = []
# cpu
x13 = []
y13 = []

# scan the rows of the file stored in lines, and put the values into some variables:
for line in linebw:
    p = line.split()
    x1.append(float(p[0]))
    y1.append(float(p[1]))

for line in  linemo:
    m = line.split()
    x12.append(float(m[0]))
    y12.append(float(m[1]))

for line in linecp:
    c = line.split()
    x13.append(float(c[0]))
    y13.append(float(c[1]))


plt.subplots_adjust(wspace=0.5)

xv = np.array(x1)
yv = np.array(y1)

xm = np.array(x12)
ym = np.array(y12)

xc = np.array(x13)
yc = np.array(y13)


# now, plot the data:
# network bandwidth
plt.subplot(211)
plt.plot(xv, yv, 'g-')
plt.title('Network usage (BW)')
plt.xlabel('sec')
plt.ylabel('bytes/sec')
plt.grid(True)
plt.ylim((0,10000))

# memory usage
plt.subplot(223)
plt.title ('Memory usage')
plt.plot(xm, ym, 'r-')
plt.xlabel('sec')
plt.ylabel('GB')
plt.grid(True)
plt.ylim((0,1))

# cpu usage
plt.subplot(224)
plt.title ('CPU usage')
plt.plot(xc, yc, 'b-')
plt.xlabel('sec')
plt.ylabel('%')
plt.grid(True)
plt.ylim((0,100))
plt.show()
