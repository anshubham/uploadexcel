from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Register your models here.
from .models import CatsData, CatsNi, CheckFile#, UploadCatsData, UploadCatsNi, UploadDocument

class CatsDataResource(resources.ModelResource):

    class Meta:
        model = CatsData
        exclude = ('id',)
        import_id_fields = ['email','phone']


class CatsDataAdmin(ImportExportModelAdmin):
    resource_class = CatsDataResource


class CatsNiResource(resources.ModelResource):

    class Meta:
        model = CatsNi
        exclude = ('id',)
        import_id_fields = ['email','phone']


class CatsNiAdmin(ImportExportModelAdmin):
    resource_class = CatsNiResource


class CheckFileResource(resources.ModelResource):

	class Meta:
		model = CheckFile
		exclude = ('id')
		import_id_fields = ['email','phone']


class CheckFileAdmin(ImportExportModelAdmin):
	resource_class = CheckFileResource

# class DocumentAdmin(admin.ModelAdmin): 
# 	list_display = ('doc_name','button') 

admin.site.register(CatsData, CatsDataAdmin)
admin.site.register(CatsNi, CatsNiAdmin)
admin.site.register(CheckFile, CheckFileAdmin)
# admin.site.register(UploadCatsData, DocumentAdmin)
# admin.site.register(UploadCatsNi, DocumentAdmin)
# admin.site.register(UploadDocument, DocumentAdmin)

# class MyModelAdmin(admin.ModelAdmin):
#     def get_urls(self):
#     	import ipdb;ipdb.set_trace()
#         urls = super(MyModelAdmin, self).get_urls()
#         my_urls = patterns('',
#             url(r'^my_view/$', self.my_view, name="custom_view")
#         )
#         return my_urls + urls

#     def my_view(self, request):
#         # custom view which should return an HttpResponse
#         pass

#     # In case your template resides in a non-standard location
#     change_list_template = "/templates/admin/change_list.html"