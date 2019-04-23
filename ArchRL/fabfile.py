__data__ = '2019-04-22 09:35'
__author__ = 'Kai'

from fabric import Connection



def foo():
    c = Connection('root@ip', connect_kwargs={'password': 'pwd'})
    c.put('ArchRL.zip', '/root/project')

if __name__ == '__main__':
    foo()
