from .logic.logic_measurements import get_all_measurements , get_measurement_by_id, delete_measurement_by_id, update_measurement_value_by_id
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse (measurements_list, content_type='application/json')

def get_measurement(request, id_measure= 1):
    measurement = get_measurement_by_id(id_measure)
    measurements = [measurement]
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse (measurements_list, content_type = 'application/json')

def update_measurement_value(request, id_measure=1,new_measure=0):
    measurement = update_measurement_value_by_id(id_measure, new_measure)
    measurements = [measurement]
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')


def delete_measurement(request, id_measure=1):
    delete_measurement_by_id(id_measure)
    return HttpResponse("Eliminado measurement con id " + str(id_measure))
