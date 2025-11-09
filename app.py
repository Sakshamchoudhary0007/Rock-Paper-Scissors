from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Game logic API
@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        result = "You Win!"
    else:
        result = "You Lose!"

    return jsonify({
        'user': user_choice,
        'computer': computer_choice,
        'result': result
    })

if __name__ == '__main__':
    app.run(debug=True)
