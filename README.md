# project_235

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Folkas/project_235/blob/master/LICENSE)

## Table of contents:
* [General info](#general-info)
* [Setup](#setup)
* [How to use](#howtouse)
* [Other](#other)


## General info:
This repository contains Flask application for Turing College module 2 spring 3 final assignment. The application predicts house price based on 13 inputs from Boston house price dataset.

## Setup
To run this project, install it using `pip` command:
```
!pip install git+https://github.com/Folkas/project_235.git
```
The linear regression model is located in ```model.py```

The Flask app is located in `app.py`

## How to use:
To use application, send `POST` request to https://folkas-project235.herokuapp.com/predict using Postman or other program. The request message could look as follows:
```
{"inputs": [4.0974e+00, 0.0000e+00, 1.9580e+01, 0.0000e+00, 8.7100e-01, 5.4680e+00, 1.0000e+02, 1.4118e+00, 5.0000e+00, 4.0300e+02, 1.4700e+01, 3.9690e+02, 2.6420e+01]}
```
or
```
{"inputs": [1.7142e-01, 0.0000e+00, 6.9100e+00, 0.0000e+00, 4.4800e-01, 5.6820e+00, 3.3800e+01, 5.1004e+00, 3.0000e+00, 2.3300e+02, 1.7900e+01, 3.9690e+02, 1.0210e+01]}
```

## Other
* I can't wait to get over this module
