from flask import Flask

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index():
	return "Testing Jenkinsfile with Kubernetes!"
	
if __name__ == "__main__":
	app.run(debug=True)
