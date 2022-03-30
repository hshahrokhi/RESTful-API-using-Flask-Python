# -*- coding: utf-8 -*-
"""
@author: Hamed Shahrokhi
"""


#%%Imports
import os
import sys
from flask import Flask
from flask_restful import Api, Resource, reqparse
import yaml
import os
import pyodbc

#%%Database
propertiesFileAddress=os.getcwd()+'/properties.yml'

if not os.path.isfile(propertiesFileAddress):
    print("property file not found")
    os._exit(1)
else: 
    with open(propertiesFileAddress) as f:
        properties=yaml.safe_load(f)
        Database=properties["Database"]["DatabaseName"]
        Server=properties["Database"]["ServerName"]

DatabaseProperties='Driver={SQL Server};'+'Server='+Server+";"+'Database='+Database+";"+'Trusted_Connection=yes;'

#%%Flask App
app = Flask(__name__)
api=Api(app)

customer_args=reqparse.RequestParser()
# customer_args.add_argument("customer_id",type=str,help="id must be provided",required=True)
customer_args.add_argument("customer_name",type=str,help="name must be provided",required=True)
customer_args.add_argument("customer_email",type=str,help="email must be provided",required=True)
customer_args.add_argument("customer_average_purchase",type=int,help="avg purchase must be provided",required=True)

class getClientInfo(Resource):
    def get(self,id):
        conn = pyodbc.connect(DatabaseProperties)
        cursor = conn.cursor()
        query='select * from  [dbo].[CustomerInfo] where customer_id='+"'"+str(id)+"'"
        cursor.execute(query)
        response={}
        for row in cursor:
            response["customer_id"]= str(row[0])
            response["customer_name"]= str(row[1])
            response["customer_email"]= str(row[2])
            response["customer_purchase_history"]= str(row[3])
               
        return response,200
    def put(self,id):
        args=customer_args.parse_args()
        print("put method called")
        conn = pyodbc.connect(DatabaseProperties)
        cursor = conn.cursor()
        query='insert into [dbo].[CustomerInfo] values('+"'"+str(id)+"','"+str(args["customer_name"])+"','"+str(args["customer_email"])+"',"+str(args["customer_average_purchase"])+")"
        print(query)
        cursor.execute(query)
        conn.commit()
        return args,201
    def delete(self,id):
        conn = pyodbc.connect(DatabaseProperties)
        cursor = conn.cursor()
        query='delete from  [dbo].[CustomerInfo] where customer_id='+"'"+str(id)+"'"
        cursor.execute(query)
        conn.commit()
        return 'deletion successful',204
        
api.add_resource(getClientInfo,"/getClientInfo/<string:id>")#


if __name__=="__main__":
    app.run(debug=True)

    




