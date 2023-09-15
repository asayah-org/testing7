from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/data', methods = ['GET'])
def ReturnJSON():
	if(request.method == 'GET'):
		data = {
			"server" : "testing7",
			"msg" : "hi",
		}

		return jsonify(data)

if __name__=='__main__':
	 app.run(debug=True, port=8080)
