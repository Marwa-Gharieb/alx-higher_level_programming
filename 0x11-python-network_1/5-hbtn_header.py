import urllib

k = dir(urllib)

#print(k)
from urllib import request

l = dir(request)
#print(l)
n = request.urlopen("https://en.wikipedia.org/wiki/HTTP_404")

#print(type(n))
#print(dir(n))
#print(n.code)
#print(n.length)
print(n.peek())