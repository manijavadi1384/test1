from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("دریافت شد:", data)  # پیام‌ها و کلیک دکمه را چاپ می‌کند
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
