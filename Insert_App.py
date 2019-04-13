from QueryExecuter import querytrigger

select = querytrigger()
insert = querytrigger()

print(insert.__str__())
print(select.__str__())

sql = "INSERT INTO public.users(id, ad, soyad) VALUES (%s, %s, %s)"
data = ('4','erdogan4','ozturk4')
records = insert.insertdeletequery(sql,data)

selectsql = "SELECT * FROM public.users LIMIT 100"
selectrecords = select.simpleselectquery(selectsql)
liste = []
for selectrecord in selectrecords:
    liste.append(selectrecord[0])
    print(selectrecord)

