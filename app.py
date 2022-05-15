import flask
import json
import traceback

server = flask.Flask(__name__)

@server.route('/si', methods=['POST', 'GET'])
def si_calculator():
    try:
        data = flask.request.json
        principal = data['principal']
        rate = data['rate']
        time = data['time']
        si = principal * rate * time
        response = json.dumps({"Simple Interest":si})
    except Exception as e:
        msg = "Failed to perform calculation::" + str(e)
        response = msg + " TRACEBACK:: " + str(traceback.format_exc())
        return flask.Response(response=response, status=202, mimetype='text')
    finally:
        pass
    return flask.Response(response=response, status=200, mimetype='application/json')