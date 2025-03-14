from flask import Flask

app = Flask(__name__)


@app.route("/health")
def health_check():
    return {"status": "healthy"}, 200


@app.route("/book", methods=["POST"])
def create_book():
    # Placeholder for book creation logic
    return {"message": "Book created successfully"}, 201


if __name__ == "__main__":
    app.run(debug=True)
