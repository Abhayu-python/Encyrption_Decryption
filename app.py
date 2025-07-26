from flask import Flask, render_template, request
import base64

app = Flask(__name__)

def encrypt(text):
    # Using Base64 for simplicity
    text_bytes = text.encode('utf-8')
    encoded = base64.b64encode(text_bytes)
    return encoded.decode('utf-8')

def decrypt(encoded_text):
    try:
        text_bytes = base64.b64decode(encoded_text)
        return text_bytes.decode('utf-8')
    except Exception:
        return "❌ Invalid encrypted input."

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    text = request.form.get("text")
    action = request.form.get("action")

    if action == "encrypt":
        result = encrypt(text)
    elif action == "decrypt":
        result = decrypt(text)
    else:
        result = "❌ Invalid action selected."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
