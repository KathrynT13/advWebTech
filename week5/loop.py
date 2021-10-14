from flask import Flask, render_template
app = Flask(__name__)

@app.route('/users/')
def users():
    names = ['kate', 'louise', 'anna', 'chloe']
    return render_template('loops.html', names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
