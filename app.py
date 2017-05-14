from flask import Flask, render_template, request

app = Flask(__name__)

form_vars = ["VAR1", " VAR2", "VAR3", "VAR4", "VAR5", "VAR6", "VAR7", "VAR8", "VAR9", "VAR10"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return show_the_result()
    else:
        return show_the_form()
  

#@app.route('/random_forest')
#def hello():
#    return 'training info here'

def show_the_form():
    return render_template('form.html', form_vars = form_vars)

def show_the_result():
    result = request.form
    return render_template("result.html",result = result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)
