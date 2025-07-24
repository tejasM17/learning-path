// GET - Get information from the server
// POST - create ne server
// PUT - Update information on the server
// DELETE - Delete information on the server

const express = require('express');
const app = express();
const connectDB = require('./config/db');

// Connect to database but don't wait for it
connectDB().catch(err => {
  console.error('Database connection error:', err.message);
});

app.use(express.json());

app.use('/products', require('./controllers/products'));
app.use('/users', require('./controllers/users'));
app.use('/about', require('./controllers/about'));
app.use('/books', require('./controllers/books'));

app.get('/', (_req, res) => {
    res.json({ message: "Welcome to the Node API!" });
});



app.get('/users', (_req, res) => {
    res.json({ message: "This is the users route page" });
});



app.listen(5000 ,  () => {
    console.log(`Server is running on port 5000`);
});
