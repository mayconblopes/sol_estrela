from django.contrib import admin
from loja.models import Product

# admin.site.register(Product)


admin.site.site_title = "Admin"
admin.site.site_header = "Administração - Sol e Estrela: Moda Infantil"
admin.site.index_title = "Sol e Estrela: Moda Infantil"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('description', 'genre', 'aquisition_data', 'aquisition_price', 'sell_price', 'in_stock', 'size')
    search_fields = ('description',)
