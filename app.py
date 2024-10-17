from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def calculate_days_until_50(birthday):
    # Convert the birthday string to a datetime object
    try:
        birthday_date = datetime.strptime(birthday, '%Y-%m-%d')
    except ValueError:
        return None  # Invalid date format

    # Calculate the 50th birthday date
    fifty_date = datetime(birthday_date.year + 50, birthday_date.month, birthday_date.day)
    today = datetime.today()

    # Calculate the number of days until the 50th birthday
    days_until_50 = (fifty_date - today).days
    return days_until_50 if days_until_50 > 0 else 0  # Ensure it doesn't return negative days

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    # Check if the 'birthday' field is present
    if not data or 'birthday' not in data:
        return jsonify({'error': 'Missing birthday field'}), 400

    birthday = data['birthday']
    days_until_50 = calculate_days_until_50(birthday)

    if days_until_50 is None:
        return jsonify({'error': 'Invalid date format'}), 400

    return jsonify({'days': days_until_50})

if __name__ == '__main__':
    app.run(debug=True)
