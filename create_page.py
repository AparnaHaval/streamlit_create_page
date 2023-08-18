from urllib.request import AbstractDigestAuthHandler
import streamlit as st 
import pandas as pd 
from pickle import load

st.title('Data Science Project')




def create_page():
	
	st.title('Myocardinal Infarction')
	st.write('Lethal outcome (cause)')
	Age = st.sidebar.slider('Choose you age', min_value=0, max_value=100)
	Systolic_BP_mmHg = st.number_input('Enter Systolic_BP(mmHg)')
	Diastolic_BP_mmHg = st.number_input('Diastolic_BP(mmHg)')
	Ventricular_fibrillation = st.sidebar.radio('Ventricular_fibrillation',[0,1])
	Myocardial_rupture = st.sidebar.radio('Myocardial_rupture',[0,1])
	Cardiogenic_shock = st.sidebar.radio('Cardiogenic_shock',[0,1])
	abc = st.selectbox('Exertional angina pectoris in the anamnesis',[1,2,3,4,5,6])
	Abcd = st.number_input('Presence of chronic Heart failure (HF) in the anamnesis')	    
	ant_im = st.number_input('Presence of an anterior myocardial infarction (left ventricular)')
	ESR = st.sidebar.slider('Erythrocyte sedimentation rate', min_value=0, max_value=100)


	data = {'AGE':Age,
	 		'S_AD_ORIT':Systolic_BP_mmHg,
			 'D_AD_ORIT':Diastolic_BP_mmHg,
	        'FIBR_JELUD':Ventricular_fibrillation,
	 		'RAZRIV':Myocardial_rupture,
	 		'K_SH_POST':Cardiogenic_shock,
			 'STENOK_AN':abc,
			 'ZSN_A' : Abcd,
			 'ant_im' : ant_im,
			 'ROE' : ESR
			}

	df = pd.DataFrame(data, index=[0])
	return df

features =create_page()
st.write(features)


if st.sidebar.button('Submit'):
	st.write(features)

	loaded_model = load(open('model.pkl','rb'))
	res = loaded_model.predict(features)
	if res == 0:
		st.write('unknown (alive)')
	elif res == 1: 
	    st.write('cardiogenic shock')
	elif res == 2: 
	    st.write('pulmonary edema')
	elif res == 3: 
	    st.write('myocardial rupture')
	elif res == 4: 
	    st.write('progress of congestive heart failure')
	elif res == 5: 
	    st.write('thromboembolism')
	elif res == 6: 
	    st.write('asystole')
	elif res == 7: 
	    st.write('ventricular fibrillation')
		
	else:
		st.write('Something wrong')

	st.write(res)

