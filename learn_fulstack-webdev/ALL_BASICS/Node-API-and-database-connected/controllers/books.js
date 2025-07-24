const express = require('express');
const router = express.Router();

const Book = require('../models/BookModel.js');

router.get('/', async (req, res) => {
    const books = await Book.find({});
    res.json({ message: "displaying all books", books: books });
});

router.post('/', (req, res) => {
    console.log(req.body);
    
    res.json({ message: "Post req - creating new book" });
});

router.put('/', (req, res) => {
    res.json({ message: "put req - updating book"});
});

router.delete('/', (req, res) => {
    res.json({ message: "delete req - deleting book"});
});


module.exports = router;