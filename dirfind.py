#!/usr/bin/python
# D1r5 - Dir & Sensitive File Scanner
# Coded By Afrizal F.A - ICWR-TECH
# Write Code ( Python )
import requests, sys

print """
#######################################
#                                     #
# D1r5 - Dir & Sensitive File Scanner #
# Coded By Afrizal F.A - ICWR-TECH    #
#                                     #
#######################################
"""

if sys.argv[1] == "-h":
    print "Help\n"
    print "$ ./" + sys.argv[0] + " http://urlwebsite.com"
    print "\nPlease using http:// or https://"
    exit()

direktori_scan = open("list.txt").read()
pisahurl = direktori_scan.split("\n")
print "\n[+] Scanning......\n"
for url_raw in pisahurl:
    if not url_raw:
        continue
    url = sys.argv[1] + "/" + url_raw
    cek = requests.get(url)
    res = cek.status_code
    if res == int(200):
        result = "[+] " + url + " ( 200 ) => OK"
        print result
        lanjut = raw_input("[?] Enter For Next Scan, Or Type 'exit' For Exit : ")
        if lanjut == str("exit"):
            print "\nResult Scanning, "
            print result
            exit()
    else :
        print "[-] " + url + " (" , res, ") => Not Valid"
print "\nResult Scanning, "
print result
