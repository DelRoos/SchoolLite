from django.db import models
from django.db.models.query import QuerySet
from .models import NewUser
from rest_framework import serializers
from school.models import ClassRoom, Classe

# class RolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roles
#         fields = '__all__'
        
# class DepartementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Departement
#         fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    classes = serializers.SerializerMethodField()
    # role = serializers.SerializerMethodField()
    # departement = serializers.SerializerMethodField()
    
    class Meta:
        model = NewUser
        fields = ['id', 'matricule', 'email', 'username', 'first_name', 'password','born_at', 'gender', 'role', 'departement','classes']
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    # def get_role(self, obj):
    #     return {'id': obj.role.id, 'describe': obj.role.describe}

    # def get_departement(self, obj):
    #     return {'id': obj.departement.id, 'describe': obj.departement.name}
    
    def get_classes(self, obj):
        classRoom = obj.classroom_user.all()
        classes = []
        for item in classRoom:
            classes.append({"id": item.classe.pk,
                      "level": item.classe.level,
                      "speciality": item.classe.speciality
                    })
            
        print(classes)
        return classes
        
    def validate(self, data):
        
        # if data['role'] == 1 and data['departement'] != None:
        #     raise serializers.ValidationError("students do not have a department")
        
        # if data['role'] == 2 and data['departement'] != None:
        #     raise serializers.ValidationError("the teacher must have a department")
        
        # if not data['gender'] :
        #     raise serializers.ValidationError("please fill the field gender")

        # if not data['role'] :
        #     raise serializers.ValidationError("please fill the field role")     
        return data