# Create your models here.
# Models are databases
# Each data type in the project needs a model
# Configure models by creating subclass of AppConfig class in apps.py
# Activate models by adding module dotted path for MysiteConfig to INSTALLED_APPS in settings.py
# Use python manage.py makemigrations to store changes to the model as a migration
# Use python manage.py migrate to create those models tables in the database
# makemigrations and migrate used to easily add changes to your model
# without having to delete and create the database or tables
# Now create django admin user
# Add rows to model through django admin page


from django.db import models

# making a class "Page" which inherits from Model class in models module
# make Pages class which holds all page versions
# in model have parameters for each page item (fields) e.g. title, text, images

class Section(models.Model):
    # change small text data to StringField()
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    content = models.TextField()
    scroll_button = models.CharField(max_length=100)
    # section_background =
    # page_image =
    # background =

    def __str__(self):
        return str("name:" + self.title + " id:" + str(self.id))

class Page(models.Model):
    # any field that uses an FK, expects integer as default value
    # FK integer references field value (PK) of referenced model (Section)
    # After error in setting default field value, manually changed in migrations file
    name = models.CharField(max_length=100)
    section_header = models.ForeignKey(Section, on_delete = models.CASCADE, default=1, related_name = "header")
    section_about_me = models.ForeignKey(Section, on_delete = models.CASCADE, default=2, related_name = "about_me")
    section_portfolio = models.ForeignKey(Section, on_delete=models.CASCADE, default=3, related_name="portfolio")
    section_chemistry_projects = models.ForeignKey(Section, on_delete=models.CASCADE, default=4, related_name="chemistry_projects")
    section_cheerleading = models.ForeignKey(Section, on_delete=models.CASCADE, default=5, related_name="cheerleading")

    # external_links

# str() wrapped around self.id to fix exception "__str__ return non-string"
    def __str__(self):
        return str(self.name + " ID:" + str(self.id))



