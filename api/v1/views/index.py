#!/usr/bin/python3
"""Index"""
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def stats_count():
    stats = {}
    class_names = {"Amenity": "amenities", "City": "cities",
                    "Place": "places", "Review": "reviews",
                    "State": "states", "User": "users"}

    for class_name in class_names:
        stats[class_names[class_name]] = storage.count(class_name)
    return jsonify(stats)
