from rest_framework.views import APIView, Response

from .utils import Procedures
# Create your views here.

class Pessoa(APIView):

    def get(self, request):
        
        pessoas = Procedures.get_people(6)
        return Response(pessoas)
    
    def post(self, request):

        new_people_id = Procedures.create_people('João', 'José', 'Maria', '1990-01-01', 1000.00, '223.456.789-00')
        return Response(new_people_id, status=200)

    def put(self, request):

        # Criar a lógica para atualizar um determinado campo apenas
        update = Procedures.updated_people(4, 'João agora trocado', 'José', 'Maria', '1990-01-01', 1000.00, '223.456.789-00')
        return Response({'sucess': update}, status=200)#Alterar o status
    
    def delete(self, request):

        delete = Procedures.delete_people(4)
        return Response({'sucess': delete}, status=200)#alterar o status
