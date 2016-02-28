import json 
import time
import pymongo

class Counter:
	i = 0

from pymongo import MongoClient
client = MongoClient("mongodb://hacktech:slo@ds047602.mlab.com:47602/hacktech")
db = client.hacktech
print("Database connection:\n",db, "\n")

'''
db.qa.insert_one(
	{
		"userID": "timchu",
		"password": "password",
		"name": "Timothy Chu",
		"reputation": str(9999),
		"categories": ["Math", "Computer Science", "Science"]
	}
)
db.qa.insert_one(
	{
		"username": "Admin",
		"category": "social",
		"question": "DTF?",
		"description": "in bed",
		"upvotes": str(0),
		"downvotes": str(0),
		"answers": []
	}
)
'''

from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

#LOGIN
@app.route("/login/", methods=["POST"])
def login():
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		print(username)
		print(password)
		cursor = db.qa.find_one({"userID": username, "password": password})
		if cursor is None:
			return "401: Didn't find user"
		else:
			
			dictionary = {"username": username,
				"name": cursor["name"], 
				"reputation": str(cursor["reputation"])}
			return json.dumps(dictionary)

#SUBSCRIBE
@app.route("/subscribe/<username>", methods=["POST"])
def subscribeCategory(username):
	dictionary = db.qa.find_one({"userID": username})
	subscriptionList = dictionary["categories"]
	subscriptionList.append(request.form["category"])
	dictionary["answers"] = subscriptionList
	db.qa.update_one({"userId": username}, 
			{"$set": {"answers": subscriptionList}})
	return "Subscribing"

#ADD QUESTION
@app.route("/add/", methods=["POST"])
def addQuestion():
	username = request.form["username"]
	question = request.form["question"]
	description = request.form["description"]
	category = request.form["category"]
	db.qa.insert_one({"questionId": str(Counter.i),
			"time": time.time(),
			"username": username,
			"category": category,
			"question": question,
			"description": description,
			"upvotes": str(0), 
			"downvotes": str(0),
			"answers": []})
	Counter.i = Counter.i + 1
	return "Added question to DB"

#FIND QUESTION FROM CATEGORY
@app.route("/findCategory/<category>")
def findCategory(category):
	questionList = []
	cursor = db.qa.find({"category": category})
	cursor = cursor.sort([["time", pymongo.DESCENDING]])
	for document in cursor:
		questionList.append(document)
	dictionary = {"questions": questionList}
	print (type(dictionary))
	return str(dictionary)

#FIND QUESTION 
@app.route("/findQuestion/")
def findQuestion():
	questionList = []
	cursor = db.qa.find()
	for document in cursor:
		questionList.append(document)
	print(questionList[2])
	return str(questionList[2])

#ANSWER QUESTION/POST REPLY
@app.route("/answerQuestion/<int:questionId>", methods=["POST"])
def answerQuestion(questionId):
	dictionary = db.qa.find_one({"questionId": questionId})
	print(dictionary)
	answersList = dictionary["answers"]
	answersList.append(request.form["answer"])
	dictionary["answers"] = answersList
	db.qa.update_one({"questionId": questionId}, 
			{"$set": {"answers": answersList}})
	return "Answering"






@app.route("/profile/<int:post_id>")
def profile(post_id):
	return "Profile id %s" % post_id

@app.route("/getpost", methods=["GET", "POST"]) 
def getpost():
	if request.method == "POST":
		return "You are using POST"
	else:
		return "You are using GET"

if __name__ == "__main__":
	app.run(debug=True)

