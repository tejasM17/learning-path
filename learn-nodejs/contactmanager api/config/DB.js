const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        const connection  = await mongoose.connect('mongodb+srv://contactmanageruser:DAqs4Yo3NctCqLNZ@contact-manager-clutste.qgtrwl5.mongodb.net/contactmanager-api?retryWrites=true&w=majority&appName=contact-manager-clutster');
        console.log(`MongoDB Connected ${connection.connection.host}`);
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
}

module.exports = connectDB;