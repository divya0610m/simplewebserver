from http.server import HTTPServer, BaseHTTPRequestHandler 
content="""
<html>
    <head>
        <TITLE> WEB APPLICATION </TITLE>
    </head>
    <body>
        <table border="6" bgcolor="pink">
        <caption>TCP/IP PROTOCOL SUITE</caption>
            <tr bgcolor="lightblue">
                <th>S.no</th> <th>Layer</th> <th>Protocols</th>
            </tr>
            <tr>
                <td>1.</td> <td>Application layer</td> <td>HTTP, FTP, DNS</td>
            </tr>
            <tr>
                <td>2.</td> <td>Transport layer</td> <td>TCP, UDP</td>
            </tr>
            <tr>
                <td>3.</td> <td>Internet layer</td> <td>IPV4/IPV3</td>
            </tr>
            <tr>
                <td>4.</td> <td>Network access layer</td> <td>MAC, Ethernet</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler (BaseHTTPRequestHandler):
     def do_GET(self):
        print("request received") 
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('', 8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

