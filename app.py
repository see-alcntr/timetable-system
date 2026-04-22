from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple in-memory timetable
timetable = []

@app.route('/')
def home():
    return redirect('/dashboard')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        subject = request.form['subject']
        day = request.form['day']
        time = request.form['time']

        timetable.append({
            "subject": subject,
            "day": day,
            "time": time
        })

        return redirect('/dashboard')

    return render_template('dashboard.html', timetable=timetable)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
