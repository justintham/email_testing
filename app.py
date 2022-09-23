# from pyexpat import model
import dataclasses
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

def critical_email(email):
    message = Mail(
        from_email='hesheitaliabu@gmail.com',
        to_emails=email,
        subject=f"""<b>Heart Disease Prediction System</b>""",
        html_content=f"""
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">

            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                <link rel="icon" sizes="" href="https://yt3.ggpht.com/a-/AN66SAzzGZByUtn6CpHHJVIEOuqQbvAqwgPiKy1RTw=s900-mo-c-c0xffffffff-rj-k-no" type="image/jpg" />
                <title>SolarWinds Orion Email Alert Template</title>
                <style>
                    body {{
                        background-color: #f0f0f0;
                        font-family: Arial, sans-serif;
                        color: #404040;
                    }}


                    td {{
                        padding: 20px 50px 30px 50px;
                    }}

                    small,
                    .small {{
                        font-size: 12px;
                    }}

                    .footer {{
                        padding: 15px 30px;
                    }}


                    a,
                    a:hover,
                    a:visited {{
                        color: #000000;
                        text-decoration: underline;
                    }}

                    h1,
                    h2 {{
                        font-size: 22px;
                        color: #404040;
                        font-weight: normal;
                    }}

                    p {{
                        font-size: 15px;
                        color: #606060;
                    }}



                    .icon {{
                        width: 32px;
                        height: 32px;
                        line-height: 32px;
                        display: inline-block;
                        text-align: center;
                        border-radius: 16px;
                        margin-right: 10px;
                    }}

                    .critical {{
                        border-top: 20px #c05050 solid;
                        background-color: #e2afae;
                    }}

                    .critical p {{
                        color: #3d211f;
                    }}

                    .critical .icon {{
                        background-color: #c05050;
                        color: #ffffff;
                        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;        
                    }}

                    .image-contain {{
                    object-fit: contain;
                    object-position: center;
                    }}

                    </style>
            </head>

            <body style="margin: 0; padding: 0">
                <table style="border: none" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                        <td style="padding: 15px 0">
                            <table style="border: none; margin-left: auto; margin-right: auto" cellpadding="0" cellspacing="0" width="600" class="content">

                                <!-- Start: Healthy Notification -->
                                <tr>
                                    <td class="critical notification">
                                        <h1><span class="icon"><img class="icon image-contain" src="https://th.bing.com/th/id/OIP.OJ618FjGfv4ZkHmrWy44nQHaHa?w=204&h=204&c=7&r=0&o=5&dpr=1.5&pid=1.7" width="230" height="230" ></span><b>ALERT</b></h1>
                                        <p>The "Heart Disease Prediction System" has predicted you have Heart Disease</p>
                                        <p class="small" ><a href="http://test-heartdisease/">Do you want to predict again?</a></p>
                                    </td>
                                </tr>
                                <!-- End: Healthy Notification -->
                            </table>
                        </td>
                    </tr>
                </table>
            </body>

            </html>            
            """)
    Sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('MyAPI'))
    Sg.send(message)

def healthy_email(email):
    message = Mail(
        from_email='hesheitaliabu@gmail.com',
        to_emails=email,
        subject=f"""<b>Heart Disease Prediction System</b>""",
        html_content=f"""
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">

            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                <link rel="icon" sizes="" href="https://yt3.ggpht.com/a-/AN66SAzzGZByUtn6CpHHJVIEOuqQbvAqwgPiKy1RTw=s900-mo-c-c0xffffffff-rj-k-no" type="image/jpg" />
                <title>SolarWinds Orion Email Alert Template</title>
                <style>
                    body {{
                        background-color: #f0f0f0;
                        font-family: Arial, sans-serif;
                        color: #404040;
                    }}


                    td {{
                        padding: 20px 50px 30px 50px;
                    }}

                    small,
                    .small {{
                        font-size: 12px;
                    }}

                    .footer {{
                        padding: 15px 30px;
                    }}


                    a,
                    a:hover,
                    a:visited {{
                        color: #000000;
                        text-decoration: underline;
                    }}

                    h1,
                    h2 {{
                        font-size: 22px;
                        color: #404040;
                        font-weight: normal;
                    }}

                    p {{
                        font-size: 15px;
                        color: #606060;
                    }}



                    .icon {{
                        width: 32px;
                        height: 32px;
                        line-height: 32px;
                        display: inline-block;
                        text-align: center;
                        border-radius: 16px;
                        margin-right: 10px;
                    }}
                    .healthy {{
                        border-top: 20px #80c080 solid;
                        background-color: #c6e2c3;
                    }}

                    .healthy p {{
                        color: #364731;
                    }}

                    .healthy .icon {{
                        background-color: #80c080;
                        color: #ffffff;
                    }}
                    .image-contain {{
                    object-fit: contain;
                    object-position: center;
                    }}

                    </style>
            </head>

            <body style="margin: 0; padding: 0">
                <table style="border: none" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                        <td style="padding: 15px 0">
                            <table style="border: none; margin-left: auto; margin-right: auto" cellpadding="0" cellspacing="0" width="600" class="content">

                                <!-- Start: Healthy Notification -->
                                <tr>
                                    <td class="healthy notification">
                                        <h1><span class="icon"><img class="icon image-contain" src="https://www.bing.com/th?id=OIP.uook2b6YTHNIbrRyvPXnPAHaHy&w=161&h=170&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2" width="230" height="230" ></span>Healthy</h1>
                                        <p>The "Heart Disease Prediction System" has predicted you don't have Heart Disease</p>
                                        <p class="small" ><a href="http://test-heartdisease/">Do you want to predict again?</a></p>
                                    </td>
                                </tr>
                                <!-- End: Healthy Notification -->
                            </table>
                        </td>
                    </tr>
                </table>
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
        # redirect(f"/email_verify/{email}")
        redirect(f"/about_us_page/{email}")
        redirect(f"/graph_page/{email}")
        return render_template('main.html')
    return render_template('login.html')

# @app.route('/email_verify/<email>')
# def email_verify(email):
#     email_verification(email)
#     # send_email(email)
#     return render_template('email_verify.html')


@app.route("/about_us_page/<email>", methods=['GET', 'POST'])
def about_us(email):
    return render_template('about_us.html',email=email)

@app.route("/signup_page", methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@app.route("/predict_page/<email>", methods=['GET', 'POST'])
def predict_page(email):
    if request.method == "POST":
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
            healthy_email(email)
            return render_template('main.html', email= email, prediction_text='The patient does not have Heart Disease' )
        else:
            critical_email(email)
            return render_template('main.html', email= email,prediction_text='The patient has Heart Disease' )

    return render_template('main.html',email=email)


@app.route("/graph_page/<email>", methods=['GET', 'POST'])
def graph_page(email):
    return render_template('graph.html',email=email)

# @app.route('/predict/<email>',methods=['GET', 'POST'])
# def predict(email):
#     '''
#     For rendering results on HTML GUI
#     '''
#     if prediction[0] == 0:
#         return render_template('main.html', prediction_text='The patient does not have Heart Disease' )
#     else:
#         return render_template('main.html', prediction_text='The patient has Heart Disease' )



if __name__ == "__main__":
    app.run(debug=True)