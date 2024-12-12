from flask import Flask, render_template, Response, jsonify, request
import sys
import os

@app.route('/shutdown', methods=['POST'])
def shutdown():
    """Shutdown the application gracefully"""
    try:
        # Release resources
        video_stream.release()
        # Exit the application
        os._exit(0)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})