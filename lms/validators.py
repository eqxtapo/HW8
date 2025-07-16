from rest_framework.serializers import ValidationError



class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = dict(value).get(self.field)

        if bool(dict(value).get('link')) and not bool('youtube.com' in link):
            raise ValidationError('Недопустимая ссылка')
