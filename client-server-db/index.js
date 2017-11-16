const http = require("http");
const express = require("express");
var bodyParser = require('body-parser');


const PouchDB = require('pouchdb');
PouchDB.plugin(require('pouchdb-find'));
codersDb = new PouchDB('coders.db', { db: require('sqldown') });

let app = express();
app.server = http.createServer(app);
var port = process.env.PORT || 3001;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use('/', express.static('public'));

//GET request
app.get("/coders", function(req, res) {
    //Try to get all data from the codersDb
    codersDb.allDocs({include_docs: true}).then(function(result) {
        res.send(result.rows.map(function(item) {
            return item.doc;
        }));
    }, function(error) {
        res.status(400).send(error);
    });
});

//GET request (with query parameter)
app.get("/coders/:id", function(req, res) {
    //Make sure query has id that we need to lookup document in codersDb 
    if(!req.params.id) {
        return res.status(400).send({"status": "error", "message": "An `id` is required"});
    }

    //Try to get data from the codersDb
    codersDb.get(req.params.id).then(function(result) {
        res.send(result);
    }, function(error) {
        res.status(400).send(error);
    });
});

//POST request
app.post("/coders", function(req, res) {
    //Make sure request has all the required data for making a new 'coder' document 
    if(!req.body.firstname) {
        return res.status(400).send({"status": "error", "message": "Please enter your first name."});
    } else if(!req.body.lastname) {
        return res.status(400).send({"status": "error", "message": "Please enter your last name."});
    } else if (!req.body.meetups) {
        return res.status(400).send({"status": "error", "message": "Please enter the number of meetups you have attended."})
    }
    
    //Add new document to codersDb
    codersDb.post(req.body).then(function(result) {
        res.send(result);
    }, function(error) {
        res.status(400).send(error);
    });
});

app.put("/coders", function(req, res) { 
    //Make sure query has id that we need to lookup document in codersDb     
    if(!req.body.id) {
        return res.status(400).send({"status": "error", "message": "An `id` is required"});
    } else if(!req.body.firstname) {
        return res.status(400).send({"status": "error", "message": "Please enter your first name."});
    } else if(!req.body.lastname) {
        return res.status(400).send({"status": "error", "message": "Please enter your last name."});
    } else if (!req.body.meetups) {
        return res.status(400).send({"status": "error", "message": "Please enter the number of meetups you have attended."})
    }

    console.log(req.body);
    //Remove document from the codersDb
    codersDb.get(req.body.id).then(function(result) {
        result.firstname = req.body.firstname;
        result.lastname = req.body.lastname;
        result.meetups = req.body.meetups;
        return codersDb.put(result);
    }).then(function(result) {
        res.send(result);
    }, function(error) {
        res.status(400).send(error);
    });
});

//DELETE request
app.delete("/coders", function(req, res) { 
    //Make sure query has id that we need to lookup document in codersDb     
    if(!req.body.id) {
        return res.status(400).send({"status": "error", "message": "An `id` is required"});
    }

    //Remove document from the codersDb
    codersDb.get(req.body.id).then(function(result) {
        return codersDb.remove(result);
    }).then(function(result) {
        res.send(result);
    }, function(error) {
        res.status(400).send(error);
    });
});

var server = app.listen(3000, function() {
   codersDb.info().then(function(info) {
       console.log(info);
       console.log("Listening on port %s...", server.address().port);
   });
});

app.server.listen(port, () => {
    console.log(`server: started listening on port ${app.server.address().port}`);
});
