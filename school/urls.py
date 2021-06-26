from django.urls import path
from . import views

urlpatterns = [
    path('speciality',views.SpecialityList.as_view()),
    path('speciality/<int:pk>',views.SpecialityAct.as_view()),
    
    path('level',views.LevelList.as_view()),
    path('level/<int:pk>',views.LevelAct.as_view()),
    
    path('classe',views.ClasseList.as_view()),
    path('classe/<int:pk>',views.ClasseAct.as_view()),
    
    path('matter',views.MatterList.as_view()),
    path('matter/<int:pk>',views.MatterAct.as_view()),

    path('question',views.QuestionList.as_view()),
    path('question/<int:pk>',views.QuestionAct.as_view()),
    
    path('reponse',views.ReponseList.as_view()),
    path('reponse/<int:pk>',views.ReponseAct.as_view()),

    path('program',views.ProgramView.as_view({
            'get': 'list',
            'post': 'create',
        })),
    
    path('program/<int:pk>', views.ProgramView.as_view({
            'get': 'retrieve',
            'put': 'update',
            # 'delete': 'destroy'
        })),

    path('program_by_matter/<int:pk_matter>', views.ProgramView.as_view({
        'get' : 'program_by_matter'
    })),

    path('program/matter/<int:pk_matter>', views.ProgramView.as_view({
            'get': 'program_by_matter',
            # 'delete': 'destroy'
        })),


    path('lecon',views.LeconView.as_view({
            'get': 'list',
            'post': 'create',
        })),

    path('lecon_test/<int:pk_program>',views.LeconView.as_view({
            'get': 'get_test'
        })),

    path('active_or_desactive/<int:pk_program>',views.active_or_desactive_lesson),
    
    path('lecon/<int:pk>', views.LeconView.as_view({
            'get': 'retrieve',
            'put': 'update',
            # 'delete': 'destroy'
        })),
        
    path('lecon_by_program/<int:pk_program>',views.LeconView.as_view({
            'get': 'get_lecon',
            # 'delete': 'destroy'
        }))
        
]
