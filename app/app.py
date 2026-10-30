from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Support Service</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}

            .card {{
                background: white;
                width: 500px;
                padding: 35px;
                border-radius: 14px;
                box-shadow: 0 4px 18px rgba(0,0,0,0.12);
            }}

            h1 {{
                margin-top: 0;
                color: #1f2937;
            }}

            .status {{
                color: green;
                font-weight: bold;
            }}

            .info {{
                margin-top: 20px;
                line-height: 1.8;
            }}

            .version {{
                margin-top: 25px;
                font-size: 14px;
                color: #6b7280;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h1>DevOps Support Service</h1>

            <p class="status">Service Status: Running</p>

            <div class="info">
                <p><strong>Support Contact:</strong> support@example.com</p>
                <p><strong>Service Hours:</strong> 8:00 AM - 4:00 PM</p>
                <p><strong>Environment:</strong> Internal Lab Service</p>
            </div>

            <div class="version">
                Application Version: {VERSION}
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        version=VERSION
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
