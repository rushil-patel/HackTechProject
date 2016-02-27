from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World: %s" % request.method

@app.route("/inbed")
def inbed():
	return "Your mom"

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
