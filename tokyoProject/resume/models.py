from django.db import models

class Resume(models.Model):
    name        = models.CharField(max_length=100) # 이름
    comment     = models.TextField() # 좌우명 
    career      = models.TextField() # 경력
    role        = models.TextField() # 지원분야
    salary      = models.TextField() # 희망연봉
    intro       = models.TextField() # 자기소개
    information = models.TextField() # 개인정보
    certificate = models.TextField() # 자격정보
    photo       = models.ImageField(upload_to='resume/', null=False, blank=False)
    
    
    def __str__(self):
        return self.title