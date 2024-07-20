from django.contrib import admin
from core.models import  Service, Contact, Quote, Hiring, About, Service, Company, CompanyItem, Solution, TeamMember
from django.utils.html import format_html



class CompanyItemInline(admin.TabularInline):
    model = CompanyItem
    raw_id_fields = ["company"]
        
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",
#         "name",
#         "order", 
#     ]
#     prepopulated_fields = {"slug": ("name",)}
#     inlines = [CompanyItemInline]
#     list_per_page = 30

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name')
    list_per_page = 40
    # def get_queryset(self, request):
    #     return super().get_queryset(request)
    



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    exclude= ('name_fr','about_high_fr', 'about_low_fr', 'title_fr')
    list_display_links = ('id','name')
    list_per_page = 40
    def has_add_permission(self, request):
        count = self.get_queryset(request).count() > 1
        print('THE SELF Count', count)
        return not count

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_title', 'is_active')
    list_display_links = ('id','name')
    list_editable = ('job_title', 'is_active',)
    list_per_page = 40
    
# class SolutionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'slug')
#     prepopulated_fields = {"slug": ("name",), "name_en": ("name",)}
#     list_display_links = ('id','name')
#     list_per_page = 40
    
# admin.site.register(Solution, SolutionAdmin)

admin.site.register(Contact) 
admin.site.register(Quote) 
admin.site.register(Hiring) 