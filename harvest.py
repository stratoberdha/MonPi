import subprocess
import sys
import os.path

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
    infile = "/home/nestig/monpi/input.txt" # path to the input file to be modified
    openfile = open(infile, 'a')
    space = " " 
    y = x * 5	# holds approximate intervals
    
    # write to file the formatted data
    openfile.write(str(y))
    openfile.write(space)    
    openfile.write(stdout)
    openfile.close()	

# display graph
subprocess.call(['python /home/nestig/monpi/filedata_graph.py'], shell=True)


#--------------------------------------------------------OBSOLETE--------------------------------------------------------------
# subprocess.call(['python /home/nestig/monpi/filedata_graph.py'], shell=True)
# os.popen('awk 'NR == 2 {printf "%s", $3} NR == 3 {print " " $4}' /home/nestig/monpi/capfile>>  /home/nestig/monpi/input.txt')
# f=open('/home/nestig/monpi/output.txt', 'r')
# print "Open file output.txt to view broadcast packets captured"
# "-R eth.dst==FF:FF:FF:FF:FF:FF" --destination MAC addr
# "-R ip.dst=192.168.1.100" --destination IP addr

