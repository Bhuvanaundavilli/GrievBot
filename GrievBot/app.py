from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

grievances = {
    "hello": "Hi there! How can I assist you today?",
    "refund": "To request a refund, please visit our refund page.",
    "appointment": "To book an appointment, visit our 'Appointments' section.",
    "support": "You can reach our support team at support@example.com."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form.get("msg").lower()
    response = grievances.get(user_input, "Sorry, I didn't understand that. Please try again.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

