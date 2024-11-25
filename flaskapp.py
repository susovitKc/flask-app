from flask import Flask, jsonify
from sqlalchemy import create_engine

app = Flask(__name__)

DATABASE_URI = 'mysql+pymysql://user:userpassword@mysql/sampledb'

@app.route('/')
def home():
    try:
        engine = create_engine(DATABASE_URI)
        connection = engine.connect()
        result = connection.execute("SELECT DATABASE();")
        db_name = result.fetchone()[0]
        connection.close()
        return jsonify({'message': f'Connected to MySQL Database: {db_name}'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
