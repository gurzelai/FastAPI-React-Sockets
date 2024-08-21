import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  // Estado para guardar el objeto Machine
  const [machines, setMachines] = useState([{ nombre: 'Loading...', valor: 0 }]);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/machines');
    ws.onopen = () => {
      console.log('WebSocket connection opened');
    };

    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        if (Array.isArray(data)) {
          setMachines(data);
        }
      } catch (error) {
        console.error('Error parsing WebSocket message:', error);
      }
    };

    ws.onclose = () => {
      console.log('WebSocket connection closed');
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    return () => ws.close();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>State of the Machines</h1>
        <ul>
          {machines.map((machine, index) => (
            <li key={index}>
              <strong>Name:</strong> {machine.name} <br />
              <strong>Value:</strong> {machine.value}
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
