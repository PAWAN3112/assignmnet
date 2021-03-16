from django.conf.urls import url

from .import apis

urlpatterns = [
    url(
        r'^list/$',
        apis.GetCommentsApi.as_view(),
        name='get_comments'
    ),
    url(
        r'^add/$',
        apis.AddCommentApi.as_view(),
        name='add_comments'
    ),
    url(
        r'^delete/$',
        apis.DeleteCommentsApi.as_view(),
        name='delete_comments'
    ),
]
