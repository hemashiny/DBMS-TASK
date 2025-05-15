from flask import Flask, request, jsonify
import sqlite3
import random

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('gold_data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_gold_prices', methods=['GET'])
def get_gold_prices():
    year = request.args.get('year')
    conn = get_db_connection()
    prices = conn.execute('SELECT month, price FROM gold_prices WHERE year = ?', (year,)).fetchall()
    conn.close()
    return jsonify([{ "month": row["month"], "price": row["price"] } for row in prices])

@app.route('/get_ornaments', methods=['GET'])
def get_ornaments():
    conn = get_db_connection()
    ornaments = conn.execute('SELECT name, price, grams FROM gold_ornaments').fetchall()
    conn.close()
    return jsonify([{ "name": row["name"], "price": row["price"], "grams": row["grams"] } for row in ornaments])

@app.route('/predict_price', methods=['GET'])
def predict_price():
    conn = get_db_connection()
    prices = conn.execute('SELECT year, AVG(price) as avg_price FROM gold_prices WHERE year IN (2022, 2023, 2024) GROUP BY year').fetchall()
    conn.close()
    avg_prices = [row["avg_price"] for row in prices]
    predicted_price = sum(avg_prices) / len(avg_prices) * (1 + random.uniform(0.05, 0.15))  # 5-15% rise
    explanation = f"The predicted price for 2025 is based on the average price from 2022 to 2024, with an expected market increase of 5-15% due to inflation and demand."
    return jsonify({ "predicted_price": round(predicted_price, 2), "explanation": explanation })

if __name__ == '__main__':
    app.run(debug=True)
