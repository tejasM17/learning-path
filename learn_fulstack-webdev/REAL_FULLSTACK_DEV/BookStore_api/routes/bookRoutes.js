const express = require('express');
const router = express.Router();
const Book = require('../models/bookModel');

// To list all the books
router.get('/', async (req, res) => {
    try {
        
    const book = await Book.find({});

    res.json({ books: book });
    } catch (error) {
        console.log(error)
        res.json({ message: "Something went wrong!" });
    }
});

// To list single book
router.get('/:bookId', async (req, res) => {
    try {
        
    const book = await Book.findById(req.params.bookId);

    res.json({ book: book });
    } catch (error) {
        console.log(error)
        res.json({ message: "Something went wrong!" });
    }
});

// Creating new book
router.post('/', async (req, res) => {
    console.log(req.body);
    try {
        
    const book = await Book.create(req.body);
    
    return res.json({ book: book, data: req.body });
    } catch (error) {
        console.log(error.message);
        return res.status(500).json({ message: "Something went wrong!" });
    }
});

// Updating book
router.put('/:bookId', async (req, res) => {
    try {
    console.log(req.params.bookId);
    const book = await Book.findByIdAndUpdate(req.params.bookId, req.body, {new: true });
    res.json({ book });
    } catch (error) {
        console.log(error);
        res.json({ message: "Something went wrong!" });    
    }
});

// Deleting book
router.delete('/:bookId', async (req, res) => {
    try {
    const book = await Book.findByIdAndDelete(req.params.bookId);
    return res.json({ message: "Book deleted successfully!", book });
    } catch (error) {
        console.log(error);
        return res.json({ message: "Something went wrong!" });    
    }
    
});

module.exports = router;