# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 15:51:14 2020

@author: gp
"""

class mapofauthorbook:
    
    def _init_(self):
        self.value=""
    def addbook(self,val):
        if(self.value==""):
            self.value=val
        else:
            self.value=self.value+","+val
    def retbooks(self):
        if(self.value==""):
            return "no book"
        else:
            c=[]
            for a in self.value.split(','):
                c.append(a)
            return c;
        