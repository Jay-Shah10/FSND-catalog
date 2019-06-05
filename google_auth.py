#!/usr/bin/python2

import os
import flask
import functools

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

