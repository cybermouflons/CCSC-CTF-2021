// Top level async function to call await on chesslib
(async function() {
    const express = require('express');
    const path = require('path');
    const chesslib_factory = require('./lib/chesslib.js')
    const chesslib = await chesslib_factory();

    const app = express();
    const port = process.env.PORT || 3000;

    const views = path.join(__dirname, 'views');

    app.set('view engine', 'ejs');
    app.set('views', views);

    app.use('/static', express.static(path.join(__dirname, 'static')))
    app.use(express.urlencoded({
        extended: true
    }))

    app.get('/', (req, res) => {
        res.locals.tab = 1;
        res.render("index");
    });

    app.post('/', async (req, res) => {
        const fen = req.body.fen;
        const fenstr_ptr = chesslib.allocateUTF8(fen);
        const checkmate_side = chesslib._check_mate(fenstr_ptr);
        chesslib._free(fenstr_ptr);

        res.locals.fen = fen;
        res.locals.checkmate_side = checkmate_side;
        res.locals.tab = 2;
        res.render("index");
    })

    app.listen(port, () => console.log(`Listening on port ${port}!`));
})()
