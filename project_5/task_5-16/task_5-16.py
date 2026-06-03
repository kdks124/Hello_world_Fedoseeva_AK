import psycopg2
connection = None
cursor = None
try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="example",
        database="testdb"
    )
    print(" Подключение к базе данных прошло успешно!")
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM products;")
    product = cursor.fetchall()
    for item in product:
        print(f"Товар: {item[0]} {item[1]}")
except Exception as error:
    print(f" Ошибка: {error}")
finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print(" Соединение с базой данных закрыто.")