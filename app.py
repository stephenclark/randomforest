"""
Simple flask app to capture 10 variables in a form and
run them against a pre built random forest machine learnign model
Stephen Kennedy-Clark
13 May 2017
"""
import HTMLParser
import pickle
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
    get_prediction = True
    model_result = ['data not valid', 'data not valid']

    for value in FORM_VARS:
        if len(result[value]) == 0:
            get_prediction = False
            err_message += "Please provide a value for " + value + "<br />"
    
    if get_prediction:
        a = []       
        for value in FORM_VARS:
            this_result = ""
            if not result[value].isdigit():
                this_result = result[value].upper()
                if result[value] == 'L':
                    this_result = 0
                elif result[value] == 'N':
                    this_result = 1
                elif result[value] == 'H':
                    this_result = 2
                else:
                    err_message += "Value for "+value+" was "+result[value]+". Value must be int, 'L', 'N', or 'H'. Assumed to be N<br />"
                    this_result = 1
            
            a.append(this_result)

        print(a, file=sys.stderr)

        filename='finalized_model.sav'
        clf = pickle.load(open(filename, 'rb'))
        # place prediction and probability in array and pass to html form template
        # prediction is either 0 or 1, probability is 2nd member of 2D array, prob of 0, prob of 1
        # so if prediction is for 0 we want the first member of probability array
        # if 1 we want toe second. 
        prediction = clf.predict(a)
        probability = clf.predict_proba(a)[0,clf.predict(a)]
        model_result = [prediction, probability]

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
