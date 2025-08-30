from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__, template_folder='../Frontend', static_folder='../static')

@app.route("/")
def start_page():
    return render_template("start_page.html")

if __name__ == "__main__":
	# Development server entrypoint
	# Flask's built-in server is fine for local dev; use a production WSGI server for deployment.
	app.run(debug=True)
