from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from core.models import City


@register(City)
class CityTranslation(TranslationOptions):
    fields = ('name', 'state', 'state_name', 'country', 'country_name')
