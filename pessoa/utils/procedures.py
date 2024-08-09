from django.db import connection

from datetime import datetime


class Procedures():

    def get_people(pessoa_id) -> tuple:
        
        with connection.cursor() as cursor:
            cursor.callproc('get_pessoa',[pessoa_id])
            result = cursor.fetchone()
            return result

    def get_peoples() -> list[tuple]:

        with connection.cursor() as cursor:
            cursor.callproc('get_pessoas')
            result = cursor.fetchall()
            return result

    def create_people(name, name_father, name_mother, date_born, salary, cpf,created_at,updated_at) -> int | None:

        with connection.cursor() as cursor:
            cursor.callproc('insert_pessoa', [name, name_father, name_mother, date_born, salary, cpf,created_at,updated_at])
            result = cursor.fetchone()
            return result[0] if result else None

    def updated_people(id, name, name_father, name_mother, date_born, salary, cpf,created_at,updated_at) -> bool:

        with connection.cursor() as cursor:
            cursor.callproc('update_pessoa', [id, name, name_father, name_mother, date_born, salary, cpf,created_at,updated_at])
            result = cursor.fetchone()
            return result[0]
        
    def delete_people(id) -> bool:
        with connection.cursor() as cursor:
            cursor.callproc('delete_pessoa', [id])
            result = cursor.fetchone()
            return result[0]
