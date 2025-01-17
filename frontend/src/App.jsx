import { useState } from 'react';
import './App.css';

function App() {
  const [userId, setUserId] = useState('');
  const [activity, setActivity] = useState('');
  const [logs, setLogs] = useState([]);
  const [stats, setStats] = useState(null);

  const fetchLogs = async () => {
    try {
      const response = await fetch(`http://localhost:5000/logs/${userId}`);
      const data = await response.json();
      setLogs(data);
    } catch (error) {
      console.error('Error fetching logs:', error);
    }
  };

  const fetchStats = async () => {
    try {
      const response = await fetch(`http://localhost:5000/logs/stats?start=2023-01-01T00:00:00&end=2023-12-31T23:59:59`);
      const data = await response.json();
      setStats(data);
    } catch (error) {
      console.error('Error fetching stats:', error);
    }
  };

  const handleLogSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/logs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: userId, activity }),
      });
      if (response.ok) {
        alert('Activity logged successfully');
        setActivity('');
        fetchLogs();
      }
    } catch (error) {
      console.error('Error submitting log:', error);
    }
  };

  return (
    <div className="container">
      <h1>Activity Logger</h1>
      <form onSubmit={handleLogSubmit} className="log-form">
        <input
          type="text"
          placeholder="User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Activity"
          value={activity}
          onChange={(e) => setActivity(e.target.value)}
          required
        />
        <button type="submit">Log Activity</button>
      </form>
      <button onClick={fetchLogs}>Fetch Logs</button>
      <button onClick={fetchStats}>Fetch Stats</button>
      <div className="logs">
        <ul>
          {logs.map((log) => (
            <li key={log.id}>
              <strong>Activity:</strong> {log.activity} | <strong>Time:</strong> {new Date(log.timestamp).toLocaleString()}
            </li>
          ))}
        </ul>
      </div>
      {stats && (
        <div>
          <h3>Stats</h3>
          <p><strong>Most Frequent Activity:</strong> {stats.most_frequent_activity || 'None'}</p>
          <h4>User Activity Count</h4>
          <ul>
            {Object.entries(stats.user_activity_count).map(([id, count]) => (
              <li key={id}>
                User ID: {id} - Count: {count}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
