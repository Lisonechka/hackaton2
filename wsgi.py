from app import app

if __name__ == "__main__":  # Protect this code to be ran if he is imported
    app.run(port=8080, debug=True)
