from xmlrpc import client

s = client.ServerProxy('http://13.92.98.159:2332/PUCMM')
print (s.primeros(5))
