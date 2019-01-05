![image](https://www.dropbox.com/s/zyuttvv6t3vb6o3/Screenshot%2019-01-05%17.55.11.png)

# Get your money back from a card that doesn't allow transferring the money out

## Steps to get working:
1. Install the dependencies with the below command.
```
pip install flask python-dotenv stripe
```
1. Create a stripe account and add the keys to the .env file in the below format. Note that you must also include your desired currency (lower case).
```
STRIPE_KEY=secret_key_here
STRIPE_PUBLISHABLE=stripe_publishable_here
CURRENCY=your_currency_here
```
2. Start the server by typing python `app.py`
3. Open `localhost:5000` in your browser and follow the prompts!
4. Get your money back!
