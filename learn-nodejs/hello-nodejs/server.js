const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
    res.send('we Brothers and Sisters have infinite Potentional');
})

// quary - request

app.get('/products', (req, res) => {
    console.log(req.query.search);
    const {search} = req.query;
    res.json({message : 'we Brothers send products GET route', names:'redos', productName: search} );
})


// params - request

app.get('/products/:id', (req, res) => {
    console.log(req.params.id);
    // destructure
    const {id} = req.params
    
    res.json({message : 'single products  GET route', names:'redos' , product: id} );
})














app.post('/products', (req, res) => {
    console.log(req.body);

    const {name, price} = req.body
    res.json({message : 'we Brothers send products POST route', name ,price} );
})

app.put('/products', (req, res) => {
    res.json({message : 'we Brothers send products PUT route', names:'redos'} );
})





app.listen(5000,() => {
    
    console.log('server started');
})

