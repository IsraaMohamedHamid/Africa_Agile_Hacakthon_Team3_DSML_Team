// backend.js
const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/translate', (req, res) => {
  const { text, target_lang } = req.body;

  // Spawn the Python process
  const pythonProcess = spawn('python', ['translate.py', text, target_lang]);

  let translatedText = '';
  pythonProcess.stdout.on('data', (data) => {
    translatedText += data.toString();
  });

  pythonProcess.on('close', (code) => {
    if (code === 0) {
      // Success
      res.json({ translatedText });
    } else {
      // Error
      res.status(500).json({ error: 'Translation failed' });
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
