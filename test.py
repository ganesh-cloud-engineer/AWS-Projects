from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Food Website</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background-color: #f4f4f4;
            }
            h1 {
                color: #333;
            }
            .food {
                background: white;
                border-radius: 10px;
                padding: 15px;
                margin: 10px;
                display: inline-block;
                width: 150px;
                box-shadow: 0 0 5px gray;
            }
            button {
                padding: 5px 10px;
                background: orange;
                border: none;
                color: white;
                cursor: pointer;
            }
        </style>
    </head>
    <body>

        <h1>🍔 Ganesh Food Hub</h1>

        <div class="food">
            <h3>Pizza</h3>
            <p>₹200</p>
            <button onclick="alert('Pizza Ordered!')">Order</button>
        </div>

        <div class="food">
            <h3>Burger</h3>
            <p>₹120</p>
            <button onclick="alert('Burger Ordered!')">Order</button>
        </div>

        <div class="food">
            <h3>Pasta</h3>
            <p>₹180</p>
            <button onclick="alert('Pasta Ordered!')">Order</button>
        </div>

        <div class="food">
            <h3>Sandwich</h3>
            <p>₹100</p>
            <button onclick="alert('Sandwich Ordered!')">Order</button>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
