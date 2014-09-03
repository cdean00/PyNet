"""
Week 4, Excersise 2
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
II. Parse the below 'show version' data and obtain the following items (vendor, model, os_version, uptime, and serial_number).  Try to make your string parsing generic i.e. it would work for other Cisco IOS devices. 



The following are reasonable strings to look for:

'Cisco IOS Software' for vendor and os_version

'bytes of memory' for model

'Processor board ID' for serial_number

' uptime is ' for uptime



Store these variables (vendor, model, os_version, uptime, and serial_number) in a dictionary.  Print the dictionary to standard output when done.

Note, "Cisco IOS Software...Version 15.0(1)M4...(fc1)" is one line.
"""

#Global variables
device = {'vendor':'','model':'','os_version':'','uptime':'','serial_number':''}

show_version_output = open('show_version_output.txt', 'r')

for line in show_version_output:
    if "Cisco IOS Software" in line:
        #Parsing for vendor
        sections = line.split(',')
        words = sections[0].split(' ')
        device['vendor'] = words[0]
        
        #Parsing for os version
        sections = line.split(',')
        words = sections[2].split(' ')
        device['os_version'] = words[2]

    #Parsing for uptime    
    if "uptime" in line:
        device['uptime'] = line[(line.find("uptime is"))+10:(line.find('\n'))]

    #Parsing for model
    if "bytes of memory" in line:
        words = line.split(' ')
        device['model'] = words[1]

    #Parsing for serial number
    if "Processor board ID" in line:
        words = line.split(' ')
        device['serial_number']
            
print device