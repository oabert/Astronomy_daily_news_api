import requests
import streamlit as st

api_key = '0eVtpdRPbfsGJsg6kHImydqk5pBSMhZkr5JKcDUd'

url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

# Get request data as dictionary
response_data = requests.get(url)
content = response_data.json()

title = content['title']
image_url = content['url']
date = content['date']
explanation = content['explanation']

# Download image
image_path = 'img.png'
response_image = requests.get(image_url)

with open(image_path, 'wb') as image_file:
       image_file.write(response_image.content)

st.title('Daily new astronomy facts')
st.subheader('This is daily changed astronomy picture')
st.write('This page will show you new astronomy picture every day. Enjoy!')
st.image(image_path)
st.write(explanation)
st.write(date)
