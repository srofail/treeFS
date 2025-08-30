from flask import Flask, render_template, request, redirect, url_for, flash, session
from backend import Backend

app = Flask(__name__, template_folder='../Frontend', static_folder='../static')

@app.route("/")
def start_page():
    if request.method == "POST":
        origin_latitude = request.form['origin_latitude']
        origin_longitude = request.form['origin_longitude']
        destination_latitude = request.form['destination_latitude']
        destination_longitude = request.form['destination_longitude']

        session['journeys'] = backend.get_journeys(origin_latitude, origin_longitude, destination_latitude, destination_longitude)
        return redirect(url_for('options'))

    return render_template("start_page.html")

@app.route("/options")
def options_page():
    if request.method == "POST":
        pass # redirect to the chosen journey

    presentation = Backend.get_short_formats[session['journeys']]

    return render_template("options.html", journey_list=presentation)

if __name__ == "__main__":
	# Development server entrypoint
    backend = Backend()
    app.run(debug=True)
    
