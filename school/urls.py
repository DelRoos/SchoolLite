from django.urls import path
from . import views

urlpatterns = [
    # path('speciality',views.SpecialityList.as_view()),
    # path('speciality/<int:pk>',views.SpecialityAct.as_view()),
    
    # path('level',views.LevelList.as_view()),
    #  path('level/<int:pk>',views.LevelAct.as_view()),
    
    path('classe',views.ClasseList.as_view()),
    path('classe/<int:pk>',views.ClasseAct.as_view()),
    path('classe/matter/<int:pk_classe>',views.get_all_matter_classe),
    
    path('matter',views.MatterList.as_view()),
    path('matter/<int:pk>',views.MatterAct.as_view()),

    path('question',views.QuestionList.as_view()),
    path('question/<int:pk>',views.QuestionAct.as_view()),
    
    path('test/result',views.TestResultList.as_view()),
    path('test/result/<int:pk>',views.TestResultAct.as_view()),
    # get_all_result_test_by_matter(request, pk_matter, pk_user)
    path('test/result/matter/<int:pk_matter>/<int:pk_user>', views.get_all_result_test_by_matter),

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
    
    path('teacher/add/class', views.ClassRoomView.as_view({
        'post': 'add_teach_class'
    })),

    path('teacher/remove/class/<int:pk_teach>/<int:pk_classe>', views.ClassRoomView.as_view({
        'get': 'remove_class_teach'
    })),

    path('active_or_desactive/<int:pk_program>',views.active_or_desactive_lesson),
    path('user/classe/<int:pk_classe>/<str:role>',views.get_all_user_classe),
    path('user/dept/<str:dept>',views.get_all_user_dept),
    path('user/test/result/<int:pk_user>',views.get_all_result_test_user),
    path('user/test/matter/<int:pk_user>/<int:pk_matter>',views.get_all_result_test_user_by_matter),
    path('class/test/result/<int:pk_matter>',views.get_all_result_test_class_by_matter),
    
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
