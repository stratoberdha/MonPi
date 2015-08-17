"""psutils.py: Collect system usage statistics."""

# Import sys and subprocess libraries to call other scripts.
# Import psutil library useful for gathering system usage info.
import sys
import subprocess
import psutil as ps


# Useful message to display when the script is running (for debugging purposes).
print "Collecting info on RAM and CPU: "

# Start collecting system usage statistics using an arbitrarily set range loop:
for x in range(0, 10):
    cpu = ps.cpu_percent(interval=2)
    mem = ps.virtual_memory()
    m = mem.used >> 20
    
    # Assigning log files to variables. 
    memfile = "./logs/memory.txt"
    cpufile = "./logs/cpu.txt"
    # This is done for formatting purposes.
    space = " "
    newline = '\n'
    # Do this to display collected usage every 5 seconds.
    y  = x * 5 
    
    # Write the collected memory usage to the respective log file. 
    openfile = open(memfile, 'a')      
    openfile.write(str(y))
    openfile.write(space)
    openfile.write(str(m))
    openfile.write('\n')
    openfile.close()
    
    # Write the collected CPU usage to the respective log file.
    openfile = open(cpufile, 'a')
    openfile.write(str(y))
    openfile.write(space)
    openfile.write(str(cpu))
    openfile.write('\n')
    openfile.close()
    

# Call graph.py to plot based on the log files.
subprocess.call(['python /home/nestig/monpi/filedata_graph.py'], shell=True)

# Clear the log files after plotting is done.
subprocess.call(['cat /dev/null > /home/nestig/monpi/logs/network.txt'], shell=True)
subprocess.call(['cat /dev/null > /home/nestig/monpi/logs/memory.txt'], shell=True)
subprocess.call(['cat /dev/null > /home/nestig/monpi/logs/cpu.txt'], shell=True)