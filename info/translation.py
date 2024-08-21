'''from modeltranslation.translator import register, TranslationOptions
from info.models import Category,Publication

@register(Category)
class CategoryTranslationOpti:
    fields = ('title',)
@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title','description')'''