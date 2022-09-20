# from pyexpat import model
import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, url_for
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd
import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

app = Flask(__name__)

# 

def get_algorithm(x):
    x=int(x)
    if x == 0:
        model = pickle.load(open('algorithm/model_rf.pkl', 'rb'))
    elif x == 1:
        model = pickle.load(open('algorithm/model_gb.pkl', 'rb'))
    elif x == 2:
        model = pickle.load(open('algorithm/model_knn.pkl', 'rb'))
    elif x == 3:
        model = pickle.load(open('algorithm/model_svm.pkl', 'rb'))
    elif x == 4:
        model = pickle.load(open('algorithm/model_dt.pkl', 'rb'))
    elif x == 5:
        model = pickle.load(open('algorithm/model_log.pkl', 'rb'))
    elif x == 6:
        model = pickle.load(open('algorithm/model_gnb.pkl', 'rb'))
    return model

def send_email(email):
    message = Mail(
        from_email='hesheitaliabu@gmail.com',
        to_emails=email,
        subject='testing 123',
        html_content='<strong>testing 123</strong>')
    Sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('MyAPI'))
    Sg.send(message)

def email_verification(email):
    message = Mail(
        from_email='hesheitaliabu@gmail.com',
        to_emails=email,
        subject='HEY BABYYYYYYYYYYYYYYYYYYY',
        html_content=f"""
            <!DOCTYPE html>
            <html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
            <head>
                <meta charset="utf-8"> <!-- utf-8 works for most cases -->
                <meta name="viewport" content="width=device-width"> <!-- Forcing initial-scale shouldn't be necessary -->
                <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Use the latest (edge) version of IE rendering engine -->
                <meta name="x-apple-disable-message-reformatting">  <!-- Disable auto-scale in iOS 10 Mail entirely -->
                <title></title> <!-- The title tag shows in email notifications, like Android 4.4. -->

                <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700" rel="stylesheet">

            </head>

            <body width="100%" style="margin: 0; padding: 0 !important; mso-line-height-rule: exactly; background-color: #f1f1f1;">
                <center style="width: 100%; background-color: #f1f1f1;">
                <div style="display: none; font-size: 1px;max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden; mso-hide: all; font-family: sans-serif;">
                &zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
                </div>
                <div style="max-width: 600px; margin: 0 auto;" class="email-container">
                    <!-- BEGIN BODY -->
                <table align="center" role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: auto;">
                    <tr>
                    <td valign="top" class="bg_white" style="padding: 1em 2.5em 0 2.5em;">
                        <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                            <tr>
                                <td class="logo" style="text-align: center;">
                                    <h1><a href="#">e-Verify</a></h1>
                                </td>
                            </tr>
                        </table>
                    </td>
                    </tr><!-- end tr -->
                    <tr>
                    <td valign="middle" class="hero bg_white" style="padding: 3em 0 2em 0;">
                        <img src="https://cdn.onlinewebfonts.com/svg/img_500737.png" alt="" style="width: 300px; max-width: 600px; height: auto; margin: auto; display: block;">
                    </td>
                    </tr><!-- end tr -->
                            <tr>
                    <td valign="middle" class="hero bg_white" style="padding: 2em 0 4em 0;">
                        <table>
                            <tr>
                                <td>
                                    <div class="text" style="padding: 0 2.5em; text-align: center;">
                                        <h3>Amazing deals, updates, interesting news right in your inbox</h3>
                                        # <p><a href= "https://test-emil-heartdisease.herokuapp.com/result_verify" class="btn btn-primary" style="border: radius 5px;background: #30e3ca;color: #ffffff;padding: 10px 15px;display: inline-block">{email}</a></p>
                                        <button onclick="myFunction()">Replace document</button>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </td>
                    </tr><!-- end tr -->
                <!-- 1 Column Text + Button : END -->
                </table>
                </div>
            </center> 
            <script>
            function myFunction() {{
                location.assign = "http://127.0.0.1:5000/result_verify";
            }}
            </script>
            </body>
            </html>
            """)
    Sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('MyAPI'))
    Sg.send(message)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/login_page", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        # return redirect(f"/success/{email}")
        redirect(f"/email_verify/{email}")
    return render_template('login.html')

@app.route('/email_verify/<email>')
def email_verify(email):
    email_verification(email)
    # send_email(email)
    return render_template('email_verify.html')

@app.route('/result_verify')
def result_verify():
    return render_template('result_verify.html')

@app.route("/about_us_page", methods=['GET', 'POST'])
def about_us():
    return render_template('about_us.html')

@app.route("/signup_page", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        # return redirect(f"/success/{email}")
        redirect(f"/email_verify/{email}")
    return render_template('signup.html')

@app.route("/predict_page", methods=['GET', 'POST'])
def predict_page():
    # redirect(url_for('success'))
    return render_template('main.html')


@app.route("/graph_page", methods=['GET', 'POST'])
def graph_page():
    return render_template('graph.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    age = request.form.get("age")
    sex = request.form.get("sex")
    cp = request.form.get("cp")
    trestbps = request.form.get("trestbps")
    chol = request.form.get("chol")
    fbs = request.form.get("fbs")
    restecg = request.form.get("restecg")
    thalach = request.form.get("thalach")
    oldpeak = request.form.get("oldpeak")
    exang = request.form.get("exang")
    slope = request.form.get("slope")
    ca = request.form.get("ca")
    thal = request.form.get("thal")
    algorithm = request.form.get("algorithm")
    data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    data = list(np.float_(data))
    result = get_algorithm(algorithm)
    scaler2 = StandardScaler()
    ##CHANGE THE INPUT TO NUMPY ARRAY
    input_data_as_numpy_array = np.asarray(data)
    #RESHAPE THE NUMPY ARRAY BECAUSE WE NEED TO PREDICT THE TARGET
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    std_data = scaler2.fit_transform(input_data_reshaped)
    prediction = result.predict(input_data_reshaped)
    if prediction[0] == 0:
        return render_template('main.html', prediction_text='The patient does not have Heart Disease' )
    else:
        return render_template('main.html', prediction_text='The patient has Heart Disease' )



if __name__ == "__main__":
    app.run(debug=True)