from django.contrib import admin
from core.models import livros,genero

class LivroAdmin(admin.ModelAdmin):
    filter_horizontal = ('genero',)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'genero':
            kwargs["initial"] = [] 
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(genero)
admin.site.register(livros,LivroAdmin)
