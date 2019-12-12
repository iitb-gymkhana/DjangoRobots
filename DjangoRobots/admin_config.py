from django.contrib.admin import site


def config():
    site.module = 'SEO Management'
    site.site_title = 'Gymkhana Robots Configuration Management'
    site.site_header = 'Gymkhana Robots Configuration Portal'
    site.site_description = 'Django app for managing robots.txt files following the robots exclusion protocol'
