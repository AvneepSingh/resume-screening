var http = require('http');
var formidable = require('formidable');
var fs = require('fs');
const { exec } = require("child_process");

http.createServer(function (req, res) {
  if (req.url == '/fileupload') {
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
      var oldpath = files.filetoupload.filepath;
      var newpath = '../input/resume.txt';
      fs.rename(oldpath, newpath, function (err) {
        if (err) throw err;
        res.write('<html>');
        res.write('<title>resume screening</title>');
        res.write('<body bgcolor="powderblue">');
        res.write('<h1>File uploaded and moved!</h1>');
        res.write('<br>')
        res.write('<h4><a href="http://localhost:8080">upload more</a></h4>');
        res.write('</body>');
        res.write('</html>')
        res.end();
        exec("cd .. && ./runcheck", (error, stdout, stderr) => {
              if (error) {
                  console.log(`error: ${error.message}`);
                  return;
              }
              if (stderr) {
                  console.log(`stderr: ${stderr}`);
                  return;
              }
              console.log(`stdout: ${stdout}`);
          });
      });
 });
  } else {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<html>');
    res.write('<title>resume screening</title>');
    res.write('<body bgcolor="powderblue">');
    res.write('<h1>resume screening</h1>');
    res.write('<br>')
    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    res.write('</body>');
    res.write('</html>')
    return res.end();
  }
}).listen(8080);
