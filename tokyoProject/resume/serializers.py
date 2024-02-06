from rest_framework import serializers
from .models import Resume
import markdown

class ResumeSerializer(serializers.ModelSerializer):
    comment     = serializers.SerializerMethodField()
    career      = serializers.SerializerMethodField()
    name        = serializers.SerializerMethodField()
    role        = serializers.SerializerMethodField()
    salary      = serializers.SerializerMethodField()
    intro       = serializers.SerializerMethodField()
    information = serializers.SerializerMethodField()
    certificate = serializers.SerializerMethodField()
    
    class Meta:
        model = Resume
        fields = '__all__'
        
    def get_comment(self, obj):
        return markdown.markdown(obj.comment)
    
    def get_career(self, obj):
        return markdown.markdown(obj.career)
    
    def get_name(self, obj):
        return markdown.markdown(obj.name)
    
    def get_role(self, obj):
        return markdown.markdown(obj.role)
    
    def get_salary(self, obj):
        return markdown.markdown(obj.salary)
    
    def get_intro(self, obj):
        return markdown.markdown(obj.intro)
    
    def get_information(self, obj):
        return markdown.markdown(obj.information)
    
    def get_certificate(self, obj):
        return markdown.markdown(obj.certificate)
    
