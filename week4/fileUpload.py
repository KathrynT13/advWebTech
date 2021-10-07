from flask import Flask, request
app = Flask(__name__)

@app.route("/display/")
def display():
    start = '<img src="'
    url = url_for('static', filename='uploads/file.png')
    end = '">'
    return start+url+end, 200

@app.route("/upload/", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static.uploads/file.png')
        return "File Uploaded"
    else:
        page = '''
        <html>
        <body>
        <form action="" method="post" name="form" enctype"multipart/form-data">
        <input type="file" name="datafile"/>
        <input type="submit" name="submit" id="submit"/>
        </form>
        </body>
        </html> '''

    return page, 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
