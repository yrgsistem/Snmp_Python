import os
from QueryExecuter import querytrigger

class SnmpProtocol:

    def __init__(self,snmpcmd = "snmpwalk -v 2c",username = "-c public",oid = "1.3.6.1.2.1.43.5.1.1.17.1"):
        self.snmpcmd = snmpcmd
        self.username = username
        self.oid = oid



        dbclass = querytrigger()
        sql = "SELECT ip FROM public.ipadresleri"

        records = dbclass.simpleselectquery(sql)

        iplist = []
        self.iplist = iplist

        for record in records:
            iplist.append(record[0])



    def execute(self,ip):
        stmt = os.popen(self.snmpcmd + " " + self.username + " " + ip + " " + self.oid).read()
        print(ip + " : " + stmt)

#snmpprotocol = SnmpProtocol()
#for i in snmpprotocol.iplist:
#    result = snmpprotocol.execute(i)

insert =  querytrigger()
insertsql = "INSERT INTO public.ipadresleri (serino) VALUES (%s)"
data = ('11')
records = insert.insertdeletequery(insertsql, data)
