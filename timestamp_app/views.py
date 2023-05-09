
import datetime 
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Timestampserializer, TimestampDocserializer , TimestampOrgserializer
from .models import user_timestamp, document_timestamp , organisation_timestamp
from rest_framework import status, permissions
import os, json, requests
from django.db.models import Q








class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        id = request.user.id
        if id is None:
            return False
        else:
            host_ip = os.environ.get('HOST_IP')
            auth_url = 'http://' + str(host_ip) + ':8002/api/users/'+ str(id)
            response = requests.get(auth_url)
            response_json = json.loads(response.content.decode('utf-8'))
            user_id = response_json['id']
            return id == user_id




class CustomQuerysetMixin:
    def get_queryset(self):
        """
        Override the get_queryset() function to filter data based on user_id and organisation.owner.
        """
        # get organisation
        queryset = super().get_queryset()
        host_ip = os.environ.get('HOST_IP')
        id = self.request.user.id
        auth_url = 'http://' + str(host_ip) + ':8002/api/users/'+ str(id)
        response = requests.get(auth_url)
        response_json = json.loads(response.content.decode('utf-8'))
        isAdmin = response_json['isAdmin']
        if isAdmin:
            return queryset
        user_organisation = response_json['organisation']
        if user_organisation is None:
            queryset = queryset.filter(owner=self.request.user.email)
            return queryset
        else:
            org_url = 'http://' + str(host_ip) + ':8002/api/organisation/create/'
            response = requests.get(org_url)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++=")
            print(response)
            response_json1 = json.loads(response.content.decode('utf-8'))
            org_data = response_json1[0]
            owner=org_data['owner']
            if owner == self.request.user.email:
                members=org_data['members']
                return queryset.filter(Q(user_id__in=members) | Q(user_id=id))
            else: 
                return queryset.filter(owner=self.request.user.email)






class createtimestamp(generics.ListCreateAPIView):
    queryset = user_timestamp.objects.all()
    serializer_class = Timestampserializer
    permission_classes=[IsUser,]
    def get_queryset(self):
        """
        Override the get_queryset() function to filter data based on user_id and organisation.owner.
        """
        # get organisation
        queryset = super().get_queryset()
        host_ip = os.environ.get('HOST_IP')
        id = self.request.user.id
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")
        print(self.request)
        print('id: ' + str(id))
        auth_url = 'http://' + str(host_ip) + ':8002/api/users/'+ str(id)
        response = requests.get(auth_url)
        response_json = json.loads(response.content.decode('utf-8'))
        print('response auth: ' + str(response_json))
        isAdmin = response_json['isAdmin']
        if isAdmin:
            return queryset
        else:
            return queryset.filter(owner=self.request.user.email)

    
    
    def post(self, request, *args, **kwargs):
        # Extract the user ID and email address from the request data
        action = request.data.get('action')
        serializer = self.get_serializer(data=request.data)
        print("))))))))))))(((((((((((((())))))))))))))"+ str(serializer))
        serializer.is_valid(raise_exception=True)
        request_join = serializer.save(action=action)
        # Return a JSON response indicating success
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class createtimestampDoc(CustomQuerysetMixin, generics.ListCreateAPIView):
    queryset = document_timestamp.objects.all()
    serializer_class = TimestampDocserializer
    permission_classes=[IsUser,]
    
    
    
    
    def post(self, request, *args, **kwargs):
        # Extract the user ID and email address from the request data
        action = request.data.get('action')
        serializer = self.get_serializer(data=request.data)
        print("))))))))))))(((((((((((((())))))))))))))"+ str(serializer))
        serializer.is_valid(raise_exception=True)
        document_id = request.data.get('document_id')
        request_join = serializer.save(action=action, document_id=document_id)
        # Return a JSON response indicating success
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    
  

class createtimestampOrg(CustomQuerysetMixin, generics.ListCreateAPIView):
    queryset = organisation_timestamp.objects.all()
    serializer_class = TimestampOrgserializer
    permission_classes=[IsUser,]
    
    
    
    
    def post(self,request):
        action = request.data.get('action')
        organisation = request.data.get('organisation')
        serializer = self.get_serializer(data=request.data)
        print("))))))))))))(((((((((((((())))))))))))))"+ str(serializer))
        serializer.is_valid(raise_exception=True)
        request_join = serializer.save(action=action, organisation=organisation)
        # Return a JSON response indicating success
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class getrequest(generics.ListAPIView):
    queryset = document_timestamp.objects.filter(action='Request Join')
    serializer_class = TimestampDocserializer
