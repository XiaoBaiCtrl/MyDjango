# 例子：books/models.py

from django.db import models

class BookInfo(models.Model):
    # 定义书籍信息模型的字段
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    # 其他字段...

    def __str__(self):
        return self.title
