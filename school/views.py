from .models import ClassRoom, Speciality, Level, Classe, Matter, Program, Lecon, Question, Reponse
from .serializers import SpecialitySerializer, LevelSerializer, ClasseSerializer, MatterSerializer, LeconSerializer, QuestionSerializer, ReponseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import ProgramSerializer
from datetime import date, timedelta, datetime
from django.db.models import F
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from django.core import serializers

class SpecialityList(generics.ListCreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class LevelList(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    
class ClasseList(generics.ListCreateAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    
class MatterList(generics.ListCreateAPIView):
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer
    
class SpecialityAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class LevelAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class ClasseAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    
class MatterAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matter.objects.all()
    serializer_class = MatterSerializer

class ProgramView(viewsets.ViewSet):
    def list(self, request):
        queryset = Program.objects.all()
        serializer = ProgramSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def program_by_matter(self, request, pk_matter):
        try:
            # queryset = Program.objects.all()
            matter = Matter.objects.get(pk=pk_matter)
            program = matter.matter_program.all()
            serializer = ProgramSerializer(program, many=True)
            return Response(serializer.data)
        except Matter.DoesNotExist:
            return Response({'error': 'this matter not exist'},status=status.HTTP_404_NOT_FOUND)
 
    
    def retrieve(self, request, pk=None):
        queryset = Program.objects.all()
        program = get_object_or_404(queryset, pk=pk)
        serializer = ProgramSerializer(program)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = Program.objects.all()
        program = get_object_or_404(queryset, pk=pk)

        serializer = ProgramSerializer(program, data=request.data, partial=True)
  
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):

        if request.data["duration"] < 3 :
            return Response({'error': 'max size of duration is 3 hours'},status=status.HTTP_404_NOT_FOUND)
        if request.data["duration"] < 1 :
            return Response({'error': 'min size of duration is 1 hours'},status=status.HTTP_404_NOT_FOUND)
        
        limit_day = datetime.strptime(request.data["limit_day"], '%Y-%m-%d').date()
        if limit_day < date.today() + timedelta(days=2):
            return Response({'error': "the deadline is less than today's date or the number of days between these dates is not at least two days"}, status=status.HTTP_404_NOT_FOUND)

        course_day = limit_day + timedelta(days=2)
        request.data['course_day'] = course_day
        request.data['status'] = False

        # controller que deux cours ne passe pas la meme heure
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            program = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


    # def get_permissions(self):
    #     if self.action == 'create' or self.action == 'update':
    #         permission_classes = [permissions.IsAuthenticated, IsAdminUser]
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]


class LeconView(viewsets.ViewSet):
    def list(self, request):
        queryset = Lecon.objects.all()
        serializer = LeconSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Lecon.objects.all()
        lecon = get_object_or_404(queryset, pk=pk)
        serializer = LeconSerializer(lecon)
        return Response(serializer.data)
    
    def get_lecon(self, request, pk_program):
        program = Program.objects.get(pk=pk_program)
        lesson = Lecon.objects.filter(program=program)
        print( "le pay est bios ", len(lesson))
        if len(lesson) == 0 :
            return Response({'error': 'the content is not aviable'}, status=status.HTTP_404_NOT_FOUND)
        
        serializers = LeconSerializer(lesson[0])
        return Response(serializers.data, status=status.HTTP_200_OK)


    def get_test(self, request, pk_program):
        data = []
        program = Program.objects.get(pk=pk_program)
        lesson = Lecon.objects.filter(program=program)
        questions = lesson[0].lecon_question.all()
        
        for question in questions:
            item = {"id": question.id, "content": question.content, "response": []}
            for rep in question.question_response.all():
                item["response"].append({
                    "id": rep.id,
                    "content": rep.content,
                    "verify": rep.verify
                })
            data.append(item)
        
        return Response(data, status=status.HTTP_200_OK)

    

    def update(self, request, pk=None):
        queryset = Lecon.objects.all()
        lecon = get_object_or_404(queryset, pk=pk)

        serializer = LeconSerializer(lecon, data=request.data, partial=True)
  
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        
        try:
            program = Program.objects.get(pk=request.data["program"])
            lesson = Lecon.objects.filter(program=program)
    
            if len(lesson) != 0:
                return Response({'error': 'the lesson has uploaded'},status=status.HTTP_404_NOT_FOUND)

        except Program.DoesNotExist:
            return Response({'error': 'this title does not exist in program'},status=status.HTTP_404_NOT_FOUND)
             
        # controller que deux cours ne passe pas la meme heure
        serializer = LeconSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            lecon = serializer.save()
            program.status = True
            program.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


    # def get_permissions(self):
    #     if self.action == 'create' or self.action == 'update':
    #         permission_classes = [permissions.IsAuthenticated, IsAdminUser]
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ReponseList(generics.ListCreateAPIView):
    queryset = Reponse.objects.all()
    serializer_class = ReponseSerializer

class ReponseAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reponse.objects.all()
    serializer_class = ReponseSerializer

def get_all_matter_class(id_class):
    all_user = ClassRoom.objects.filter(classe=id_class)
    all_teacher = all_user.filter(role=2)

@api_view(['GET'])
def active_or_desactive_lesson(request, pk_program):
    # activate or desactivate the lesson title in the program list

    program = Program.objects.get(pk=pk_program)
    program.status = not program.status
    program.save()
    data = ProgramSerializer(program).data

    return Response(data, status=status.HTTP_200_OK)
    