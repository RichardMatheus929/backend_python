from rest_framework.exceptions import APIException

class NullData(APIException):
    status_code = 400
    default_detail = 'A requisição post não pode conter dados vazios'
    default_code = 'data not could be null'

class PessoaNotExist(APIException):
    status_code = 400
    default_detail = 'A pessoa não pode ser editada porque não existe'
    default_code = 'people not exists'

class InvalidData(APIException):
    status_code = 400
    default_detail = "Os dados inseridos são inválidos"
    default_code = 'invalid data'