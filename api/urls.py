from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassPackViewSet, InstrumentViewSet, PriceViewSet, ClasseViewSet, LevelsViewSet, TeacherClasseViewSet, StudentViewSet, EnrollmentViewSet, ClassPackDiscountRulesViewSet, ClassPackClasseViewSet
from django.urls import path
from api import views


router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'class_packs', ClassPackViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'classes', ClasseViewSet)
router.register(r'levels', LevelsViewSet)
router.register(r'teacher_classes', TeacherClasseViewSet)
router.register(r'student', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'class_pack_discount_rules', ClassPackDiscountRulesViewSet)
router.register(r'class_pack_classes', ClassPackClasseViewSet)

urlpatterns = [
    path('',views.index,name='index'),
    path('', include(router.urls)),
    path('<str:table>/', views.table_view, name='table_view'),
    path('<str:table>/create/', views.create_entry, name='create_entry'),
    path('<str:table>/<int:id>/update/', views.update_entry, name='update_entry'),
    path('<str:table>/<int:id>/delete/', views.delete_entry, name='delete_entry'),
]
