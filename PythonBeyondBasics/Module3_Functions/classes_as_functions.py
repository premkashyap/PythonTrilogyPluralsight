import socket

class Resolver:
    def __init__(self):
        self._cache = {}
    ''' this enables class to use as function and can be used as a function which hold state'''
    def __call__(self, host):
        if host not in self._cache:
            self._cache[host]=socket.gethostbyname(host)
        return self._cache[host]
    def clear(self):
        self._cache.clear()
    
    def has_host(self, host):
        return host in self._cache

resolver = Resolver()

if __name__ == 'main':
    print(resolver('facebook.com'))
    print(resolver('twitter.com'))
    print(resolver.has_host('facebook.com'))


