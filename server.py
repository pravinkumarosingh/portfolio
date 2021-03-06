from flask import Flask, render_template, url_for,request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def default():
    return render_template('index.html')


# @app.route('/index.html')
# def home():
#     return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')


# @app.route('/components.html')
# def components():
#     return render_template('components.html')

@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)



# def write_to_file(data):
#     with open("database.txt", mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')



def write_to_csv(data):
    with open("database.csv", mode='a', newline='') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_file = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong"


