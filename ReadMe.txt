This repo includes the following scrips:

	1. APIService.py: includes the code for the Restful API and and end point
	2. APITester.py: includes sample data for testing the delete, put, and get methods of the API
	3. createMSSQLTable.sql: includes MS SQL scipts to create a table within your database
	4. properties.yml: includes the database server information, base url for API, and base query (you need to chnage it to match your database and server info)


Steps:
	1. Modify the properties.yml to match your system properties (server and database name, etc.)
	2. Run the createMSSQLTable.sql in your MS SQL Management Studio (or any other database management tool you use)
	3. open a command prompt and run the APIService.py using python
	4. run the APITester.py in another command prompt using python