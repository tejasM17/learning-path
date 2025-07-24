const mongoose = require('mongoose');

const bookSchema = new mongoose.Schema({
    name:{
        type: String,
        required: true
    },
    price: {
        type: Number,
        required: true
    },
    author: {
        type: String,
        required: true
    },
    discription: {
        type: String,
        required: true
    }
});

module.exports = mongoose.model('Book', bookSchema);