import os
from flask import Flask, render_template, request
import stripe
import settings

# Setup 

stripe_keys = {
    'secret_key': os.getenv('STRIPE_SECRET'),
    'publishable_key': os.getenv('STRIPE_PUBLISHABLE')
}

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

# Routes et al.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pay')
def pay():
    return render_template('pay.html', key=stripe_keys['publishable_key'], amount=request.args['amount'])

@app.route('/charge', methods=['POST'])
def charge():
    # Amount in cents
    amount = request.form.get('amount')

    customer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency=os.getenv('CURRENCY'),
        description='Just getting my money back ;)'
    )

    return render_template('charge.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)
