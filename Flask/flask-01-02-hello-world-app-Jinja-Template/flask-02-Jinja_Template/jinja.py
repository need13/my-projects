from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 167800, number2 = 2567800)

@app.route('/sum')
def number():
    var1, var2 = 45677, 234570
    return render_template('body.html', value1 = var1, value2 = var2, sum = var1*var2)


if __name__ == '__main__':
    app.run(debug=True)