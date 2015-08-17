"""netcap.py: Captures packets from the network traffic on eth0 interface."""

# Import os.path, subprocess and sys libraries to call other scripts and use system calls.
import subprocess
import sys
import os.path

# Useful message to display when the script is running (for debugging purposes).
print "Monitoring broadcast packets on the network..."

# Start collecting network usage statistics using an arbitrarily set range loop:
for x in range(0, 10): 
    
    # Start capturing with tshark on eth0 interface and write the raw data output to capfile under root. 
    subprocess.call(['sudo tshark -i eth0 -a duration:2 -w /root/capfile'], shell=True)
    
    # Neccessary to move file to different location to avoid root permission problem
    subprocess.call(['sudo mv /root/capfile ./capfile'], shell=True)
    
    # Next 3 lines are calls to process output formatting of network packets captured
    pcap = subprocess.Popen(["sudo", "capinfos", "-yu", "/home/nestig/monpi/capfile"], stdout=subprocess.PIPE)
    lrow = subprocess.Popen(["awk",  "NR==3"], stdin=pcap.stdout, stdout=subprocess.PIPE)
    dbrate = subprocess.Popen (["cut",  "-c22-25"], stdin=lrow.stdout, stdout=subprocess.PIPE)
    
    # Close output stream
    pcap.stdout.close() 
    lrow.stdout.close()

    # Connect PIPE  
    stdout, stderr = dbrate.communicate()

    # To avoid newline
    sys.stdout.write(stdout)

    # The infile will hold the network usage data to server as input file.
    infile = "./logs/network.txt"
    openfile = open(infile, 'a')
    space = " "
    # Collecting data every 5 seconds. 
    y = x * 5
    
    # Write the formatted data to file
    openfile.write(str(y))
    openfile.write(space)    
    openfile.write(stdout)
    openfile.close()	

# Call psutils.py script to collect system usage statistics.
subprocess.call(['python /home/nestig/monpi/psutils.py'], shell=True)
