from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs.10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India'
}, {
    'id': 3,
    'title': 'Associate Engineer',
    'location': 'Mumbai, India',
    'salary': 'Rs.50,00,000'
}, {
    'id': 4,
    'title': 'Web Developer',
    'location': 'Bengaluru, India',
    'salary': 'Rs.60,00,000'
}, {
    'id': 5,
    'title': 'DevOps Engineer',
    'location': 'Bengaluru, India',
    'salary': 'Rs.10,00,000'
}]


@app.route("/")
def home():
  return render_template('index.html', jobs=JOBS, company_name="Lowe's")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
