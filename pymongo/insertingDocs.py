import pymongo
from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb

users = db.users

user1 = {"username":"Leah", "password" : "macbook", "favorite_number" : 9, "hobbies" : ["python", "running", "pizza"]}
user2 = {"username":"Bella", "password" : "macbook", "favorite_number" : 9, "hobbies" : ["sleeping", "eating", "bacon"]}
user3 = {"username":"Snowball", "password" : "macbook", "favorite_number" : 9, "hobbies" : ["attention", "running", "barking"]}

user4 = [{"username":"Natasha", "password" : "macbook", "favorite_number" : 9, "hobbies" : ["painting", "biking", "mingling"]},{"username":"Maryusa", "password" : "macbook", "favorite_number" : 9, "hobbies" : ["bossing", "running", "barking"]}]

user_id = users.insert_one(user1).inserted_id
user_id = users.insert_one(user2).inserted_id
user_id = users.insert_one(user3).inserted_id

inserted = users.insert_many(user4)

user_id

