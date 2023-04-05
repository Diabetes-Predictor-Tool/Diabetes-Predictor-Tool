# #import libraries
# import numpy as np
# from flask import Flask, render_template,request
# import pickle#Initialize the flask App

# app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

# #default page of our web-app
# @app.route('/')
# def home():
#     return render_template('/templates/index.html')

#To use the predict button in our web-app
# @app.route('/predict',methods=['POST'])
# def predict():
#     #For rendering results on HTML GUI
#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#     output = round(prediction[0], 2)

#     return render_template('/templates/result.html', prediction_text=':{}'.format(output))

# @app.route('/dashboard')
# def dashboard():
#     return render_template('/templates/dashboard.html')

# @app.route('/result')
# def result():
#     return render_template('/templates/result.html')

# if __name__ == "__main__":
#     app.run(debug=False)
