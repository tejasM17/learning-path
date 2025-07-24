//  CRUD API for BookStore
// C - Create book
// R - Read book
// U - Update book
// D - Delete book

const express = require('express');
const app = express();
const cors = require('cors');
app.use(cors());

const connectDB = require('./config/db');
connectDB();

app.use(express.json({ extended: false }));

// Middleware
app.use(express.json()); // For parsing application/json
app.use(express.urlencoded({ extended: true })); // For parsing application/x-www-form-urlencoded

// Routes
app.use('/api/books', require('./routes/bookRoutes'));

// Root route
app.get('/', (req, res) => {
    res.json({ message: "API server is running" });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: "Something went wrong!", error: err.message });
});

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
