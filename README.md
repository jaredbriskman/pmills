## Setup
### System
Install some system packages first ([needed for dlib](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/)):

```shell
$ sudo apt-get update
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libopenblas-dev liblapack-dev 
```

### Python
It's significantly suggested to use pipenv
```shell
$ pip3 install pipenv
```

Then install packages and enter a venv with:

```shell
$ pipenv install
$ pipenv shell
```

You could also use the requirements.txt, if you feel like that.
