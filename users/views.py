from django.contrib.auth.models import User
from .models import Roles, NewUser, Departement
from school.models import Classe, ClassRoom
from .serializers import RolesSerializer, DepartementSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import NewUser
from .serializers import UserSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class RolesList(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class DepartementList(generics.ListCreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    
class UserList(generics.ListAPIView):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
        
class RolesAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

class DepartementAct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class UserView(viewsets.ViewSet):
    def list(self, request):
        queryset = NewUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = NewUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = NewUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        
        try:
            if user.role.id != request.data['role'] :
                return Response({'message': 'cannot change roleof user'},status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            pass
            
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def create(self, request):
        id_role = request.data.pop('role')
        if id_role == 2:
            id_dep = request.data.pop('dep')
        id_classes = request.data.pop('classes')
        
        try:
            id_role = int(id_role)
            role = Roles.objects.get(pk=id_role)
        except Roles.DoesNotExist:
            return Response({'message': 'this role not exist'},status=status.HTTP_404_NOT_FOUND)
        
        if id_role == 2:    
            try:
                id_dep = int(id_dep)
                dep = Departement.objects.get(pk=id_dep)
            except Departement.DoesNotExist:
                return Response({'message': 'this departement not exist'},status=status.HTTP_404_NOT_FOUND)
        
        classes = []
        for id in id_classes: 
            try:
                id = int(id)
                item = Classe.objects.get(pk=id)
                classes.append(item)
            except Classe.DoesNotExist:
                return Response({'message': 'this classe not exist'},status=status.HTTP_404_NOT_FOUND)
           
        if len(classes) == 0:
            return Response({'message': 'classe not exist'},status=status.HTTP_404_NOT_FOUND)
        
        if role.id == 1 and not len(classes)==1 :
            return Response({'message': 'student don\'t have many classe'},status=status.HTTP_404_NOT_FOUND)
        if role.id == 2:
           request.data['departement'] = dep.pk
        request.data['role'] = role.pk
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            for classe in classes:
                try:
                    classroom = ClassRoom.objects.get(user=user, classe=classe)
                    return Response({'message': 'this teacher give courses in classe {} {}'.format(classe.id, classe.speciality)},status=status.HTTP_404_NOT_FOUND)
                except ClassRoom.DoesNotExist:
                    classroom = ClassRoom.objects.create(user=user, classe=classe) 
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        queryset = NewUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        
        try:
            if user.role.id != request.data['role'] :
                return Response({'message': 'cannot change roleof user'},status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            pass

        user.delete()

        return Response({'message': 'the user has been successfully deleted'})
    
    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.action == 'list':
    #         permission_classes = [permissions.IsAuthenticated]
    #     elif self.action == 'destroy' or self.action == 'create' or self.action == 'update':
    #         permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    #     else:
    #         permission_classes = [permissions.IsAuthenticated]
    #     return [permission() for permission in permission_classes]

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)