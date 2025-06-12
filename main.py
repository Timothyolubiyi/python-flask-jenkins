from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


  # return render_template("registrationform.html")
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    # app.run(debug=True, port=5002)
    app.run(host='0.0.0.0', port=5007)
