from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="/encrypt" method="post">
        <label>
            Rotate by:
            <input type="text" name="rot" value="0"/>
            <br><br>
            <textarea name="text">{0}</textarea>
            
        </label>
        <br><br>
        <input type="submit" value="Submit Query"/>
    </form>


    </body>
</html>

"""
@app.route("/encrypt", methods=['POST'])
def encrypt ():
    
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']
    encrypt_txt = rotate_string(text, rot)
    encrypt_txt = "<h1>" + encrypt_txt + "</h1>"

    #return (encrypt_txt)
    #error = "'{0}'".format(crossed_off_movie)

    return  form.format(encrypt_txt)

@app.route("/")
def index():
    #return form.format('{0}',"")
    return form.format("")
app.run()