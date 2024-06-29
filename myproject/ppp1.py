import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-ef5fed4e58754fac9a44a86666ad61b7"
}
url = "https://api.deepseek.com/chat/completions"
data = '''{
        "model": "deepseek-chat",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hello!"}
        ],
        "stream": false
      }'''
response = requests.post(url, headers=headers, data=data)

print(response.json()['choices'][0]['message']['content'])