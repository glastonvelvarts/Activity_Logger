from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy import func
from flask_cors import CORS

import os  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:root@localhost:5432/flask_database'
)
CORS(app)

#creating a database model for activity logs this is step 1

db = SQLAlchemy(app)
class ActivityLog(db.Model):
    __tablename__ = 'activity_logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(50), nullable=False)
    activity = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    extra_metadata = db.Column(db.JSON, nullable=True)

#helps in posting new activity

@app.route('/logs', methods=['POST'])
def create_log():
    data = request.get_json()
    try:
        new_log = ActivityLog(
            user_id=data['user_id'],
            activity=data['activity'],
            timestamp=data.get('timestamp', datetime.datetime.utcnow()),
            extra_metadata=data.get('metadata', {})
        )
        db.session.add(new_log)
        db.session.commit()
        return jsonify({'message': 'Log created successfully'}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500



#Getting logs for specific user just by passing user_id query parameter

@app.route('/logs/<user_id>', methods=['GET'])
def get_logs(user_id):
    from datetime import timedelta
    filter_activity = request.args.get('activity')
    start_date = datetime.datetime.utcnow() - timedelta(days=7)

    query = ActivityLog.query.filter(ActivityLog.user_id == user_id, ActivityLog.timestamp >= start_date)
    if filter_activity:
        query = query.filter(ActivityLog.activity == filter_activity)

    logs = query.all()
    result = [{'id': log.id, 'user_id': log.user_id, 'activity': log.activity, 'timestamp': log.timestamp, 'extra_metadata': log.extra_metadata} for log in logs]
    return jsonify(result)

@app.route('/logs/stats', methods=['GET'])
def get_stats():
    start = request.args.get('start')
    end = request.args.get('end')

    try:
        if not start or not end:
            return jsonify({'error': 'Start and end dates are required'}), 400

        start_date = datetime.datetime.fromisoformat(start)
        end_date = datetime.datetime.fromisoformat(end)
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid date format. Use ISO 8601 format (YYYY-MM-DDTHH:MM:SS)'}), 400

    user_activity_count = db.session.query(ActivityLog.user_id, db.func.count(ActivityLog.id)).\
        filter(ActivityLog.timestamp.between(start_date, end_date)).\
        group_by(ActivityLog.user_id).all()

    most_frequent_activity = db.session.query(ActivityLog.activity, db.func.count(ActivityLog.activity)).\
        filter(ActivityLog.timestamp.between(start_date, end_date)).\
        group_by(ActivityLog.activity).order_by(db.func.count(ActivityLog.activity).desc()).first()

    return jsonify({
        'user_activity_count': {user_id: count for user_id, count in user_activity_count},
        'most_frequent_activity': most_frequent_activity[0] if most_frequent_activity else None
    })




#running the app
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)