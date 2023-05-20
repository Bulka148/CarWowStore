import json
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets
from CarWowStore.settings import EMAIL_ADDRESS, EMAIL_PASSWORD


class forgot_password(viewsets.ViewSet):
    def set_new_password(self, request):
        data = json.loads(request.body)
        user = User.objects.get(email=data['email'])
        user.set_password(data['password'])
        user.save()
        return JsonResponse({'result': 'OK'})

    def get_recovery_code(self, request):
        recovery_code = str(random.randint(1000, 9999))
        text = MIMEMultipart()
        msgText = MIMEText(f'<h3>Код: {recovery_code}</h3>', 'html')
        text.attach(msgText)
        text['Subject'] = 'CarWowStore password recovering'
        text['From'] = EMAIL_ADDRESS
        text['To'] = request.GET.get('email')
        smtpObj = smtplib.SMTP('smtp.yandex.ru', 587)
        smtpObj.starttls()
        smtpObj.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtpObj.sendmail(text['From'], text['To'], text.as_string().encode())
        return JsonResponse({'result': recovery_code})


