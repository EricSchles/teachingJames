from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/<name>", methods=["GET","POST"])
def index(name=None):
    if name:
        return "Hello,"+name
    else:
        return "Hello, James"
    
if "__main__" == __name__:
    app.run(debug=True)
