from wtforms.validators import ValidationError


def alphanumeric_validator(form, field):
    if field.data and not field.data.isalnum():
        raise ValidationError('Поле содержит недопустимые символы')
