#!/usr/bin/python
# D1r5 - Dir & Sensitive File Scanner
# Coded By Afrizal F.A - ICWR-TECH
# Copyright (c)2019 - Afrizal F.A ( ICWR-TECH )
# Write Code ( Python )

print("""
#######################################
#                                     #
# D1r5 - Dir & Sensitive File Scanner #
# Coded By Afrizal F.A - ICWR-TECH    #
# Super Faster                        #
#                                     #
#######################################
""")

import sys,random,requests
from threading import Thread

class scanner:
    def __init(self):
        pass

    def user_agent(self):
        arr=["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3","Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16","Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
        return arr[random.randint(0,len(arr)-1)]

    def check(self,xurl):
        try:
            cek=requests.get(url=xurl,headers={"User-Agent":self.user_agent()})
            if cek.status_code == int(200):
                print("[+] %s ( %s ) => OK"%(xurl,str(cek.status_code)))
            else :
                print("[-] %s ( %s ) => Not Valid"%(xurl,str(cek.status_code)))
        except:
            print("[-] %s ( %s ) => Network Error"%(xurl,str(cek.status_code)))

x=scanner()
if len(sys.argv)>1:
    direktori_scan=open("list.txt").read()
    pisahurl = direktori_scan.split("\n")
    print("[+] Scanning......\n")
    for path in pisahurl:
        if not path:
            continue
        Thread(target=x.check,args=(sys.argv[1]+"/"+path,)).start()
    
else:
    print("[*] Help\n")
    print("[?] $ ./" + sys.argv[0] + " http://urlwebsite.com")
    print("\n[*] Please using http:// or https://")
