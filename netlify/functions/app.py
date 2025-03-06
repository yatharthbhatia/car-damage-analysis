from flask import Flask
from src.app import app

def handler(event, context):
    return app(event, context)