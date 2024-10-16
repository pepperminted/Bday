from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def calculate_days_until_50(birthday):
    # Calculate the number of days until the person's 50th birthday
    birthday_date = datetime.strptime(birthday, '%Y-%m-%d')
    fifty_date = datetime(birthday_date.year + 50, birthday_date.month, birthday_date.day)
    today = datetime.today()
    days_until_50 = (fifty_date - today).days
    return days_until_50

@app.route('/calculate', methods=['POST'])
def calculate():
    birthday = request.get_json()['birthday']
    days_until_50 = calculate_days_until_50(birthday)
    return jsonify({'days': days_until_50})

if __name__ == '__main__':
    app.run(debug=True)