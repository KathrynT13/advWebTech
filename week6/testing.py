from flask import Flask
app = Flask(__name__)

@app.route('/')
def root:
    return "HELLO WORLD", 200

if __name __ == "__main__":
    app.run(host'0.0.0.0', debug=True)
