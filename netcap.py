import subprocess
import sys
import os.path
import psutil

print "Monitoring broadcast packets on the network..."

# loop range set arbitrarily for testing
for x in range(0, 10): 

    subprocess.call(['sudo tshark -i eth0 -a duration:2 -w /root/capfile'], shell=True)
    # moving file to different location to avoid root permission problem
    subprocess.call(['sudo mv /root/capfile /home/nestig/monpi/capfile'], shell=True)
    # next 3 lines are calls to process output formatting of packets captured
    pcap = subprocess.Popen(["sudo", "capinfos", "-yu", "/home/nestig/monpi/capfile"], stdout=subprocess.PIPE)
    lrow = subprocess.Popen(["awk",  "NR==3"], stdin=pcap.stdout, stdout=subprocess.PIPE)
    dbrate = subprocess.Popen (["cut",  "-c22-25"], stdin=lrow.stdout, stdout=subprocess.PIPE)
    pcap.stdout.close() # close output stream
    lrow.stdout.close()  # close output stream
    stdout, stderr = dbrate.communicate() # connects PIPE
    sys.stdout.write(stdout) # no newline bullshit
    infile = "/home/nestig/monpi/logs/network.txt" # path to the input file to be modified
    openfile = open(infile, 'a')
    space = " " 
    y = x * 5	# holds approximate intervals
    
    # write the formatted data to file
    openfile.write(str(y))
    openfile.write(space)    
    openfile.write(stdout)
    openfile.close()	

# call psutils.py to get memory and cpu stats
subprocess.call(['python /home/nestig/monpi/psutils.py'], shell=True)
