var fs = require('fs');
var path = require('path');

// Webserver.
var express = require('express');
var morgan = require('morgan');
var app = express();
var server = require('http').createServer(app);
var port = process.env.PORT || 3000;

const NODE_ENV = process.env.NODE_ENVIRONMENT || 'development';

const ROOT_DIR = path.normalize(__dirname + '/../..');
const BUILD_DIR = ROOT_DIR + '/build';
const CLIENT_DIR = ROOT_DIR + '/src/client';

app.use(morgan(NODE_ENV === 'development' ? 'dev' : 'combined'));

app.use('/js/', express.static(BUILD_DIR + '/js'));
app.use('/css/', express.static(BUILD_DIR + '/css'));
app.use(express.static(CLIENT_DIR));

app.get('/', function (req, res, next) {
  res.sendFile(CLIENT_DIR + '/index.html');
  next();
});

app.get('/index.html', function (req, res, next) {
  res.sendFile(CLIENT_DIR + '/index.html');
  next();
});

server.listen(port, function () {
  console.log('Server listening at port %d', port);
});
