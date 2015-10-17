__author__ = 'ishant'

from django.conf.urls import url


from . import views

urlpatterns = [
    # ex: /polls/

    # ex: /polls/5/
    url(r"^$",views.index,name="index"),
    url(r"^formTest/$",views.formTest,name="formTest"),
    url(r"^viewTool/$",views.viewTool,name="view_tool"),
    url(r"^runTool/$",views.runTool,name="run_tool"),
    url(r"^viewLogs/$",views.viewLogs,name="view_log"),
    url(r"^toolDetail/(?P<pk>[0-9]+)$",views.toolDetail,name="tool_detail"),
    url(r"^runToolDetail/(?P<pk>[0-9]+)$",views.runToolDetail,name="run_tool_detail"),
    url(r"^logDetail/(?P<pk>[0-9]+)$",views.logDetail,name="log_detail"),
]


