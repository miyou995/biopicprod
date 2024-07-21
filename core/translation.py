from modeltranslation.translator import translator, TranslationOptions
from .models import Service , Solution






class ServiceTranslationOptions(TranslationOptions):
     fields =('name','description', 'full_description_1', 'full_description_2')

translator.register(Service,ServiceTranslationOptions)



class SolutionTranslationOptions(TranslationOptions):
     fields =('name', 'title', 'text', 'description')

translator.register(Solution,SolutionTranslationOptions)



