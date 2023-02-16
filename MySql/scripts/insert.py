from faker import Faker
import mysql.connector

# Crea una instancia de Faker
fake = Faker()

# Conecta con la base de datos
cnx = mysql.connector.connect(user='user', password='password', host='localhost', database='test')
cursor = cnx.cursor()

# Genera y ejecuta una declaración INSERT INTO para cada registro
for i in range(1000):
    username = fake.user_name()
    email = fake.email()
    age = fake.random_int(min=18, max=80)
    bio = fake.text()
    avatar = None
    is_active = fake.boolean()
    data = '{"key": "value"}'
    salary = fake.random_int(min=30000, max=100000)
    
    query = "INSERT INTO users (username, email, age, bio, avatar, is_active, created_at, data, salary) VALUES (%s, %s, %s, %s, %s, %s, NOW(), %s, %s)"
    values = (username, email, age, bio, avatar, is_active, data, salary)
    
    cursor.execute(query, values)

# Hace commit de los cambios y cierra la conexión
cnx.commit()
cursor.close()
cnx.close()
