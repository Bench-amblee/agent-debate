import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [apiStatus, setApiStatus] = useState('Checking...');

  useEffect(() => {
    // Test connection to backend
    fetch('http://localhost:8000/health')
      .then(res => res.json())
      .then(data => {
        setApiStatus(`Backend connected! Status: ${data.status}`);
      })
      .catch(err => {
        setApiStatus('Backend not running');
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>🎭 Debate Arena</h1>
        <p>{apiStatus}</p>
        <p>Setup complete! Ready for hackathon tomorrow.</p>
      </header>
    </div>
  );
}

export default App;