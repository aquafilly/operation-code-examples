const http = require("http");
const express = require("express");

let app = express();
app.server = http.createServer(app);

let buttonClicks = 0;

var port = process.env.PORT || 3001;

app.use('/', express.static('public'));

app.get('/button', function(req, res) {
    buttonClicks += 1;
    console.log('server: button clicked ' + buttonClicks + ' times');
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify({clicks: buttonClicks}));
});

app.server.listen(port, () => {
    console.log(`server: started listening on port ${app.server.address().port}`);
});
