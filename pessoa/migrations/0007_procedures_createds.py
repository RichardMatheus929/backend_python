from django.db import migrations

SQL_GET_PESSOAS = """
CREATE OR REPLACE FUNCTION public.get_pessoas()
 RETURNS TABLE(pessoa_id integer, name character varying, name_father character varying, name_mother character varying, date_born date, salary numeric, cpf character varying, created_at timestamp with time zone, updated_at timestamp with time zone)
 LANGUAGE plpgsql
AS $function$
BEGIN
    RETURN QUERY
    SELECT p.pessoa_id,
           p.name,
           p.name_father,
           p.name_mother,
           p.date_born,
           p.salary,
           p.cpf,
           p.created_at,
           p.updated_at
    FROM pessoa_pessoa p;
END;
$function$
;
"""

SQL_GET_PESSOA = """
CREATE OR REPLACE FUNCTION public.get_pessoa(p_pessoa_id integer)
 RETURNS TABLE(pessoa_id integer, name character varying, name_father character varying, name_mother character varying, date_born date, salary numeric, cpf character varying, created_at timestamp with time zone, updated_at timestamp with time zone)
 LANGUAGE plpgsql
AS $function$
BEGIN
    RETURN QUERY
    SELECT p.pessoa_id,
           p.name,
           p.name_father,
           p.name_mother,
           p.date_born,
           p.salary,
           p.cpf,
			p.created_at,
			p.updated_at

    FROM pessoa_pessoa p
    WHERE p.pessoa_id = p_pessoa_id;
END;
$function$
;
"""

SQL_DELETE_PESSOA = """
CREATE OR REPLACE FUNCTION public.delete_pessoa(p_pessoa_id integer)
 RETURNS boolean
 LANGUAGE plpgsql
AS $function$
BEGIN
    DELETE FROM pessoa_pessoa
    WHERE pessoa_id = p_pessoa_id;

    IF FOUND THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$function$
;
"""
SQL_POST_PESSOA = """
CREATE OR REPLACE FUNCTION public.update_pessoa(p_pessoa_id integer, p_name text, p_name_father text, p_name_mother text, p_date_born date, p_salary numeric, p_cpf character, p_created_at timestamp with time zone, p_updated_at timestamp with time zone)
 RETURNS boolean
 LANGUAGE plpgsql
AS $function$
BEGIN
    UPDATE pessoa_pessoa
    SET name = p_name,
        name_father = p_name_father,
        name_mother = p_name_mother,
        date_born = p_date_born,
        salary = p_salary,
        cpf = p_cpf,
        created_at = p_created_at,
        updated_at = p_updated_at
    WHERE pessoa_id = p_pessoa_id;

    -- Verifica se a atualização afetou alguma linha
    IF FOUND THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END;
$function$
;
"""

SQL_CREATE_PESSOA = """
CREATE OR REPLACE FUNCTION public.insert_pessoa(
    p_nome TEXT,
    p_nomepai TEXT,
    p_nomemae TEXT,
    p_datanascimento TIMESTAMP,
    p_salario NUMERIC,
    p_cpf CHAR(14),
    p_created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
    p_updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now()
) RETURNS INTEGER
LANGUAGE plpgsql
AS $function$
DECLARE
    new_id INTEGER;
BEGIN
    INSERT INTO pessoa_pessoa (name, name_father, name_mother, date_born, salary, cpf, created_at, updated_at)
    VALUES (p_nome, p_nomepai, p_nomemae, p_datanascimento, p_salario, p_cpf, p_created_at, p_updated_at)
    RETURNING pessoa_id INTO new_id;

    RETURN new_id;
END;
$function$;

"""


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0006_pessoa_created_at_pessoa_updated_at'),
    ]

    operations = [
        migrations.RunSQL(SQL_GET_PESSOA),
        migrations.RunSQL(SQL_GET_PESSOAS),
        migrations.RunSQL(SQL_DELETE_PESSOA),
        migrations.RunSQL(SQL_POST_PESSOA),
        migrations.RunSQL(SQL_CREATE_PESSOA),
    ]
