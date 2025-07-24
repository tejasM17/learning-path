// const express = require('express');
// const router = express.Router();

// module.exports = router;

// abbove code is boiler pate 


const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
    console.log(req.body);
    res.json({ message: "This is the products route page" });
});

router.get('/:productId', (req, res) => {
    console.log(req.params.productId);

    const productId = req.params.productId;

    res.json({ message: `display product with id ${productId}` });
});

module.exports = router;