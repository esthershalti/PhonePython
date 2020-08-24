use pythonDB
INSERT INTO cRoute(WaysName,Cost,MinuteHere,MinuteAbroad) VALUES('kosher',54,2000,1000)
INSERT INTO cRoute(WaysName,Cost,MinuteHere,MinuteAbroad) VALUES('busy',20,2000,1000)
INSERT INTO cRoute(WaysName,Cost,MinuteHere,MinuteAbroad) VALUES('tocman',5,1,2)
INSERT INTO cRoute(WaysName,Cost,MinuteHere,MinuteAbroad) VALUES('govine',21,2,1)

INSERT INTO lines(CustomerCode,CrouteCode,Phone) VALUES(40,1,'0548466119')
INSERT INTO lines(CustomerCode,CrouteCode,Phone) VALUES(60,2,'0542558966')
INSERT INTO lines(CustomerCode,CrouteCode,Phone) VALUES(70,2,'0522235689')
INSERT INTO lines(CustomerCode,CrouteCode,Phone) VALUES(90,1,'0528896598')

INSERT INTO talking(StartDate,EndDate,FromPhone,ToPhone) VALUES('12-10-2000','12-10-2000','0548466119','0542558966')
INSERT INTO talking(StartDate,EndDate,FromPhone,ToPhone) VALUES('12/13/2000','12/12/2000','0542558966','0522235689')
INSERT INTO talking(StartDate,EndDate,FromPhone,ToPhone) VALUES('12/25/2000','12/26/2000','0528896598','0542558966')
INSERT INTO talking(StartDate,EndDate,FromPhone,ToPhone) VALUES('10-01-2000','10-02-2000','0548466119','0522235689')

UPDATE cRoute 
set Cost=Cost*102/100
where Cost<30


select * from talking

select SUM(DATEDIFF(MINUTE,StartDate, EndDate))
from talking t  join lines l  
on t.FromPhone =l.Phone join cRoute c 
on l.CrouteCode= c.CrouteCode
