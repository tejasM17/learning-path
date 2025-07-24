const express = require('express');
const router = express.Router();

const Contact = require('../models/contactModel');


// display all contacts
router.get('/', async(req, res) => {
    try {
        const contacts = await Contact.find();
        res.json(contacts);
    } catch (error) {
        console.log(error);
    }
});

// display single contacts
router.get('/:id', async (req, res) => {
    try {
        const contact = await Contact.findById(req.params.id);
        res.json(contact);
    } catch (error) {
        console.log(error);
    }
})

//  create contacts
router.post('/', async(req, res) => {
    console.log(req.body);

    const {name, email, phone , address} = req.body;

    try {
        const contact = await Contact.create({
            name,
            email,
            phone,
            address
        })

        res.json(contact);
    } catch (error) {
        console.log(error);
    }

    console.log(contact);
    

    
})

// update contacts details
router.put('/:id', (req, res) => {
    res.json({message: "is is for updating contacts details "});
})

// delete contacts
router.delete ('/:id', (req, res) => {
    res.json({message: "is is for deleting contacts "});
})



// display single contacts
router.get('/:id', (req, res) => {
    res.json({message: "is is for showing single contacts "});
})




module.exports = router;