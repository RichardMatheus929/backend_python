from rest_framework.views import APIView, Response, status
import datetime

from pessoa.models import Pessoa

from .utils.procedures import Procedures
from .utils.exceptions import NullData, PessoaNotExist, InvalidData
from .utils.validation import Validation

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

        return Response(response_peoples, status.HTTP_200_OK)

    def post(self, request):

        new_people = {
            'name': request.data.get('name'),
            'name_father': request.data.get('name_father'),
            'name_mother': request.data.get('name_mother'),
            'date_born': request.data.get('date_born'),
            'salary': request.data.get('salary'),
            'cpf': request.data.get('cpf'),
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now()
        }

        # Validações

        if None in new_people.values():
            raise NullData
        
        if Pessoa.objects.filter(cpf=new_people['cpf']).exists():
            raise InvalidData
        
        if new_people['date_born']:
            try:
                new_people['date_born'] = datetime.datetime.strptime(new_people['date_born'],"%d/%m/%Y")
            except ValueError:
                raise InvalidData
            
        if not Validation.validador_cpf(new_people['cpf']):
            raise InvalidData
        
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
            
        return Response({'people_created':new_people_id}, status=status.HTTP_201_CREATED)
    
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

        return Response(response_pessoa,status=status.HTTP_200_OK)

    def put(self, request, pessoa_id):

        pessoa = Pessoa.objects.filter(pessoa_id=pessoa_id).first()

        # Validações
        if not pessoa:
            raise PessoaNotExist
        
        if request.data.get('date_born',pessoa.date_born):
            try:
                date_born = request.data.get('date_born',pessoa.date_born)
                date_born = datetime.datetime.strptime(request.data.get('date_born',pessoa.date_born),"%d/%m/%Y")
            except ValueError:
                raise InvalidData
        
        update = Procedures.updated_people(
            pessoa_id,
            request.data.get('name',pessoa.name),
            request.data.get('name_father',pessoa.name_father),
            request.data.get('name_mother',pessoa.name_mother),
            date_born,
            request.data.get('salary',pessoa.salary),
            request.data.get('cpf',pessoa.cpf),
            pessoa.created_at,
            datetime.datetime.now()
        )

        return Response({'sucess': update}, status=status.HTTP_200_OK)

    def delete(self, request, pessoa_id):

        pessoa = Pessoa.objects.filter(pessoa_id=pessoa_id).first()

        if not pessoa:
            raise PessoaNotExist

        delete = Procedures.delete_people(pessoa_id)

        return Response({'sucess': delete}, status=status.HTTP_204_NO_CONTENT)
