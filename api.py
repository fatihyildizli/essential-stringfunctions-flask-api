from flask import Flask
from flask import g
from flask import jsonify
from flask import request
import json
import re
import urllib.parse
import codecs
import base64
import binascii
## Author: Fatih Yıldızlı 
app = Flask(__name__)


@app.route("/length", methods=["POST"])
def length():

     return jsonify(len(request.form['input']))


@app.route("/removewhitespace", methods=["POST"])
def removewhitespace():

  return jsonify(re.compile(r'\s+').sub('', request.form['input']))


@app.route("/encode", methods=["POST"])
def encode():

  return jsonify(urllib.parse.quote(request.form['input']) )

@app.route("/decode", methods=["POST"])
def decode():

  return jsonify(urllib.parse.unquote(request.form['input']) )

@app.route("/binary", methods=["POST"])
def binary():

  return jsonify(''.join(format(ord(i), 'b') for i in request.form['input']))


@app.route("/base64encode", methods=["POST"])
def encodeBase64():

  return jsonify("".join(map(chr, base64.b64encode(request.form['input'].encode()))))

@app.route("/base64decode", methods=["POST"])
def decodeBase64():

  return jsonify("".join(map(chr, base64.b64decode(request.form['input'].encode()))))

@app.route("/encodehex", methods=["POST"])
def encodehex():
  
  return jsonify("".join(hex(ord(c))[2:] for c in request.form['input']))


if __name__ == '__main__':
    app.run(debug=False)

