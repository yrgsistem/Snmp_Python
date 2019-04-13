import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="20252278",
                                  host="192.168.5.10",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM public.playground"
    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchall()

    for row in mobile_records:
        print("Id = ", row[0], )
        print("Model = ", row[1])
        print("Price  = ", row[2], "\n")
except (Exception, psycopg2.Error) as error:
    print("Error", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
