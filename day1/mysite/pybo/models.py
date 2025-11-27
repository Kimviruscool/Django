from django.db import models

# Create your models here.

class Question(models.Model): #질문 모델 작성
    subject = models.CharField(max_length=200) #제목 = models.characterFiled 캐릭터타입 varchar와 동일 최대 200자
    content = models.TextField() # 내용 = models.TextField 텍스트타입
    create_data = models.DateTimeField() #작성일 = models.DateTimeField 날짜타입

class Answer(models.Model): #대답 모델 작성
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #대칭키 참조키 = models.ForeignKey(질문, 종속)
    content = models.TextField() #내용 = models.TextField
    create_data = models.DateTimeField() #작성일 = models.DateTimeField 날짜