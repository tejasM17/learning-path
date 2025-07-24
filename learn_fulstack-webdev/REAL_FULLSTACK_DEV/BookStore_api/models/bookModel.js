const mongoose = require('mongoose');

const bookSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    // Changed field name to match incoming data (Discription)
    Discription: {
        type: String,
        required: true
    },
    // Changed field name to match incoming data (Price)
    Price: {
        type: Number,
        required: true
    },
    // Changed field name to match incoming data (authour)
    authour: {
        type: String,
        required: true
    },
    publishYear: {
        type: Number,
        required: false // Made optional for now
    }
}, {
    // This will allow additional fields that aren't in the schema
    strict: false
});

module.exports = mongoose.model('Book', bookSchema);