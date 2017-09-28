from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/PUCMM',)

server = SimpleXMLRPCServer(("foocamp.org.do", 2332),
                            requestHandler=RequestHandler)

def primeros(x):
    ans = [ y for y in range(x) ]
    return ans
server.register_function(primeros)

server.serve_forever()
