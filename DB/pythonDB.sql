

create database pythonDB
go
use pythonDB
go
create table customer
(
CustomerCode  int primary key identity(0,10),
CustomerId varchar(9),
CustomerName varchar(20),
CustomerLast varchar(20),
CustomerAddress varchar(40),
CustomerCountry varchar(20)
)
create table cRoute
(
CrouteCode int primary key identity(1,1),
WaysName varchar(25),
Cost int,
MinuteHere int,
MinuteAbroad int
)
create table lines
(
LineCode  int identity(100,10)primary key,
CustomerCode int foreign key references customer(CustomerCode),
CrouteCode int foreign key references cRoute(CrouteCode),
Phone varchar(10) unique
)
create table talking(
TalkCode int primary key identity(1,1),
StartDate date,
EndDate date,
FromPhone varchar(10) foreign key references lines(Phone),
ToPhone varchar(10) foreign key references lines(Phone)
)