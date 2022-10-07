
from asyncio import constants
import json
from flask import Flask, redirect, url_for, request,render_template,Request,jsonify,make_response
app = Flask(__name__)


@app.route('/biz', methods=[ 'GET'])
def business():
	if request.method == 'GET':
		keyword = request.args.get('keyw')
		newresp = {
			"name": "John",
			"age": 30,
			"city": "New York"
			}
		jsondata = json.dumps(newresp)
		print(jsondata)
		return render_template('biz.html',data = jsondata)
	


if __name__ == '__main__':
	app.run(debug=True)
