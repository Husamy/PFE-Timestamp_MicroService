from django.urls import path
from .views import createtimestamp, getrequest, createtimestampDoc, createtimestampOrg 


urlpatterns = [
    path('create/', createtimestamp.as_view()),
    path('createDoc/', createtimestampDoc.as_view()),
    path('createorg/',createtimestampOrg.as_view()),
    path('getrequests/', getrequest.as_view())

]


