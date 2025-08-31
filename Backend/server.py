from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from backend import Backend

app = Flask(__name__, template_folder='../Frontend', static_folder='../static')

@app.route("/", methods=["GET", "POST"])
def start_page():
    if request.method == "POST":
        # origin_latitude = request.form.get('origin_latitude', 'string')
        # origin_longitude = request.form.get('origin_longitude', 'string')
        # destination_latitude = request.form.get('destination_latitude', 'string')
        # destination_longitude = request.form.get('destination_longitude', 'string')

        session['origin_name'] = "University of Sydney"
        session['dest_name'] = "Random Place"

        session['journeys'] = backend.get_journeys(-33.889299, 151.193106, -33.889922, 151.089027)
        return redirect(url_for('options_page'))

    return render_template("start_page.html")

@app.route("/list_of_options")
def list_of_options():
    presentation = Backend.get_short_formats(Backend.results[session['journeys']])

    return jsonify({"journey_list": presentation, "start": session["origin_name"], "end": session["dest_name"]})

@app.route("/options", methods=["GET","POST"])
def options_page():
    if request.method == "POST":
        session['route_chosen'] = request.form['number']
        print("got it")
        return redirect(url_for('more_info'))

    return render_template("options.html")

@app.route("/list_of_info")
def list_of_info():
    presentation = Backend.get_short_formats(Backend.results[session['journeys']][session['route_chosen']])

    return jsonify({"journey_list": presentation, "start": session["origin_name"], "end": session["dest_name"]})

@app.route("/more_info")
def more_info():
    return render_template("more_info.html")

if __name__ == "__main__":
	# Development server entrypoint
    backend = Backend()
    app.secret_key = "philip"
    app.run(debug=True)
    
