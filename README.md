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
{"inputs": [4.5900e-02, 5.2500e+01, 5.3200e+00, 0.0000e+00, 4.0500e-01, 6.3150e+00, 4.5600e+01, 7.3172e+00, 6.0000e+00, 2.9300e+02, 1.6600e+01, 3.9690e+02, 7.6000e+00]}
```
Output (expected price: 22.3):\
```{"predicted price": 27}```\

or

```
{"inputs": [1.06590e-01, 8.00000e+01, 1.91000e+00, 0.00000e+00, 4.13000e-01, 5.93600e+00, 1.95000e+01, 1.05857e+01, 4.00000e+00, 3.34000e+02, 2.20000e+01, 3.76040e+02, 5.57000e+00]}
```
Output (expected price: 20.6):\
```{"predicted price": 17}```\
## Other
* I can't wait to get over this module
