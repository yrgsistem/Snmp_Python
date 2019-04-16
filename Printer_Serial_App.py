import os
from QueryExecuter import querytrigger

class SnmpProtocol:

    #snmpwalk -v 2c -c public 10.6.208.80 1.3.6.1.2.1.25.3.2.1.3.1 model number

    def __init__(self,snmpcmd = "snmpwalk -v 2c",username = "-c public",oid = "1.3.6.1.2.1.43.5.1.1.17.1", oid2 = "1.3.6.1.2.1.25.3.2.1.3.1" ):
        self.snmpcmd = snmpcmd
        self.username = username
        self.oid = oid
        self.oid2 = oid2

        dbclass = querytrigger()
        sql = "SELECT ip FROM public.ipadresleri"

        records = dbclass.simpleselectquery(sql)

        iplist = []
        self.iplist = iplist

        for record in records:
            iplist.append(record[0])

    def execute(self,ip):
        stmt = os.popen(self.snmpcmd + " " + self.username + " " + ip + " " + self.oid).read()
        stmt2 = os.popen(self.snmpcmd + " " + self.username + " " + ip + " " + self.oid2).read()

        a = stmt.split('.')
        c = a[-1]
        d = c[c.find("\"")+1: len(c) -2]

        a1 = stmt2.split('.')
        print(a1)
        c1 = a1[-3]
        print(c1)
        d1 = c1[c1.find("\"") + 1: len(c1)]
        print(ip +" : "+d1)

        #qt = querytrigger()
        #updatesql = "UPDATE public.ipadresleri SET serino=%s WHERE ip=%s"
        #data = [d,ip]
        #qt.insertdeletequery(updatesql, data)
        #print("updated")

snmpprotocol = SnmpProtocol()
snmpprotocol.execute("10.6.208.64")
#for i in snmpprotocol.iplist:
#    result = snmpprotocol.execute(i)


#insert =  querytrigger()
#insertsql = "INSERT INTO public.ipadresleri(serino) VALUES (%s)"
#data = ['sonson']
#records = insert.insertdeletequery(insertsql, data)