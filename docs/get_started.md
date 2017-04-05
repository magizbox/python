# Get Started

Welcome! This tutorial details how to get started with Python.

## For Windows

### Anaconda 4.3.0

<div class="row">
<div class="col-sm-6">
<i>Anaconda is BSD licensed which gives you permission to use Anaconda commercially and for redistribution.</i>
<br/><br/>
1. Download the installer <br/>
2. Optional: Verify data integrity with MD5 or SHA-256  <br/>
3. Double-click the <b>.exe</b> file to install Anaconda and follow the instructions on the screen

</div>
<div class="col-sm-6 text-center">
<h4>Python 3.6 version</h4>
<a class="btn btn-success" href="https://repo.continuum.io/archive/Anaconda3-4.3.0.1-Windows-x86_64.exe" target="_blank">64-BIT INSTALLER</a>
<br/>
<hr style="border-top: 1px solid rgba(51, 51, 51, 0.24);">
<h4>Python 2.7 version</h4>
<a class="btn btn-success" href="https://repo.continuum.io/archive/Anaconda2-4.3.0.1-Windows-x86_64.exe" target="_blank">64-BIT INSTALLER</a>
<br/>
</div>
</div>


**Step 2.** Discover the Map

[https://docs.python.org/2/library/index.html](https://docs.python.org/2/library/index.html)


## For CentOS

### Developer tools
<div class="row">
<div class="col-sm-6">
<i>The Development tools will allow you to build and compile software from source code. Tools for building RPMs are also included, as well as source code management tools like Git, SVN, and CVS.</i>
</div>
<div class="col-sm-6">
```bash
yum groupinstall "Development tools"
yum install zlib-devel
yum install bzip2-devel
yum install openssl-devel
yum install ncurses-devel
yum install sqlite-devel
```
</div>
</div>

### Python & Anaconda
<div class="row">
<div class="col-sm-6">
<i>Anaconda is BSD licensed which gives you permission to use Anaconda commercially and for redistribution.</i>
</div>
<div class="col-sm-6">

```bash
cd /opt
wget --no-check-certificate https://www.python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz
tar xf Python-2.7.6.tar.xz
cd Python-2.7.6
./configure --prefix=/usr/local
make && make altinstall
## link
ln -s /usr/local/bin/python2.7 /usr/local/bin/python
# final check
which python
python -V
# install Anaconda
cd ~/Downloads
wget https://repo.continuum.io/archive/Anaconda-2.3.0-Linux-x86_64.sh
bash ~/Downloads/Anaconda-2.3.0-Linux-x86_64.sh
```
</div>
</div>
