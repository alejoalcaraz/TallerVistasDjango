from ..models import Measurement

def get_measurement_by_id(id:int):
    measurement = Measurement.objects.get(pk = id)
    return measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def update_measurement_value_by_id(id:int, new_measure:int):
    measurement = get_measurement_by_id(id)
    measurement.value = new_measure
    measurement.save()
    return measurement

def delete_measurement_by_id(id:int):
    measurement = get_measurement_by_id(id)
    measurement.delete()

