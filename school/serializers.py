from django.db import models
from .models import Speciality, Level, Classe, Matter, Program, Lecon, Question, Reponse
from rest_framework import serializers

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'
        
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
    
class ClasseSerializer(serializers.ModelSerializer):
    level = LevelSerializer(many=False)
    speciality = SpecialitySerializer(many=False)
    
    class Meta:
        model = Classe
        fields = '__all__'
        
    def validate(self, data):
        query = Classe.objects.filter(level=data['level'], speciality=data['speciality'])
        if query != None:
            raise serializers.ValidationError("this class already exists")
        return data
        
class MatterSerializer(serializers.ModelSerializer):
    classe = ClasseSerializer(many=False)
    teacher = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Matter
        fields = '__all__'
            
    def validate(self, data):
        query = Matter.objects.none(classe=data['classe'], teacher=data['teacher'])
        if query != None:
            raise serializers.ValidationError("the teaching unit is already taught by this teacher")
        
        query_matter_exist = Matter.objects.filter(classe=data['classe'])
        if query !=None and query_matter_exist!=None:
            for item in query_matter_exist :
                if item.teacher.departement == query[0].teacher.departement:
                    raise serializers.ValidationError("the teaching unit is already taught by this teacher")
                    
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
