from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head> 
       <title>TOP SOFTWARE COMPANIES REVENUE</title>
    </head>
    <body>
    <table border="4" cellspacing="5" width="40" height="50">
       <caption>REVENUE</caption>
       <tr>
         <th>company</th>
         <th>revenue</th>
         <th>r&d spend</th>
       </tr>
       <tr>
         <td>amazon.com</td>
         <td>$177,866m</td>
         <td>$23,015m</td>
       </tr>
       <tr>
         <td>alphabet</td>
         <td>$110,855m</td>
         <td>$16,625m</td>
       </tr>
       <tr>
         <td>facebook</td>
         <td>$40,653m</td>
         <td>$7,754m</td>
       </tr>
       <tr>
         <td>salesforce.com</td>
         <td>$10,480m</td>
         <td>$1,632.2m</td>
       </tr>
       <tr>
         <td>netflix</td>
         <td>$11,692.7m</td>
         <td>$1,052.8m</td>
       </tr>
    </table> 
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()