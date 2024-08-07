from django.db import connection


class Procedures():

    def get_people(id) -> list:
        with connection.cursor() as cursor:
            cursor.callproc('get_pessoas')
            result = cursor.fetchall()
            return result

    def create_people(name, name_father, name_mother, date_born, salary, cpf) -> int | None:
        with connection.cursor() as cursor:
            cursor.callproc('insert_pessoa', [name, name_father, name_mother, date_born, salary, cpf])
            result = cursor.fetchone()
            return result[0] if result else None

    def updated_people(id, name, name_father, name_mother, date_born, salary, cpf) -> bool | None:
        with connection.cursor() as cursor:
            cursor.callproc('update_pessoa', [id, name, name_father, name_mother, date_born, salary, cpf])
            result = cursor.fetchone()
            return result[0]
        
    def delete_people(id) -> bool | None:
        with connection.cursor() as cursor:
            cursor.callproc('delete_pessoa', [id])
            result = cursor.fetchone()
            return result[0]
