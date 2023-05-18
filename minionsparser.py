#!/usr/bin/python3
# 
# Description: This script normalizes the data contained in the file published by Binary Edge at
# https://api.binaryedge.io/v1/minions into a format that can be consumed as an EDL by the Palo Alto NGFW
# 
# The script downloads the contents of the file "minions" from the above ULR and then strips the following 
# characters:
#
# 1. From the first line  
#
#          {"scanners":[ "
#
# is eliminated before the first IP Address in the file
#
# 2. Each instance of 
#
#           ", ") 
#
# is replaced by a newline
# 
# 3. The characters
#
#            "]}
#
# Are removed from the last IP Address in the file
#
# Support Policy
# 
# This script is provided under an as-is, best effort, support policy. 
# These scripts should be seen as community supported and Palo Alto Networks will 
# contribute our expertise as and when possible. We do not provide technical support or
# help in using or troubleshooting the components of the project through our normal support 
# options such as Palo Alto Networks support teams, or ASC (Authorized Support Centers) 
# partners and backline support options. 
#
# The underlying product used (the NGFW and EDLs) by the scripts is still supported, 
# but the support is only for the product functionality and not for help in deploying or using the template 
# or script itself. 
#
#
# Open the file and read it into a buffer
# input = open("./minions", "r")
# data = input.read()

# Retrieve contents of the file and store the string in a buffer 
import requests
link = "https://api.binaryedge.io/v1/minions"
f = requests.get(link)

# Replace characters as mentioned above
data2 = f.text.replace("{\"scanners\":[ \"", "\n")
data3 = data2.replace("\"]}", "\n")
newdata = (data3.replace("\", \"", "\n")) 

# Open the file minions.edl.txt in the tmp directory and write the newly formatted data.  
output = open("/tmp/minionsparser/minions.edl.txt", "w")
output.writelines(newdata)

# Close the file
output.close()