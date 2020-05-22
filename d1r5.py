print("""
 /$$$$$$$    /$$             /$$$$$$$ 
| $$__  $$ /$$$$            | $$____/ 
| $$  \ $$|_  $$    /$$$$$$ | $$      
| $$  | $$  | $$   /$$__  $$| $$$$$$$ 
| $$  | $$  | $$  | $$  \__/|_____  $$
| $$  | $$  | $$  | $$       /$$  \ $$
| $$$$$$$/ /$$$$$$| $$      |  $$$$$$/
|_______/ |______/|__/       \______/ 
======================================
[*] D1r5 - R&D ICWR
--------------------------------------
[*] Dir & Sensitive File Scanner
======================================
""")

import sys, requests
from random import randint
from threading import Thread
from time import sleep as delay

class d1r5:

    def useragent(self):

        arr=["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3","Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16","Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
        return arr[randint(0,len(arr)-1)]

    def check_code(self, xurl):

        try:

            resp = requests.get(url=xurl, headers={ "User-Agent": self.useragent() }, timeout=5)

            if resp.status_code == 200:

                print("[+] Found : {}".format(xurl))

            else:

                print("[-] Not Found : {}".format(xurl))

        except:

            print("[-] Error : {}".format(xurl))

    def __init__(self):

        if len(sys.argv)>2:

            for x in open(sys.argv[2], errors='ignore').read().split("\n"):

                if x != '':

                    Thread(target=self.check_code, args=("{}/{}".format(sys.argv[1], x), )).start()
                    delay(0.1)

        else:

            print("[-] Invalid Option")

if __name__ == "__main__":
    
    d1r5()
