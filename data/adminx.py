import xadmin

# Register your models here.


from .models import *
from xadmin import views


class ProjectAdmin(object):
    pass


class GlobalSetting(object):
    site_title = "Soccer backend"

    site_footer = "Soccer backend"


xadmin.site.register(views.CommAdminView, GlobalSetting)



class PlayerAdmin(object):
    search_fields = ['first_name','last_name']
    list_display = ['first_name', 'last_name']



xadmin.site.register(Player, PlayerAdmin)


class RecordAdmin(object):

    list_display = ['Player','Year','Player_num','Potential_Strats','bio_link']


xadmin.site.register(Record, RecordAdmin)


class AccoladeAdmin(object):

    list_display = ['Player','College','Accolade']


xadmin.site.register(Accolade, AccoladeAdmin)


class HSAdmin(object):
    search_fields = ['Name']
    list_display = ['Name','location_lat','location_long']


xadmin.site.register(High_school, HSAdmin)


class CollegeAdmin(object):
    search_fields = ['Name']
    list_display = ['Name']
    list_filter = ['College_League']


xadmin.site.register(College, CollegeAdmin)