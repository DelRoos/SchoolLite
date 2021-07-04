from users.models import NewUser
from django.db import models
from .models import Classe, Matter, Program, Lecon, Question, Reponse, ClassRoom, TestResults
from rest_framework import serializers

# class SpecialitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Speciality
#         fields = '__all__'
        
# class LevelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Level
#         fields = '__all__'

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
    
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

class TestResultSerializer(serializers.ModelSerializer):
    # classe = ClasseSerializer(many=False)
    # teacher = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = TestResults
        fields = '__all__'
            
    def validate(self, data):
        
        lessons = Lecon.objects.filter(pk=data['lesson'])
        testResult = TestResults.objects.filter(lesson=data['lesson'], student=data['student'])

        if len(testResult) == 0:
            if 0 <= data['note'] <= 20:
                if len(lessons) > 0:
                    questions = lessons[0].lecon_question.all()
                    if len(questions) > 0:
                        try:
                            user = NewUser.objects.get(pk=data['student'])
                            if user.role == 'stud':
                                if len(user.classroom_user.all()) == 1 and user.classroom_user.all()[0].classe == data['classe']:
                                    return data
                                else:
                                    raise serializers.ValidationError('the user is not in this class')
                            else:
                                raise serializers.ValidationError('the user is not a student')
                        except NewUser.DoesNotExist:
                            raise serializers.ValidationError('user does not exist')
                    else:    
                        raise serializers.ValidationError('the tests of this lesson have not been uploaded')
                else:
                    raise serializers.ValidationError('the lesson does not exist')
            else:
                raise serializers.ValidationError('the score must be in the range [0..20].')
        else:
            raise serializers.ValidationError('the test has already been noted')
