import json

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
'''

#cursor = db.qa.find({"username": username, "password": password})

from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

@app.route("/login/", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		data = request.data
		json = request.json['password']
		print(data)
		print(json["username"])
		return data

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
