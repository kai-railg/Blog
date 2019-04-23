__data__ = '2019-04-22 09:35'
__author__ = 'Kai'

from fabric import Connection


def main():
    c = Connection('root@ip', connect_kwargs={'password': ''})
    c.local('cd ~/Desktop/git/; git add .; git commit -m "提交"; git push')
    c.run('/root/git/./git pull')


def foo():
    c = Connection('root@ip', connect_kwargs={'password': ''})
    c.put('collect_static/', '/root/project/ArchMd/')

if __name__ == '__main__':
    foo()
