from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

@app.route('/snakeai')
def snakeai():
    return render_template('snakeai.html')




if __name__ == "__main__":
    app.run(debug=True, port=3000)

# pip freeze > requirements.txt
# pip install -r requirements.txt (For Python from requirements.txt)

# npm install (for Tailwind from package.json)

# Recompile Tailwind
# npx tailwindcss -i ./static/input.css -o ./static/output.css --watch