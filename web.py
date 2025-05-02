from http.server import HTTPServer,BaseHTTPRequestHandler

content='''

<html>
   <h1>TCP/IP Protocol Suite</h1>

    <table>
    <table border="5" bgcolor="cyan" cellpadding="10"> 
            <caption align="center"></caption> 
            <th colspan="7" align="center" bgcolor="aquamarine"></th> 
        <tr>
            <th>LAYER</th>
            <th>PROTOCOLS (EXAMPLES)</th>
            <th>FUNCTION</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP</td>
            <td>Provides network services to applications</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
            <td>Manages end-to-end communication</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>IP (IPv4, IPv6), ICMP, ARP, IGMP</td>
            <td>Handles addressing and routing</td>
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>Ethernet, Wi-Fi, PPP, SLIP</td>
            <td>Manages physical data transmission</td>
        </tr>
    </table>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()