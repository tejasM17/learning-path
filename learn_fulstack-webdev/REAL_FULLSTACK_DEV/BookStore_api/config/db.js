const mongoose = require('mongoose');
const connectDB = async () => {
    try {
        // Fixed connection string - properly encoded the password with @ symbol
        const conn = await mongoose.connect(
            'mongodb+srv://nodeapi:tejas123%409380@nodeapi-cluster.465s1z1.mongodb.net/bookstore_api'
        );

        console.log(`MongoDB Connected to ${conn.connection.host}`);
    } catch (error) {
        console.log(error);
        process.exit(1);
    }
}

module.exports = connectDB;