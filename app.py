from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #do_the_prediction()
        #return 'training info here'
        return show_the_form()
    else:
        return show_the_form()
  

#@app.route('/random_forest')
#def hello():
#    return 'training info here'

def show_the_form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)
