from django.db import migrations

class Migration(migrations.Migration):

    CREATE_IDX_NAME = "CREATE INDEX idx_name ON pessoa_pessoa (name);"
    CRATE_IDX_DATE_BORN = "CREATE INDEX idx_date_born ON pessoa_pessoa (date_born);"

    dependencies = [
        ('pessoa', '0007_procedures_createds'),
    ]

    operations = [
        migrations.RunSQL(CREATE_IDX_NAME),
        migrations.RunSQL(CRATE_IDX_DATE_BORN),
    ]
