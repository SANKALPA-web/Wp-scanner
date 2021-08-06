# Wordpress vulnerability scanner
# --Made--by--SankalpaBaral--

import requests
import pyfiglet
text = pyfiglet.figlet_format("WP SCANNER")
print(text)


print("Enter the url without adding https/http\n")

url = input("Enter the target url ")
target = ("https://"+url)

print("Scanning",target+"\n")


a = requests.get("https://"+url+"/xmlrpc.php")
if a.status_code==405:
    print("[!] xmlrpc.php file is enabled\n")
else:
    print("[!] xmlrpc.php file is disabled\n")


b = requests.get("https://"+url+"/wp-json/")
if b.status_code==200:
    print("[!] wp-json file is enabled\n")
else:
    print("[!] wp-json file is disabled\n")

c = requests.get("https://"+url+"/admin")
if c.status_code==200:
    print("[!] Admin pannel is enabled\n")
else:
    print("[!] Admin pannel is disabled\n")

d = requests.get("https://"+url+"/robots.txt")
if d.status_code==200:
    print("[!] Robots.txt file is enabled\n")
else:
    print("[!] Robots.txt is disabled\n")

e = requests.get("https://"+url+"/wp-content/uploads")
if e.status_code==200:
    print("[!] Direcotry travelsal  is enabled\n")
else:
    print("[!]Direcotry travelsal is disabled\n")

e = requests.get("https://"+url+"/sitemap.xml")
if e.status_code==200:
    print("[!] Sitemap.xml file is enabled\n")
else:
    print("[!] Sitemap.xml file is disabled\n")

f = requests.get("https://"+url+"/.htaccess")
if f.status_code==200:
    print("[!] .htaccess file is enabled\n")
else:
    print("[!] .htaccess file is disabled\n")

g = requests.get("https://"+url+"/.gitignore")
if g.status_code==200:
    print("[!] .gitignore file is enabled\n")
else:
    print("[!] .gitignore file is disabled\n")

h = requests.get("https://"+url+"/.log")
if h.status_code==200:
    print("[!] .log file is enabled\n")
else:
    print("[!] .log file is disabled\n")

i = requests.get(target+"/license.txt")
if i.status_code==200:
    print("[!] license.txt file is enabled\n")
else:
    print("[!] license.txt file is disabled\n")


     


