const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;

const server = http.createServer(function(req, res) {
  console.log(`${req.method} request for ${req.url}`);

  if (req.url === '/') {
    fs.readFile(path.join(__dirname, 'public', 'index.html'), function(err, data) {
      if (err) {
        res.writeHead(500, {'Content-Type': 'text/plain'});
        res.end('500 Internal Server Error');
      } else {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.end(data);
      }
    });
  } else {
    res.writeHead(404, {'Content-Type': 'text/plain'});
    res.end('404 Not Found');
  }
});

server.listen(PORT, function() {
  console.log(`Server listening on port ${PORT}`);
});