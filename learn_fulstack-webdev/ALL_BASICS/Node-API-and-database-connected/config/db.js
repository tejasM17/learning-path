const mongoose = require('mongoose');
const connectDB = async () => {
  try {
    // Connect to MongoDB Atlas with the provided connection string
    // URL-encode the password to handle special characters like @
    const username = 'nodeapi';
    const password = encodeURIComponent('tejas123@9380');
    const cluster = 'nodeapi-cluster.465s1z1.mongodb.net';
    const connectionString = `mongodb+srv://${username}:${password}@${cluster}/?retryWrites=true&w=majority&appName=nodeapi-cluster`;

    const connection = await mongoose.connect(connectionString, {
      serverSelectionTimeoutMS: 10000 // Timeout after 10 seconds
    });

    console.log(`MongoDB connected: ${connection.connection.host}`);
  } catch (error) {
    console.error("MongoDB connection error:", error.message);
    console.log("Running without database connection");
  }
};

module.exports = connectDB;

