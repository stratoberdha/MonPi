# demonstrate psutil for memory and cpu usages
import sys
import subprocess
import psutil as ps




print "Collecting info on RAM and CPU: "

for x in range(0, 10):
    cpu = ps.cpu_percent(interval=2)
    mem = ps.virtual_memory()
    m = mem.used >> 20
     
    mfile = "/home/nestig/monpi/logs/memory.txt"
    cfile = "/home/nestig/monpi/logs/cpu.txt"
    space = " "
    newline = '\n'
    y  = x * 5 # arbitrarily set loop variable to get samples
    
    # open memory log file
    openfile = open(mfile, 'a')      
    openfile.write(str(y))
    openfile.write(space)
    openfile.write(str(m))
    openfile.write('\n')
    openfile.close()
    
    # open cpu log file
    openfile = open(cfile, 'a')
    openfile.write(str(y))
    openfile.write(space)
    openfile.write(str(cpu))
    openfile.write('\n')
    openfile.close()
    
   
     

# call filedata_graph.py to plot
subprocess.call(['python /home/nestig/monpi/filedata_graph.py'], shell=True)

subprocess.call(['cat /dev/null > /home/nestig/monpi/logs/network.txt'], shell=True)
subprocess.call(['cat /dev/null > /home/nestig/monpi/logs/memory.txt'], shell=True)
subprocess.call(['cat /dev/null > /home/nestig/monpi/logs/cpu.txt'], shell=True)

    #print m
    # print the data to the screen
    #print "CPU usage: ", cpu
    #print "Memory usage: ", mem.used >> 20


