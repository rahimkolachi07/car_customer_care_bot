import pathlib
import textwrap
from gemini.scarping import*
from gemini.data_extract import*
from gemini.reguler import*

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

model = genai.GenerativeModel('gemini-pro')
previous_data = scrp()
urls = load_urls_from_json()
car_data = extract_car_data(urls)
car_names = extract_car_titles(car_data)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import os
os.environ['GOOGLE_API_KEY']="AIzaSyC01V-IT4_FVNJwIsiHipCbIRzPm3H3vFk"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    pass
txt =[]
txt.append("hello, autobot, introduce your self")
resp=[]
z=0
def g_model(text):
    txt.append(text)
    if z==0:
       response = model.generate_content(f"act as customer care for autbot company. dont mention you are bot, bot name is alen, you are an customer care reprasentive. autobot is car selling, car repairing, car insurance company. past user inputs={resp}, past bot response ={txt}. now give the answare based on new user request={text}. all text must be in hebrow languages")
    elif z>0:
       response = model.generate_content(f" past user inputs={resp}, past bot response ={txt}, continue the conversation and this is user new  request={text}. all text must be in hebrow languages")
    resp.append(response)
    if 'buy' in text or 'buy car' in text:
        response = model.generate_content(f"past user inputs={resp}, past bot response ={txt}, continue the conversation and this is user new request={text}. all text must be in hebrow languages. show him the catalogue of car from carnames = {car_names}. response must be attractive so user can buy the car.")
    # If the car is found, include its action_url and image_url in the input
    if extract_car_info(text) is not None:
        car_name, model_number, year = extract_car_info(text)
        query = car_name+" "+model_number+" "+year
        print(query)
        most_similar = most_similar_text(query, car_names)
        print(most_similar)
        action_url, image_url = search_car_by_name(most_similar, car_data)
        response = model.generate_content(f"past user inputs={txt}, past bot response ={resp}, continue the conversation. all text must be in hebrow languages.  this is our website https://autobot.co.il/  mention this website and  car action_url ={action_url} and the car image_url ={image_url}.")
        
    return response.text


