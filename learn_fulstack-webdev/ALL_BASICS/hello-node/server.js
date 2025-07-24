const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());

app.get('/', (req, res) => {
    res.json('node node nodeJSSS');
});

app.listen(5000, () => {
    console.log('Example app listening on port 5000!');
});