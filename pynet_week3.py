import sys

#global variables
ip_addr = []
binary_ip_addr = []

#checks if command line argument was given
if len(sys.argv) > 1:
    args = sys.argv
    ip_addr = args[1]
else:
    ip_addr = raw_input("Please enter an IP address: ")

#splitting ip_address according to '.'"
ip_addr = ip_addr.split(".")

#Checks if entered IP address is 2 or less octects long. If so asks to re-enter IP address to until 3 or 4 octects long.
if len(ip_addr) <= 2 and type(ip_addr) == list:
    while len(ip_addr) <= 2:
        ip_addr = raw_input("Re-enter an IP address: ")
        ip_addr = ip_addr.split(".")

#Mandatory 3 octes. If 4th octet is left off appends 0 for 4th"
if len(ip_addr) == 3:
    ip_addr.append(str(0))

#Converts each octect to binary
for i in xrange(0,len(ip_addr)):
    binary_ip_addr.append(bin(int(ip_addr[i])))
    binary_ip_addr[i] = binary_ip_addr[i].lstrip('0b')

    #Adding leading zeros to pad each binary number so each output is 8-bit
    while len(binary_ip_addr[i]) < 8:
        binary_ip_addr[i] = "0" + binary_ip_addr[i]

#Joining strings back together using a period
binary_ip_addr = ".".join(binary_ip_addr)
ip_addr = ".".join(ip_addr)

print "IP Address    Binary"
print "%-13s %s" % (ip_addr, binary_ip_addr)


