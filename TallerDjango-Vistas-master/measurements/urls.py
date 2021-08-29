from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('get_by_id/<int:id_measure>',views.get_measurement,name='medida_por_id'),
    path('delete_by_id/<int:id_measure>',views.delete_measurement,name='eliminar_medida_por_id'),
    path('update_by_id/<int:id_measure>/<int:new_measure>', views.update_measurement_value, name='actualizar_medida_por_id'),
]