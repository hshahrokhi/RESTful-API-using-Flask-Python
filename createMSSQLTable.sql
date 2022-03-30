--Create Table----------------------------------------------------------------------------------------
USE [customers]--this is the name of your database; replace if needed
GO

drop table if exists [dbo].[CustomerInfo];

CREATE TABLE [dbo].[CustomerInfo](
	[customer_id] [nchar](50) NOT NULL,
	[customer_name] [nchar](50) NOT NULL,
	[customer_email] [nchar](50) NOT NULL,
	[customer_average_purchase] [int] NOT NULL,
 CONSTRAINT PKCOntraint PRIMARY KEY ([customer_id]));

--Sample data insertion---------------------------------------------------------------------------------------

insert into [dbo].[CustomerInfo] values('customer1','customer1Name','customer1@gmail',10);
insert into [dbo].[CustomerInfo] values('customer2','customer2Name','customer2@gmail',20);
insert into [dbo].[CustomerInfo] values('customer3','customer3Name','customer3@gmail',15);
select * from [dbo].[CustomerInfo];