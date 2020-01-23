#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = '++/EggoTrainingFlaskApplication/++'

client = MongoClient('mongodb://admin:admin@mongodb:27017/admin')
db = client.eggodb

