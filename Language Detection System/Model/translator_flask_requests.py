import requests

url = 'http://localhost:5000/translate'
data = {'text': 'Hello', 'target_lang': 'yo'}

response = requests.post(url, json=data)
if response.ok:
    translated_text = response.json()['translated_text']
    print(translated_text)
else:
    print("Error:", response.text)
