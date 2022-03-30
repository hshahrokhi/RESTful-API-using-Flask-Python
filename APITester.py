# -*- coding: utf-8 -*-
"""
@author: Hamed Shahrokhi
"""
import requests

BASEURL="http://127.0.0.1:5000/"
customerIdForGet="customer2"
customerIdForDelete="customer7"
customerIdForPut="customer7"

response=requests.get(BASEURL+"getClientInfo/"+str(customerIdForGet))
print(response.json())


response=requests.delete(BASEURL+"getClientInfo/"+str(customerIdForDelete))
print(response)

response=requests.put(BASEURL+"getClientInfo/customer7",{"customer_name":"customer7_name","customer_email":"customer7@gmail.com","customer_average_purchase":12})
print(response)
