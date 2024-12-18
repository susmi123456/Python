users=[{"id":1,"name":"trunnett0","email":"jparradice0@newsvine.com","gender":"Non-binary"},
{"id":2,"name":"eviegas1","email":"chorley1@creativecommons.org","gender":"Male"},
{"id":3,"name":"mmacinerney2","email":"waizik2@hud.gov","gender":"Male"},
{"id":4,"name":"jmccahey3","email":"ggalley3@issuu.com","gender":"Male"},
{"id":5,"name":"gaddyman4","email":"cperren4@senate.gov","gender":"Bigender"},
{"id":6,"name":"oashplant5","email":"sroath5@xrea.com","gender":"Male"},
{"id":7,"name":"jwardel6","email":"mdarby6@hatena.ne.jp","gender":"Female"},
{"id":8,"name":"wsprigg7","email":"lmiebes7@telegraph.co.uk","gender":"Female"},
{"id":9,"name":"wwiszniewski8","email":"lemburey8@macromedia.com","gender":"Female"},
{"id":10,"name":"jwillers9","email":"ggiacoboni9@51.la","gender":"Male"},
{"id":11,"name":"jgreenroda","email":"lhullaha@mozilla.org","gender":"Female"}]



for user in users:
    print(user.get('name'),user.get('id') ,user.get('email'),(user.get('gender')))