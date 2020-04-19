#!/usr/bin/python

from wrapper import connect_alias
from wrapper import connect
from wrapper import status
from wrapper import disconnect
from flask import Flask,jsonify
from flask_restful import Resource, Api
import urllib
import time

app = Flask(__name__)
api = Api(app)


class Location(Resource):
    def post(self, location):
        if location=="fr1":alias="frst"
        elif location=="fr2":alias="frpa1"
        elif location=="fr3":alias="frpa2"
        elif location=="ch":alias="ch2"
        elif location=="be":alias="be"
        elif location=="mc":alias="mc"
        elif location=="lu":alias="lu"
        elif location=="ca1":alias="cato"
        elif location=="ca2":alias="camo2"
        elif location=="smart":alias="smart"
        elif location=="uk":alias="ukdo"
        elif location=="us":alias="usny"
        else: alias="frst"
        disconnect()
        connect_alias(alias)
        return jsonify({'location': str(alias)})

class Reconnect(Resource):
    def post(self):
        disconnect()
        connect()
        return jsonify({'status': 'connected'})
        
        
class Status(Resource):
    def get(self):
        return jsonify({'status': status()[0]})
      
api.add_resource(Location, '/location/<string:location>', endpoint="location")
api.add_resource(Reconnect, '/reconnect', endpoint="reconnected")
api.add_resource(Status, '/status', endpoint="status")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)
