This aligns faces, with some tuning for a *particular* use case. Primarily cribbed off [this tutorial](https://www.pyimagesearch.com/2017/05/22/face-alignment-with-opencv-and-python/).

## Setup

### System

Install some system packages first ([needed for dlib](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/)):

```shell
$ sudo apt-get update
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libopenblas-dev liblapack-dev 
```

Also [download a dlib face predictor model](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).

Unzip it and put it in this folder.

```shell
$ bzip2 -d shape_predictor_68_face_landmarks.dat.bz2
$ mv shape_predictor_68_face_landmarks.dat <here>
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
The package install will take a while, because opencv is big, and dlib has to build with cmake.

You could also use whatever python env solution is the flavour of the month.

## Usage

```shell
$ python align_faces.py --shape-predictor shape_predictor_68_face_landmarks.dat --images photos --output output
```


