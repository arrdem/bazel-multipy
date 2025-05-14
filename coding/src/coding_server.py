import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from flask import Flask, request, jsonify
import click

app = Flask(__name__)
 
def coding_geocode(address: str) -> Dict[str, float]:
    """A very basic dummy geocoder."""
    if "San Francisco" in address:
        if "Golden Gate Bridge" in address:
            return {"latitude": 37.8199, "longitude": -122.4783}
        elif "Larimer Square" in address:
            return {"latitude": 37.7953, "longitude": -122.3930} # Mock Larimer Square in SF (Ferry Building area)
        else:
            return {"latitude": 37.7749, "longitude": -122.4194} # Generic San Francisco
    else:
        return {} # Address not found

            
 @app.route('/geocode', methods=['GET'])
 def coding_geocode_endpoint():
     address = request.args.get('address')
     if address:
         coordinates = coding_geocode(address)
         return jsonify(coordinates)
     else:
         return jsonify({"error": "Address parameter is missing"}), 400


def coding_run_geocoding_service(host: str = HOST, port: int = PORT):

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
