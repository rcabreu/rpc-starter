from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/PUCMM',)

server = SimpleXMLRPCServer(("0.0.0.0", 2332),
                            requestHandler=RequestHandler)

def primeros(x):
    ans = [ y for y in range(x) ]
    return ans
server.register_function(primeros)

server.serve_forever()
