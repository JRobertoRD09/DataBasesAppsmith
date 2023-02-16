from faker import Faker
import mysql.connector

# Create an instance of Faker
fake = Faker()

# Connect with the database
cnx = mysql.connector.connect(user='user', password='password', host='localhost', database='test')
cursor = cnx.cursor()

# Generates and executes an INSERT INTO statement for each record
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

# Commits the changes and closes the connection
cnx.commit()
cursor.close()
cnx.close()

print("The data insertion was successful!!")