from audioop import reverse
from django.db import models
from django.db import models
from tinymce import models as tinymce_models
from django.utils.html import format_html
from django.core.exceptions import ValidationError
# Create your models here.
from django.db.models.signals import pre_init
from django.db.models import F
from django.urls import reverse
from django.utils.translation import gettext as _
# Create your models here.

CHOICES = (
    ('S1' ,'Cycle Moyen'),
    ('S2' ,'Niveau Secondaire'),
    ('S3' ,'Niveau Terminal'),
    ('S4' ,'Formation Professionnelle '),
    ('S5' ,'Baccalauréat'),
    ('S6' ,'Niveau Universitaire'),
)


class About(models.Model):
    name                = models.CharField(verbose_name="Nom de l'entreprise", max_length=100,  blank=True, null=True)
    image_breadcrumb    = models.ImageField(upload_to='images/', verbose_name='breadcrumb image', blank=True, null=True)
    brochure            = models.FileField(upload_to='files/', verbose_name='brochure', blank=True, null=True)
    image_high          = models.ImageField(upload_to='images/', verbose_name='image_1', blank=True, null=True)
    image_low           = models.ImageField(upload_to='images/', verbose_name="image_2", blank=True, null=True)
    title               = models.CharField(verbose_name="Titre", max_length=50, blank=True) 
    about_high          = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)
    about_low           = tinymce_models.HTMLField(verbose_name='Page a propos 2', blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'
        
    
class TeamMember(models.Model):
    name        = models.CharField(verbose_name="Nom", max_length=60)
    job_title   = models.CharField(verbose_name="Fonction", max_length=80)
    image       = models.ImageField(upload_to='images/team/', verbose_name='image')
    is_active   = models.BooleanField(default=True)
    instagram   = models.URLField(verbose_name="Instagram", blank=True, null=True)
    linkedin    = models.URLField(verbose_name="Linkedin", blank=True, null=True)
    facebook    = models.URLField(verbose_name="Facebook", blank=True, null=True)
    
    def __str__(self):
        return str(self.name)

class Service(models.Model):
    name                = models.CharField(verbose_name="service title", max_length=100,)
    slug                = models.SlugField(unique=True, verbose_name='URL', max_length=110)
    ordering            = models.IntegerField(verbose_name=_('Display order'), null=True, blank=True)
    display_on_home     = models.BooleanField(verbose_name=_('Display on home page'), default=False)
    description         = models.TextField(verbose_name="service samll description ", blank=True, null=True)
    image_breadcrumb    = models.ImageField(upload_to='images/', verbose_name='breadcrumb image', blank=True, null=True)
    icon                = models.FileField(upload_to='images/', verbose_name='icon', blank=True, null=True)
    image               = models.ImageField(upload_to='images/', verbose_name='image du service', blank=True, null=True)
    image_high          = models.ImageField(upload_to='images/', verbose_name='image_detail_1', blank=True, null=True)
    image_low           = models.ImageField(upload_to='images/', verbose_name="image_detail_2", blank=True, null=True)
    full_description_1  = tinymce_models.HTMLField(verbose_name='full Text service 1', blank=True, null=True)
    full_description_2  = tinymce_models.HTMLField(verbose_name='full Text service 2', blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    def __str__(self):
        return str(self.name)
    
    class Meta:
        ordering = ['ordering', '-id']
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def get_absolute_url(self):
        return reverse("core:service_detail", kwargs={"slug": self.slug})
    

    
class Contact(models.Model):
    name            = models.CharField(max_length=150, verbose_name='Nom', null=True, blank=True)
    entreprise      = models.CharField(max_length=150, verbose_name="Nom de l'entreprise", null=True, blank=True)
    email           = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    phone           = models.CharField(verbose_name="Téléphone" , max_length=25, null=True, blank=True)
    service         = models.ForeignKey(Service, verbose_name='service', null=True, blank=True, on_delete=models.SET_NULL)
    subject         = models.CharField(max_length=150, verbose_name='sujet', null=True, blank=True)
    message         = models.TextField(null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contact")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:contact", kwargs={"pk": self.pk})
    
    


class Hiring(models.Model):
    name        = models.CharField(max_length=150, verbose_name='Nom')
    email       = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25, null=True, blank=True)
    niveau      = models.CharField(choices=CHOICES,verbose_name="niveau d'étude", max_length=2, null=True, blank=True)
    birth_date  = models.DateField(null=True, blank=True) 
    birth_place = models.CharField(max_length=150, verbose_name='lieu de naissance', null=True, blank=True)
    permis      = models.BooleanField(verbose_name='Permis de Conduire ', default=False)
    passeport   = models.BooleanField(verbose_name='Passeport valide', default=False)
    army        = models.BooleanField(verbose_name='Service militaire', default=False)
    message     = models.TextField(verbose_name='Experience', null=True, blank=True)
    cv_file     = models.FileField(upload_to='media', verbose_name='CV', null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name = _("hiring")
        verbose_name_plural = _("hirings")
    
    def __str__(self):
        return str(self.email)


    def get_absolute_url(self):
        return reverse("core:hiring", kwargs={"pk": self.pk})

    
class Quote(models.Model):
    email       = models.EmailField(verbose_name="E-mail")
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25) 
    entreprise  = models.CharField(max_length=150, verbose_name="Nom de l'entreprise", null=True, blank=True)
    service     = models.ForeignKey(Service, verbose_name='service', null=True, blank=True, on_delete=models.CASCADE)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name = _("quote")
        verbose_name_plural = _("quotes")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("business:quote", kwargs={"pk": self.pk})
    
    def get_total_cost(self):
        return self.surface.price +  self.bien.price + self.formule.price
    

class Solution(models.Model):
    name        = models.CharField(_("Nom de la solution"), max_length=50)
    slug        = models.SlugField(max_length=150, unique=True, verbose_name=_("URL"))
    title       = models.CharField(_("Grand titre de la solution"), max_length=70, blank=True, null=True)
    icon        = models.ImageField(upload_to='images/solutions', verbose_name=_("Petite image"), blank=True, null=True)
    banner      = models.ImageField(upload_to='images/solutions', verbose_name=_("Grande image"), blank=True, null=True)
    text        = models.TextField(verbose_name="petit texte", blank=True, null=True)
    is_active   = models.BooleanField(_("Activer la solution"), default=True)
    description = tinymce_models.HTMLField(verbose_name='Description du service', blank=True, null=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("core:solution_detail", kwargs={"slug": self.slug})
    
    


class ProtfolioCategory(models.Model):
    name = models.CharField(_("Nom de la categorie"), max_length=50)
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_("URL"))
    description = models.TextField(_("Description de la categorie"), blank=True, null=True)
    is_active = models.BooleanField(_("Activer la categorie"), default=True)
    
    class Meta:
        verbose_name = _("Categorie de portfolio")
        verbose_name_plural = _("Portfolio")
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("core:portfolio_category", kwargs={"slug": self.slug})
    
class PortfolioItem(models.Model):
    category        = models.ForeignKey(ProtfolioCategory, verbose_name='categorie', related_name="portfolio_items", null=True, blank=True, on_delete=models.SET_NULL)
    name            = models.CharField(_("Nom de l'item"), max_length=50)
    video_url       = models.URLField(_("URL de la video"), blank=True, null=True)
    image           = models.ImageField(upload_to='images/portfolio', verbose_name=_("Image de l'item"), blank=True, null=True)
    description     = models.TextField(_("Description de l'item"), blank=True, null=True)
    is_active       = models.BooleanField(_("Activer l'item"), default=True)
    display_on_home = models.BooleanField(verbose_name=_('Display on home page'), default=False)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("core:portfolio_item", kwargs={"pk": self.pk})
    
    @property
    def is_video(self):
        return self.video_url != None
    
    
    
class Client(models.Model):
    name = models.CharField(_("Nom du client"), max_length=50)
    logo = models.ImageField(upload_to='images/clients', verbose_name=_("Logo du client"))
    ordering = models.IntegerField(verbose_name=_('Display order'), null=True, blank=True)
    is_active = models.BooleanField(_("Activer le client"), default=True)
    
    def __str__(self):  
        return self.name
    
    class Meta:
        ordering = ['ordering', '-id']
        
class Proof(models.Model):
    number = models.CharField(_("Chiffre"), max_length=50)
    text = models.TextField(_("Achievment detail"))
    ordering = models.IntegerField(verbose_name=_('Display order'), null=True, blank=True)
    is_active = models.BooleanField(_("Activer le client"), default=True)
    
    class Meta:
        ordering = ['ordering', '-id']
    def __str__(self):  
        return self.number