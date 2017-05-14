"""
Simple flask app to capture 10 variables in a form and
run them against a pre built random forest machine learnign model
Stephen Kennedy-Clark
13 May 2017
"""
import HTMLParser
from flask import Flask, render_template, request


app = Flask(__name__)

FORM_VARS = ["VAR1", " VAR2", "VAR3", "VAR4", "VAR5", "VAR6", "VAR7", "VAR8", "VAR9", "VAR10"]

@app.route('/', methods=['GET', 'POST'])


def index():
    """default route, detects isPostBack and displays either blank form  or results"""
    if request.method == 'POST':
        return show_the_result()
    else:
        return show_the_form()

def show_the_form():
    """displays an empty form - not isPostBack"""
    return render_template('form.html', form_vars=FORM_VARS)


def show_the_result():
    """PostBackm displays prepopulated HTML form and prediction """
    result = request.form
    err_message = ""

    for value in FORM_VARS:
        if len(result[value]) == 0:
            err_message += "Please provide a value for " + value + "<br />"

    model_result = [0, 0.92]
    return render_template("result.html", \
                                    result=result, \
                                    form_vars=FORM_VARS, \
                                    model_result=model_result, \
                                    err_message=err_message)

#@app.route('/random_forest')
#def hello():
#    return 'training info here'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
