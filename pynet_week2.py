"""ip_addr = raw_input("Enter an IP address in: ")

ip_addr_split = ip_addr.split('.')

#Last octect is always 0, assuming /24 networks
if len(ip_addr_split) == 4:
    ip_addr_split[3] = '0'
    
elif len(ip_addr_split) == 3:
    ip_addr_split.append('0')

print ".".join(ip_addr_split) + "\n

first_octect_binary = bin(int(ip_addr_split[0]))
second_octect_binary = bin(int(ip_addr_split[1]))
third_octect_binary = bin(int(ip_addr_split[2]))
fourth_octect_binary = bin(int(ip_addr_split[3]))

#first_octect_hex = hex(int(ip_addr_split[0]))

print "NETWORK_NUMBER FIRST_OCTECT SECOND_OCTECT THIRD_OCTECT FOURTH_OCTECT\n"
print "%s %12 %12s %16s %10s" % (".".join(ip_addr_split), first_octect_binary, second_octect_binary, third_octect_binary, fourth_octect_binary)"""

"""entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"

entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"

entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"

entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

entries = [entry1, entry2, entry3, entry4]

#splitting entry1 - entry4
for i in xrange(0, len(entries)):
    entries[i] = entries[i].split()

print "ip_prefix              as_path"
for i in xrange(0,len(entries)):
    entry = entries[i]
    print "%s %11s %s %s %s %s" % (entry[1], entry[3], entry[4], entry[5], entry[6], entry[7])"""

cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

#split using comma
cisco_ios = cisco_ios.split(',')

#display version 3rd position
cisco_version = cisco_ios[2]

print cisco_version.strip()
