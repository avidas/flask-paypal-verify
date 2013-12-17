# Flask application to demo accepting payments via PayPal
# using the rest sdk for Python

from flask import Flask, render_template

app = Flask(__name__)

#Get MODE, CLIENT_ID and CLIENT_SECRET from config file
app.config.from_envvar('CONFIG')

@app.route("/")
def credit_card_form():
	return render_template("card.html")

if __name__ == '__main__':
	app.run(debug=True)