#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1


def findAdmin():
        f = open("link.txt","r");
        link = raw_input("Site ismi gir \n(ex : site panel vur SOAYHG ): ")
        print "\n\nAvilable links : \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "OK => ",req_link

def Credit():
        Space(9); print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
        Space(9); print "@    Python Kelleci / SOAYHG        @"
        Space(9); print "@    Onurex Özel Saldırı Takımı     @"
        Space(9); print "@    Onurex Ethical Hacker Ekibi    @"
        Space(9); print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

Credit()
findAdmin()