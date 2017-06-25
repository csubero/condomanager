from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from manager.views import BuildingListView, BuildingAddView, BuildingEditView

urlpatterns = [
	# url(r'^$', IndexView.as_view(), name='backend.index'),
	# Building URL'S
	url(r'^buildings/$', BuildingListView.as_view(), name='manager.building.list'),
	url(r'^buildings/add/$', BuildingAddView.as_view(), name='manager.building.add'),
	url(r'^buildings/(?P<pk>[0-9]+)/edit/$', BuildingEditView.as_view(), name='manager.building.edit'),
]

# if settings.DEBUG:
# 	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
