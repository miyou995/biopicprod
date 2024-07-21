from django.contrib import admin
from core.models import  Service, Contact, Quote, Hiring, About, Service, ProtfolioCategory, PortfolioItem, TeamMember, Client, Proof
from django.utils.html import format_html




class PortfolioItemInline(admin.TabularInline):
    model = PortfolioItem
    raw_id_fields = ["category"]
   
@admin.register(ProtfolioCategory)
class ProtfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name')
    list_editable = ('is_active',)
    list_per_page = 40
    inlines = [PortfolioItemInline]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_display_links = ('id','name')
    list_editable = ('is_active',)
    list_per_page = 40

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_on_home')
    # prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name')
    list_editable = ('display_on_home',)
    list_per_page = 40
    # def get_queryset(self, request):
    #     return super().get_queryset(request)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_on_home')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name')
    list_editable = ('display_on_home',)
    list_per_page = 40
    # def get_queryset(self, request):
    #     return super().get_queryset(request)
    

@admin.register(Proof)
class ProofAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'text', 'is_active', 'ordering')
    list_display_links = ('id','number')
    list_editable = ('ordering','is_active')
    list_per_page = 40


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    exclude= ('name_fr','about_high_fr', 'about_low_fr', 'title_fr')
    list_display_links = ('id','name')
    list_per_page = 40
    
    def has_add_permission(self, request):
        count = self.get_queryset(request).count() > 0
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