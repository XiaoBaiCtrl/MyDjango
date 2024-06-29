from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!XXX")


# myapp/views.py
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_completion(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('userInput')
        messages = data.get('messages', [])

        # Add the system message and user message to the list
        messages.append({"role": "user", "content": user_input})
        print(messages)
        response = requests.post('https://api.deepseek.com/chat/completions', json={
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                *messages
            ],
            "stream": False
        }, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer sk-ef5fed4e58754fac9a44a86666ad61b7"
        })

        if response.status_code == 200:
            assistant_message = response.json().get('choices', [{}])[0].get('message', {})
            return JsonResponse(assistant_message)
        else:
            return JsonResponse({"error": "Failed to get response from DeepSeek API"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
# from django.http import StreamingHttpResponse
# import json
# import requests
#
# @csrf_exempt
# def chat_completion(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         user_input = data.get('userInput')
#         messages = data.get('messages', [])
#
#         # Add the system message and user message to the list
#         messages.append({"role": "user", "content": user_input})
#         print(messages)
#
#         response = requests.post('https://api.deepseek.com/chat/completions', json={
#             "model": "deepseek-chat",
#             "messages": [
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 *messages
#             ],
#             "stream": True
#         }, headers={
#             "Content-Type": "application/json",
#             "Authorization": "Bearer sk-ef5fed4e58754fac9a44a86666ad61b7"
#         }, stream=True)
#
#         def event_stream():
#             for chunk in response.iter_content(chunk_size=None):
#                 if chunk:
#                     yield chunk.decode('utf-8')
#
#         return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
#
#     return JsonResponse({"error": "Invalid request method"}, status=405)