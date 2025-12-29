
import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [endpoint]);

  // Get all unique keys for table header
  const allKeys = Array.from(
    activities.reduce((keys, item) => {
      Object.keys(item).forEach(k => keys.add(k));
      return keys;
    }, new Set())
  );

  return (
    <div className="container mt-4">
      <div className="card shadow">
        <div className="card-body">
          <h2 className="card-title mb-4 text-primary">Activities</h2>
          {activities.length > 0 ? (
            <div className="table-responsive">
              <table className="table table-striped table-hover align-middle">
                <thead className="table-dark">
                  <tr>
                    {allKeys.map(key => (
                      <th key={key}>{key.charAt(0).toUpperCase() + key.slice(1)}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {activities.map((activity, idx) => (
                    <tr key={activity.id || idx}>
                      {allKeys.map(key => (
                        <td key={key}>{activity[key]}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="alert alert-info">No activities found.</div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Activities;
