import json

class Counter:
	i = 0

from pymongo import MongoClient
client = MongoClient("mongodb://hacktech:slo@ds047602.mlab.com:47602/hacktech")
db = client.hacktech
print("Database connection:\n",db, "\n")

'''
db.qa.insert_one(
	{
		"username": "Admin",
		"password": "password"
	}
)
db.qa.insert_one(
	{
		"username": "Admin",
		"category": "social",
		"question": "DTF?",
		"description": "in bed",
		"upvotes": 0,
		"downvotes": 0,
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
		password = request.form['password']
		print(username)
		print(password)
		cursor = db.qa.find({"username": username, "password": password})
		if(cursor.count() == 1):
			return "Found user"
		else:
			return "401: Didn't find user"

#ADD QUESTION
@app.route("/add/", methods=["POST"])
def add():
	username = request.form["username"]
	question = request.form["question"]
	description = request.form["description"]
	category = request.form["category"]
	db.qa.insert_one({"questionId": Counter.i,
			"username": username,
			"category": category,
			"question": question,
			"description": description,
			"upvotes": 0, 
			"downvotes": 0,
			"answers": []})
	Counter.i = Counter.i + 1
	return "Added"

#FIND QUESTION FROM CATEGORY
@app.route("/findCategory/<category>")
def findCategory(category):
	questionList = []
	cursor = db.qa.find({"category": category})
	for document in cursor:
		questionList.append(document)
	dict = {"questions": questionList}
	print(dict)
	return jsonify(dict)

#FIND QUESTION 
#answer question

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

