from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название шаблона')
    fields = models.ManyToManyField(Field)
    def __str__(self):
        return self.form_name
class Field(models.Model):
    CHOICE_TYPE = (
        (text, 'text'),
        (email, 'example@email.mail'),
        (phone, '+7123456789'),
        (date, '2023-01-01')
    )

    f_name = models.CharField(max_length=50)
    f_type = models.CharField(max_length=5,
                                   choices=CHOICE_TYPE,
                                   default=text)
    def __str__(self):
        return self.f_тфьу
