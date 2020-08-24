create database ezer
go
use ezer
go
create table customerEzer
(
CustomerCode  int primary key identity(0,10),
CustomerId varchar(9),
CustomerName varchar(20),
CustomerLast varchar(20),
CustomerAdress varchar(40),
CustomerCountry varchar(20)
)
create table cRouteEzer
(
RouteCode int primary key identity(1,1),
RouteName varchar(25),
RouteCost int,
MinitRouteHere int,
MinitRouteBroad int
)
create table lineEzer
(
LineCode  int identity(100,10)primary key,
CustomerCode int foreign key references customerEzer(CustomerCode),
RouteCode int foreign key references cRouteEzer(RouteCode),
LineFone varchar(10) unique
)
create table talkingEzer(
TalkinCode int primary key identity(1,1),
StartDate date,
EndDate date,
OneFhone varchar(10) foreign key references lineEzer(LineFone),
SecondFhone varchar(10) foreign key references lineEzer(LineFone)
)
INSERT customerEzer(CustomerId,CustomerName,CustomerLast,CustomerAdress,CustomerCountry) VALUES('111','esther','shalti','abc','IL')
INSERT customerEzer(CustomerId,CustomerName,CustomerLast,CustomerAdress,CustomerCountry) VALUES('222','rr','we','et','u')
INSERT customerEzer(CustomerId,CustomerName,CustomerLast,CustomerAdress,CustomerCountry) VALUES('333','ff','se','ss','s')
INSERT customerEzer(CustomerId,CustomerName,CustomerLast,CustomerAdress,CustomerCountry) VALUES('444','ss','wr','tyh','w')
