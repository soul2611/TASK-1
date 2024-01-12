# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/url/task')
def task_page():
    # You can pass dynamic data to the template here if needed
    dynamic_data = "This is dynamic data!"
    return render_template('task.html', dynamic_data=dynamic_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
