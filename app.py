# Flask application to demo accepting payments via PayPal
# using the rest sdk for Python

from flask import Flask, render_template, request
import paypalrestsdk

app = Flask(__name__)

#Get MODE, CLIENT_ID and CLIENT_SECRET from config file
app.config.from_envvar('CONFIG')
paypalrestsdk.configure({
	"mode": app.config['MODE'],
	"client_id": app.config['CLIENT_ID'],
	"client_secret": app.config['CLIENT_SECRET']
})

@app.route("/")
def credit_card_form():
	return render_template("card.html")

@app.route("/create_payment", methods=["POST"])
def create_payment():
	'''
	Set indent as sale for immediate payment
	'''
	print request.form
	payment = paypalrestsdk.Payment({
		"intent": "sale",
		"payer": {
			"payment_method": "credit_card",
			"funding_instruments": [{
				"credit_card": {
					"number": request.form["number"],
					"expire_month": request.form["expire_month"],
					"expire_year": request.form["expire_year"],
					"cvv2": request.form["cvv2"]
				}
			}]
		},
		"transactions": [{
			"amount": {
				"total": "12",
				"currency": "USD"
			},
			"description": "creating a direct payment with credit card"
		}]
	})
	if payment.create():
		return "<h1>Payment {0} created successfully</h1>".format(payment.id)
	else:
		return "<h1>Error while creating payment: {0}</h1>".format(payment.error)

if __name__ == '__main__':
	app.run(debug=True)