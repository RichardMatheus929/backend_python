from rest_framework.views import APIView, Response
from datetime import datetime

from .utils import Procedures
from pessoa.models import Pessoa
from .exceptions import NullData, PessoaNotExist
# Create your views here.


class Pessoas(APIView):

    def get(self, request):

        peoples = Procedures.get_peoples()

        response_peoples = []
        for people in peoples:
            response_peoples.append({
                'id': people[0],
                'name': people[1],
                'name_father': people[2],
                'name_mother': people[3],
                'date_born': people[4],
                'salary': people[5],
                'cpf': people[6],
                'created_at': people[7],
                'updated_at': people[8]
            })

        return Response(response_peoples, status=200)

    def post(self, request):

        new_people = {
            'name': request.data.get('name'),
            'name_father': request.data.get('name_father'),
            'name_mother': request.data.get('name_mother'),
            'date_born': request.data.get('date_born'),
            'salary': request.data.get('salary'),
            'cpf': request.data.get('cpf'),
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }

        if None in new_people.values():
            raise NullData
        # Validar se a pessoa já não existe ou o cpf
        # Validar cpf e data de nascimento
        
        new_people_id = Procedures.create_people(

            new_people['name'],
            new_people['name_father'],
            new_people['name_mother'],
            new_people['date_born'],
            new_people['salary'],
            new_people['cpf'],
            new_people['created_at'],
            new_people['updated_at']
            ),
            
        return Response({'people_created':new_people_id}, status=200)
    
class PessoaDetail(APIView):

    def get(self,request,pessoa_id):

        pessoa = Pessoa.objects.filter(pessoa_id=pessoa_id).first()

        if not pessoa:
            raise PessoaNotExist

        pessoa = Procedures.get_people(pessoa_id)

        response_pessoa = {
            'id': pessoa[0],
            'name': pessoa[1],
            'name_father': pessoa[2],
            'name_mother': pessoa[3],
            'date_born': pessoa[4],
            'salary': pessoa[5],
            'cpf': pessoa[6],
            'created_at': pessoa[7],
            'updated_at': pessoa[8]
        }

        return Response(response_pessoa,status=200)

    def put(self, request, pessoa_id):

        pessoa = Pessoa.objects.filter(pessoa_id=pessoa_id).first()

        if not pessoa:
            raise PessoaNotExist
        
        update = Procedures.updated_people(
            pessoa_id,
            request.data.get('name',pessoa.name),
            request.data.get('name_father',pessoa.name_father),
            request.data.get('name_mother',pessoa.name_mother),
            request.data.get('date_born',pessoa.date_born),
            request.data.get('salary',pessoa.salary),
            request.data.get('cpf',pessoa.cpf),
            pessoa.created_at,
            datetime.now()
        )

        return Response({'sucess': update}, status=200)  # Alterar o status

    def delete(self, request, pessoa_id):

        pessoa = Pessoa.objects.filter(pessoa_id=pessoa_id).first()

        if not pessoa:
            raise PessoaNotExist

        delete = Procedures.delete_people(pessoa_id)

        return Response({'sucess': delete}, status=200)  # alterar o status
