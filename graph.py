# Import matplotlib and numpy libraries for plotting.
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Check log files used for data input.
try:
    netfile = open('./logs/network.txt', 'r')
    memfile = open('./logs/memory.txt', 'r')
    cpufile = open('./logs/cpu.txt', 'r')
except IOError:
    print "Log file does not exist. Exiting gracefully"

# Read the whole file into a single variable, which is a list of every row of the file.
line1 = netfile.readlines()
line2 = memfile.readlines()
line3 = cpufile.readlines()

# Initialize some variables to be lists for:
# Network portion
x1 = []
y1 = []
# Memory portion
x2 = []
y2 = []
# CPU portion
x3 = []
y3 = []


# Start to plot using interactive/animation mode.
plt.ion()
fig = plt.figure()
plt.subplots_adjust(wspace=0.5)

# Scan the line, store it into variables as placeholders.
# Draw the graph with the data collected for:
# Network portion
for line in line1:
    p = line.split()
    x1.append(float(p[0]))
    y1.append(float(p[1]))
    xv = np.array(x1)
    yv = np.array(y1)
    plt.subplot(211)
    plt.plot(xv, yv, 'g-')
    plt.title('Network usage (BW)')
    plt.xlabel('sec')
    plt.ylabel('bytes/sec')
    plt.grid(True)
    plt.ylim((0,10000))
    plt.draw()
    plt.pause(0.000000001)

# Memory portion
for line in  line2:
    m = line.split()
    x2.append(float(m[0]))
    y2.append(float(m[1]))
    xm = np.array(x2)
    ym = np.array(y2)
    plt.subplot(223)
    plt.title ('Memory usage')
    plt.plot(xm, ym, 'r-')
    plt.xlabel('sec')
    plt.ylabel('MB')
    plt.grid(True)
    plt.ylim((0,10000))
    plt.draw()
    plt.pause(0.000000001)

# CPU portion
for line in line3:
    c = line.split()
    x3.append(float(c[0]))
    y3.append(float(c[1]))
    xc = np.array(x3)
    yc = np.array(y3)
    plt.subplot(224)
    plt.title ('CPU usage')
    plt.plot(xc, yc, 'b-')
    plt.xlabel('sec')
    plt.ylabel('%')
    plt.grid(True)
    plt.ylim((0,100))
    plt.draw()
    plt.pause(0.000000001)