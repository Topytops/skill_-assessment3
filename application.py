from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")


@app.route("/application-form")
def show_form():


    return render_template("application-form.html")



@app.route("/applications", methods=['POST'])
def application_resp():

    f_name = request.form.get("first_name")
    l_name = request.form.get("last_name")
    salary = request.form.get("salary")
    position = request.form.get("job_title")

    return render_template('application-response.html', first_name=f_name, last_name=l_name, job_title=position,
    						salary=salary)


if __name__ == "__main__":
    app.run(debug=True)



    
