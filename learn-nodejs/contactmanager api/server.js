const express = require('express');
const contacts = require('./routes/contactRoutes.js');
const connectDB = require('./config/DB.js');


const app = express();
app.use(express.json());

connectDB();

app.get('/', (req, res) => {
    res.json({message: "contact manage api"});
})

app.use('/contacts', contacts);


app.listen(5000, () => {
    console.log("server is running on port 5000");
})