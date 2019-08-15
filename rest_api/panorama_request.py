import requests

ip_addr  = "192.168.135.200"
username = "admin"
password = "admin"
verify = False

resp = requests.get("https://"+ip_addr+"/api/?type=keygen&user="+username+"&password="+password, verify=verify)
r = resp.text
key = r[r.find("<key>")+5:r.find("</key>")]

resp = requests.get("https://"+ip_addr+"/api?type=config&action=show&key="+key+"&xpath=/config", verify=verify)
r = resp.text
content = r[r.find("<result>")+8:r.find("</result>")]
with open("config.xml", 'w') as fp:
    fp.write('<?xml version="1.0"?>\n')
    fp.write(content)


