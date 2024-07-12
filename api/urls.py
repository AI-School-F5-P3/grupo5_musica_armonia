from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, ClassPackViewSet, InstrumentViewSet, PriceViewSet, ClasseViewSet, LevelsViewSet, TeacherClasseViewSet, StudentViewSet, EnrollmentViewSet, ClassPackDiscountRulesViewSet, ClassPackClasseViewSet
from .views import index, show_tables, new_enrollment, new_student, update_student, delete_student, update_enrollment, delete_enrollment

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'class_packs', ClassPackViewSet)
router.register(r'instruments', InstrumentViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'classes', ClasseViewSet)
router.register(r'levels', LevelsViewSet)
router.register(r'teacher_classes', TeacherClasseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'class_pack_discount_rules', ClassPackDiscountRulesViewSet)
router.register(r'class_pack_classes', ClassPackClasseViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('tables/', show_tables, name='show_tables'),
    path('new_enrollment/', new_enrollment, name='new_enrollment'),
    path('new_student/', new_student, name='new_student'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),
    path('update_enrollment/<int:id>/', update_enrollment, name='update_enrollment'),
    path('delete_enrollment/<int:id>/', delete_enrollment, name='delete_enrollment'),
    path('api/', include(router.urls)),
]
