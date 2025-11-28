from modeltranslation.translator import TranslationOptions, register
from .models import Car, Feedback

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Feedback)
class FeedbackTranslationOptions(TranslationOptions):
    fields = ('comment',)