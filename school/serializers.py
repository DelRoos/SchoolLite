from django.db import models
from .models import Classe, Matter, Program, Lecon, Question, Reponse, ClassRoom
from rest_framework import serializers

# class SpecialitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Speciality
#         fields = '__all__'
        
# class LevelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Level
#         fields = '__all__'
    
class ClasseSerializer(serializers.ModelSerializer):
    # level = LevelSerializer(many=False)
    # speciality = SpecialitySerializer(many=False)
    
    class Meta:
        model = Classe
        fields = '__all__'
        
    def validate(self, data):
        query = []
        query = Classe.objects.filter(level=data['level'], speciality=data['speciality'])
        # print(query)
        if len(query) > 0:
            raise serializers.ValidationError("this class already exists")
        return data
        
class MatterSerializer(serializers.ModelSerializer):
    # classe = ClasseSerializer(many=False)
    # teacher = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Matter
        fields = '__all__'
            
    def validate(self, data):
        query = Matter.objects.filter(classe=data['classe'], matter=data['matter'])
        if len(query) > 0 :
            raise serializers.ValidationError("the subject has already been assigned to another teacher")

        get_teacher_have_spec = ClassRoom.objects.filter(user__departement=data['matter'], classe=data['classe'])
        if len(get_teacher_have_spec) > 0 :
            raise serializers.ValidationError("No teacher from {} department teaches this class".format(data['matter']))

        return data

        
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class LeconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecon
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'
