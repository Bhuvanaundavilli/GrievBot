from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

grievances = {
    "hello": "Hi there! How can I help you today?",
    "refund": "To request a refund, please fill the refund form on our website.",
    "appointment": "To book an appointment, go to the 'Appointments' section.",
    "support": "Our support team can be reached at support@example.com.",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"].lower()
    response = grievances.get(user_input, "Sorry, I didn't understand that. Please try again.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
