// backend.js
const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.use(express.json());

app.get('/streamlit', (req, res) => {
  // Spawn the Streamlit process
  const streamlitProcess = spawn('streamlit', ['run', 'text_to_speech_sys.py']);

  streamlitProcess.stdout.on('data', (data) => {
    console.log(`Streamlit output: ${data}`);
  });

  streamlitProcess.stderr.on('data', (data) => {
    console.error(`Streamlit error: ${data}`);
  });

  streamlitProcess.on('close', (code) => {
    console.log(`Streamlit process exited with code ${code}`);
  });

  res.send('Streamlit app is running.');
});

app.listen(port, () => {
  console.log(`Backend server is running on http://localhost:${port}`);
});
