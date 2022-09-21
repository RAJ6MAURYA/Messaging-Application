from flask import Flask, render_template, request
import client as cl
app = Flask(__name__)

messages = []


@app.route('/', methods=['GET', "POST"])
def client():
    cl.init()
    if(request.method == 'POST'):
        message = request.form.get('message')
        messages.append(message)
        cl.send(message)
        return render_template("client.html", message="".join(messages))

    else:
        message = ""
        return render_template("client.html")


if __name__ == '__main__':
    app.run(debug=True)
