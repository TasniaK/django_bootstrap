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
    title = models.TextField()
    tagline = models.TextField()
    content = models.TextField()
    scroll_button = models.TextField()
    # section_background =
    # page_image =
    # background =

    def __str__(self):
        return self.title

    def __str__(self):
        return self.tagline

    def __str__(self):
        return self.content

    def __str__(self):
        return self.scroll_button

class Page(models.Model):
    header = models.ForeignKey(Section, on_delete = models.CASCADE)
    # external_links

    def __str__(self):
        return self.header
