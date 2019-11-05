class Customer:

##       def  __init__(self):
##                self.__cutomerid=0
##                self.__telephoneno=[ ]
        
       def setcustomerid(self,id):
              self.customerid=id

       def  settelephoneno(self,teleno):
              self.telephoneno=teleno

       def getcusttid(self):
               return self.customerid

       def gettelephone(self):
               return self.telephoneno

         

custobj=Customer()
custobj.setcustomerid(1001)
custobj.settelephoneno(9900121234)
print(custobj.getcusttid())
print(custobj.gettelephone())


        

          


































































