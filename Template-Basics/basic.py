from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #mylist = [1,2,3,4,5,6]
    user_logged_in = False
    puppes = ['Fluffy','Rufus','Spike']
    name = "aboulmagd"
    letters = list(name)
    pup_dictionary = {'pup_name':'sammy'}
    return render_template('basic.html',name=name,letters=letters,pup_dictionary=pup_dictionary,puppes=puppes,user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)