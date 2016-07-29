# Installation

## Windows 8, 64 bit

**Step 1.** Install Anaconda

```shell
https://www.continuum.io/downloads
```

**Step 2.** Discover the Map

[https://docs.python.org/2/library/index.html](https://docs.python.org/2/library/index.html)


## CentOS 6.3, Cent OS 7

Download developer tools

```bash
yum groupinstall "Development tools"
yum install zlib-devel
yum install bzip2-devel
yum install openssl-devel
yum install ncurses-devel
yum install sqlite-devel

```


Download, compile and install Python

```bash
cd /opt
wget --no-check-certificate https://www.python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz
tar xf Python-2.7.6.tar.xz
cd Python-2.7.6
./configure --prefix=/usr/local
make && make altinstall

ln -s /usr/local/bin/python2.7 /usr/local/bin/python

## link

# final check
which python
python -V

# install Anaconda
cd ~/Downloads
wget https://repo.continuum.io/archive/Anaconda-2.3.0-Linux-x86_64.sh
bash ~/Downloads/Anaconda-2.3.0-Linux-x86_64.sh
```

