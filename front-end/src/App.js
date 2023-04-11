import React, { useState } from 'react';

function App() {
  const [formData, setFormData] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const requestOptions = {
      methods: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ data: formData })
    };
    const response = await fetch('/api/data', requestOptions);
    const data = await response.json();
    console.log(data);
  };

  const handleChange = (event) => {
    setFormData(event.target.value);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Input data:
          <input type="text" value={formData} onChange={handleChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
