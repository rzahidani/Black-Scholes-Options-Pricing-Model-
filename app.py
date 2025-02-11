from flask import Flask, render_template, request 
from black_scholes_formula import black_scholes_formula 
from fetch_data import get_stock_data 
''' Flask allows developers to create web applications with just some lines of code: 
    - allows interface with web servers 
    - built-in development server + debugger 
    - allows for dynamic HTML rendering 
    - extensive documentation + community support 
'''
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    option_price = None
    error_message = None 

    if request.method == "POST": 
        try: 
            ticker = request.form["ticker"]
            S, vol = get_stock_data(ticker)
            # Use float for below to express floating-point number with multiple decimal points 
            K = float(request.form["strike"])
            T = float(request.form["time"])
            r = float(request.form["rate"]) 
            option_type = request.form["option_type"]

            option_price = black_scholes_formula(S, K, T, r, vol, option_type) 
        except Exception as e: 
            error_message = str(e) 
        return render_template("index.html", option_price = option_price)
    
    ''' 
        Checks if the script is being run directly and when a Python script is executed directly, Python sets the special variable 
        "__name__" to the string "__main__" and if this condition is true, it means the script is the main program being run and the 
        code inside the if block will be executed 
        
    '''
    if __name__ == "__main__": 
        app.run(debug=True)

       