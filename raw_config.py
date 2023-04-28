# Import the requests HTTP module
import requests

# Declare the variable (string) for the URL of leaf1-DC1
url = "https://198.18.250.124/command-api"

# Use the open() function to open the file you just created, "r" means read-only
commands = open("eth7.json", "r")

# The requests method post does an HTTP post with HTTP AUTH_BASIC type credentials. 
# Replace the aristaXXXX with your password. 
# The "data=commands" essentially dumps the contents of eth3.json into the payload of the HTTP post.
# verify=False tells the requests module not to worry about self-signed certificates. 
r = requests.post(url, auth=('admin','Arista123!'), data=commands, verify=False) 

# This simple print statement displays how the switch\'s eAPI responded
print(r.text)