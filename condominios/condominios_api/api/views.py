from django.http import JsonResponse
from django.views import View
from .models import Condominium,Resident,House,Residence

# Create your views here.
class CondominiumView(View):
    def get(self, request):
        condominiums = list(Condominium.objects.values())
        if len(condominiums) > 0:
            datos = {'message':"Succes",'condominium':condominiums}
        else:
            datos = {'message':"Condominiums not found..."}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class ResidentView(View):
    def get(self, request):
        objt = list(Resident.objects.values())
        if len(objt) > 0:
            datos = {'message':"Succes",'resident':objt}
        else:
            datos = {'message':"Residents not found..."}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class HouseView(View):
    def get(self, request):
        objt = list(House.objects.values())
        if len(objt) > 0:
            datos = {'message':"Succes",'house':objt}
        else:
            datos = {'message':"Houses not found..."}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

class ResidenceView(View):

    def get(self, request):
        objt = list(Residence.objects.values())
        if len(objt) > 0:
            datos = {'message':"Succes",'residence':objt}
        else:
            datos = {'message':"Residences not found..."}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass