from flask import render_template, jsonify
from app import app, lm, db, util
from ..models import Device
import json


@app.route('/devicelist')
def devicelist():
    return render_template("devicelist.html")


@app.route('/loaddevices', methods=['POST'])
def loaddevices():
    devices = Device.query.all()
    return util.query_result_json(devices)


@app.route('/editor')
def editor():
    i=0