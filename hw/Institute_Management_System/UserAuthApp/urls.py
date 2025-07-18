from django.urls import path
from UserAuthApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',registerPage, name='registerPage'),
    path('loginPage/',loginPage, name='loginPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    path('changePasswordPage/',changePasswordPage, name='changePasswordPage'),
    path('profileInfoPage/',profileInfoPage, name='profileInfoPage'),
    path('forgot_password/',forgot_password, name='forgot_password'),

    path('homePage/',homePage, name='homePage'),

    path('teacher/register/', registerTeacherPage, name='registerTeacherPage'),
    path('teacher/teacherList/', teacherListPage, name='teacherListPage'),

    path('student/registerStudentPage/', registerStudentPage, name='registerStudentPage'),
    path('student/studentListPage/', studentListPage, name='studentListPage'),
    path('student/pendingStudentReg/', pendingStudentReg, name='pendingStudentReg'),
    path('student/pendingPage/', pendingPage, name='pendingPage'),
    path('student/acceptPendingStudent/<str:id>', acceptPendingStudent, name='acceptPendingStudent'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)