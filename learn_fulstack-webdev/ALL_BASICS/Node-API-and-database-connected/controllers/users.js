const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    res.json({ message: "This is the users route page" });
});

router.get('/:userId', (req, res) => {
    console.log(req.params.userId);

    const userId = req.params.userId;

    res.json({ message: `display user with id ${userId}` });
});

module.exports = router;
