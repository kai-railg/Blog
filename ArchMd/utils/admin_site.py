__data__ = '2019-04-20 14:47'
__author__ = 'Kai'



from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Blog'
    site_title = 'Blog 后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')