import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image



st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open(f'{working_dir}/saved_models/breast_cancer_model.sav', 'rb'))

liver_disease_model = pickle.load(open(f'{working_dir}/saved_models/liver_model.sav', 'rb'))


Img = ('C:/Users/tusha/Desktop/Multiple_Disease_Prediction_webapp/image/')

with st.sidebar:

    selected = option_menu('Main Menu',
                           ['Home',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson`s Prediction',
                            'Liver Disease Prediction',
                            'Breast Cancer Prediction',
                            ],
                           menu_icon='menu',
                           icons=['house','activity', 'heart', 'person','clipboard-pulse','gender-female'],
                           default_index=0)
    
    st.subheader('Presented By : ')
    st.markdown('1.Hazira Idrisi')
    st.markdown('2.Tushar Ramani')
    st.markdown('3.Pushpak Patel')
    
    st.subheader('Guided By : ')
    st.markdown('Abdul Aziz Md, Master Trainer, Edunet Foundation.')


# Diabetes Prediction

if selected == 'Home':
    
    image = Image.open(Img+ "logo.png") 
    st.image(image, caption='') 

    st.markdown("This Web Application is designed to help users predict the likelihood of developing certain diseases based on their input features. With the use of trained and tested machine learning models, we provide predictions for **Diabetes, Heart Disease, Parkinson`s Disease, Breast Cancer and Liver Disease.**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        image = Image.open(Img+ "d1.jpg") 
        st.image(image, caption='Diabetes Prediction',width=200) 
        
    with col2:
         image = Image.open(Img+ "heart_1.jpg") 
         st.image(image, caption='Heart Disease Prediction',width=200)

    with col3:
        image = Image.open(Img+ "p_1.jpg") 
        st.image(image, caption='Parkinson`s Prediction',width=200)
    
    with col1:
        image = Image.open(Img+ "b1.jpg") 
        st.image(image, caption='Breast Cancer Prediction',width=200)
        
    with col3:
        image = Image.open(Img+ "L1.jpg") 
        st.image(image, caption='Liver Disease Prediction',width=200)
    
        
    st.header("How to Use :")
    
    st.markdown("- Navigate to the Main Menu(>) located in the top-left corner of the screen.")
    st.markdown("- Click on the desired tab among 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson`s Prediction', 'Breast Cancer Prediction', 'Liver Disease Prediction' and 'Lung Cancer' to access prediction tools for specific diseases.")
    st.markdown("- Enter relevant information as requested in the input fields.")
    st.markdown("- Click on the **'Test Result'** button to obtain predictions based on the provided data.")

    st.header("Disclaimer :")
 
    st.markdown("- This Web App may not provide accurate predictions at all times. When in doubt, please enter the values again and verify the predictions.")
    st.markdown("- It is important to note that individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.")



# Diabetes Prediction

if selected == 'Diabetes Prediction':
    
    st.markdown("<h1 style='text-align: center;; color: #4783c4;font-size:50px;'>Diabetes Prediction using ML</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        image = Image.open(Img+ "dib.jpg")
        st.image(image, caption='')
    
    name = st.text_input("Enter Your Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    diab_diagnosis = ''


    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            image = Image.open(Img+'pav.png')
            st.image(image, caption='')
            diab_diagnosis = name + ' : We are really sorry to say but it seems like you are Diabetic.'
        else:
            image = Image.open(Img+'nav.png')
            st.image(image, caption='')
            diab_diagnosis = 'Congratulation '+name+' You are not diabetic'

    st.success(diab_diagnosis)
    
# Heart Disease Prediction

if selected == 'Heart Disease Prediction':
    st.markdown("<h1 style='text-align: center;; color: #4783c4;font-size:50px;'>Heart Disease Prediction using ML</h1>", unsafe_allow_html=True)

    
    col1, col2, col3 = st.columns(3)
    
   
    with col2:
        image = Image.open(Img+ "heart.jpg")
        st.image(image, caption='',width=300)
   

    name = st.text_input("Enter Your Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Enter your age: ')

    with col2:
        sex=0
        display = ("Male", "Female")
        options = list(range(len(display)))
        value = st.selectbox("Gender", options, format_func=lambda x: display[x])
        if value == "Male":
            sex = 1
        elif value == "Female":
            sex = 0

    with col3:
        cp = st.selectbox('Chest pain type',(0,1,2,3))

    with col1:
        trestbps = st.text_input('Resting blood pressure: ')

    with col2:
        chol = st.text_input('Serum cholestoral in mg/dl: ')

    with col3:
        fbs = st.selectbox('Fasting blood sugar',(0,1))

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results: ',(0,1))

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved: ')

    with col3:
        exang = st.selectbox('Exercise Induced Angina: ',(0,1))

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise: ')

    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment: ',(0,1,2))

    with col3:
        ca = st.selectbox('Major vessels colored by flourosopy',(0,1,2,3))

    with col1:
        thal = st.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',(0,1,2))

    heart_diagnosis = ''


    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            image = Image.open(Img+'pav.png')
            st.image(image, caption='')
            heart_diagnosis = name+' : we are really sorry to say but it seems like you have Heart Disease.'
        else:
            image = Image.open(Img+'nav.png')
            st.image(image, caption='')
            heart_diagnosis = "Congratulation "+name+" You don't have Heart Disease."

    st.success(heart_diagnosis)
    
# Parkinsons Prediction
    
if selected == "Parkinson`s Prediction":
    
    st.markdown("<h1 style='text-align: center;; color: #4783c4;font-size:50px;'>Parkinson`s Disease Prediction using ML</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        image = Image.open(Img+ "ParkinsonsDisease.png")
        st.image(image, caption='')

   
    name = st.text_input("Enter Your Name:")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz) ex: 50 above')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz) ex: 100 above')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz) ex: 50 above')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%) ex: 0.00 to 0.9')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs) ex: 0.00 to 0.9')

    with col1:
        RAP = st.text_input('MDVP:RAP ex: 0.00 to 0.9')

    with col2:
        PPQ = st.text_input('MDVP:PPQ ex: 0.00 to 0.9')

    with col3:
        DDP = st.text_input('Jitter:DDP ex: 0.00 to 0.9')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer ex: 0.00 to 0.9')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB) ex: 0.00 to 0.9')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3 ex: 0.00 to 0.9')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5 ex: 0.00 to 0.9')

    with col3:
        APQ = st.text_input('MDVP:APQ ex: 0.00 to 0.9')

    with col4:
        DDA = st.text_input('Shimmer:DDA ex: 0.00 to 0.9')

    with col5:
        NHR = st.text_input('NHR ex: 0.00 to 0.9')

    with col1:
        HNR = st.text_input('HNR ex: 0 to 30')

    with col2:
        RPDE = st.text_input('RPDE ex: 0.00 to 0.9')

    with col3:
        DFA = st.text_input('DFA ex: 0.00 to 0.9')

    with col4:
        spread1 = st.text_input('spread1 ex: -0.00 to -10.00')

    with col5:
        spread2 = st.text_input('spread2 ex: 0.00 to 0.9')

    with col1:
        D2 = st.text_input('D2 ex: 0.00 to 4.00')

    with col2:
        PPE = st.text_input('PPE ex: ex: 0.00 to 0.9')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson`s Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            image = Image.open(Img+'pav.png')
            st.image(image, caption='')
            parkinsons_diagnosis = name + ' : we are really sorry to say but it seems like you have Parkinson disease'
        else:
            image = Image.open(Img+'nav.png')
            st.image(image, caption='')
            parkinsons_diagnosis = "Congratulation "+name+" You don't have Parkinson disease"

    st.success(parkinsons_diagnosis)
    
# Breast Cancer Detection
   
if selected == 'Breast Cancer Prediction':
    
    st.markdown("<h1 style='text-align: center;; color: #4783c4;font-size:50px;'>Breast Cancer Prediction using ML</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        image = Image.open(Img+ "breast.jpg")
        st.image(image, caption='')

    
    name = st.text_input("Enter Your Name:")
    col1, col2, col3 = st.columns(3)

        
    with col1:
        radius_mean = st.slider("Enter your Radius Mean", 6.0, 30.0, 15.0)
        texture_mean = st.slider("Enter your Texture Mean", 9.0, 40.0, 20.0)
        perimeter_mean = st.slider("Enter your Perimeter Mean", 43.0, 190.0, 90.0)
        area_mean = st.slider("Enter your Area Mean", 143.0, 2501.0, 750.0)
        smoothness_mean = st.slider("Enter your Smoothness Mean", 0.05, 0.25, 0.1)
        compactness_mean = st.slider("Enter your Compactness Mean", 0.02, 0.3, 0.15)
        concavity_mean = st.slider("Enter your Concavity Mean", 0.0, 0.5, 0.2)
        concave_points_mean = st.slider("Enter your Concave Points Mean", 0.0, 0.2, 0.1)
        symmetry_mean = st.slider("Enter your Symmetry Mean", 0.1, 1.0, 0.5)
        fractal_dimension_mean = st.slider("Enter your Fractal Dimension Mean", 0.01, 0.1, 0.05)
    
    with col2:
        radius_se = st.slider("Enter your Radius SE", 0.1, 3.0, 1.0)
        texture_se = st.slider("Enter your Texture SE", 0.2, 2.0, 1.0)
        perimeter_se = st.slider("Enter your Perimeter SE", 1.0, 30.0, 10.0)
        area_se = st.slider("Enter your Area SE", 6.0, 500.0, 150.0)
        smoothness_se = st.slider("Enter your Smoothness SE", 0.001, 0.03, 0.01)
        compactness_se = st.slider("Enter your Compactness SE", 0.002, 0.2, 0.1)
        concavity_se = st.slider("Enter your Concavity SE", 0.0, 0.05, 0.02)
        concave_points_se = st.slider("Enter your Concave Points SE", 0.0, 0.03, 0.01)
        symmetry_se = st.slider("Enter your Symmetry SE", 0.1, 1.0, 0.5)
        fractal_dimension_se = st.slider("Enter your Fractal Dimension SE", 0.01, 0.1, 0.05)

    with col3:
        radius_worst = st.slider("Enter your Radius Worst", 7.0, 40.0, 20.0)
        texture_worst = st.slider("Enter your Texture Worst", 12.0, 50.0, 25.0)
        perimeter_worst = st.slider("Enter your Perimeter Worst", 50.0, 250.0, 120.0)
        area_worst = st.slider("Enter your Area Worst", 185.0, 4250.0, 1500.0)
        smoothness_worst = st.slider("Enter your Smoothness Worst", 0.07, 0.3, 0.15)
        compactness_worst = st.slider("Enter your Compactness Worst", 0.03, 0.6, 0.3)
        concavity_worst = st.slider("Enter your Concavity Worst", 0.0, 0.8, 0.4)
        concave_points_worst = st.slider("Enter your Concave Points Worst", 0.0, 0.2, 0.1)
        symmetry_worst = st.slider("Enter your Symmetry Worst", 0.1, 1.0, 0.5)
        fractal_dimension_worst = st.slider("Enter your Fractal Dimension Worst", 0.01, 0.2, 0.1)

    breast_diagnosis = ''


    if st.button('Breast Cancre Test Result'):

        user_input = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
                      radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                      radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]

        user_input = [float(x) for x in user_input]

        breast_prediction = breast_cancer_model.predict([user_input])

        if breast_prediction[0] == 1:
            image = Image.open(Img+'pav.png')
            st.image(image, caption='')
            breast_diagnosis = name+ " : we are really sorry to say but it seems like you have Breast Cancer."
        else:
            image = Image.open(Img+'nav.png')
            st.image(image, caption='')
            breast_diagnosis = "Congratulation "+name+" You don't have Breast Cancer."

    st.success(breast_diagnosis)
    
# Liver Disease Prediction

if selected == 'Liver Disease Prediction':
    
    st.markdown("<h1 style='text-align: center;; color: #4783c4;font-size:50px;'>Liver Prediction using ML</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        image = Image.open(Img+ "liver.jpg")
        st.image(image, caption='')

    name = st.text_input("Enter Your Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Entre your Age')

    with col2:
        
        Gender=0
        display = ("Male", "Female")
        options = list(range(len(display)))
        value = st.selectbox("Gender", options, format_func=lambda x: display[x])
        if value == "Male":
            Gender = 1
        elif value == "Female":
            Gender = 0

    with col3:
        Total_Bilirubin = st.text_input('Entre your Total_Bilirubin (ex:0 to 50 above, point value is also enter)')

    with col1:
        Direct_Bilirubin = st.text_input('Entre your Direct_Bilirubin (ex:0 to 50 above, point value is also enter)')

    with col2:
        Alkaline_Phosphotase = st.text_input('Entre your Alkaline_Phosphotase (ex:80 to 1500 above)')

    with col3:
        Alamine_Aminotransferase = st.text_input('Entre your Alamine_Aminotransferase (ex:10 to 1500 above)')

    with col1:
        Aspartate_Aminotransferase = st.text_input('Entre your Aspartate_Aminotransferase (ex:10 to 1500 above)')

    with col2:
        Total_Protiens = st.text_input('Entre your Total_Protiens (ex: 3.0 to 10.0 above)')

    with col3:
        Albumin = st.text_input('Entre your Albumin (ex:1.0 to 10.0 above)')

    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('Entre your Albumin_and_Globulin_Ratio (ex:0.0 to 5.0 in between')


    Liver_diagnosis = ''


    if st.button('Liver Disease Test Result'):

        user_input = [Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                      Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]

        user_input = [float(x) for x in user_input]

        liver_prediction = liver_disease_model.predict([user_input])

        if liver_prediction[0] == 1:
            image = Image.open(Img+'pav.png')
            st.image(image, caption='')
            Liver_diagnosis = name +' : we are really sorry to say but it seems like you have liver disease.'
        else:
            image = Image.open(Img+'nav.png')
            st.image(image, caption='')
            Liver_diagnosis = "Congratulation "+name+" You don't have liver disease."

    st.success(Liver_diagnosis)
    

def set_bg_from_url(url, opacity=1):
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url("https://images.everydayhealth.com/homepage/health-topics-2.jpg?w=768", opacity=0.9)