# core/admin_site.py
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "Панель управления"
    site_title = "Админка проекта"
    index_title = "Добро пожаловать"

admin_site = MyAdminSite(name="myadmin")
