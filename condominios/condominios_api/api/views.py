import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Condominium,Resident,House,Residence

# Create your views here.
class CondominiumView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        # condominiums = list(Condominium.objects.values())
        # if len(condominiums) > 0:
        #     datos = {'message':"Succes",'condominium':condominiums}
        # else:
        #     datos = {'message':"Condominiums not found..."}
        # return JsonResponse(datos)
        print('myid ='+f' {id}')
        if(id>0):
            objt = list(Condominium.objects.filter(id_condominium = id).values())
            print('mylistobjt'+f'{objt}')
            if len(objt) > 0:
                condominium = objt[0]
                datos = {'message':"Succes",'condominium':condominium}
            else:
                datos = {'message':"Condominium not found..."}
            return JsonResponse(datos)
        if(id == 0):
            objt = list(Condominium.objects.values())
            print('mylistobjts'+f'{objt}')
            if len(objt) > 0:
                datos = {'message':"Succes",'Condominiums':objt}
            else:
                datos = {'message':"Condominiums not found..."}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Condominium.objects.create(name=jd['name'], code=jd['code'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass

class ResidentView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request):
        objt = list(Resident.objects.values())
        if len(objt) > 0:
            datos = {'message':"Succes",'resident':objt}
        else:
            datos = {'message':"Residents not found..."}
        return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Resident.objects.create(name=jd['name'], last_name=jd['last_name'],phone=jd['phone'],date_birth=jd['date_birth'],mail=jd['mail'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

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