import xmlrpclib

s = xmlrpclib.ServerProxy('http://foocamp.org.do:2332/PUCMM')
print s.primeros(5)
