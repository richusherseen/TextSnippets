from django.shortcuts import render
import sys
from rest_framework import response
from rest_framework.views import APIView
from users.models import Snippets, Tags
from users.serializers import UserSerializer, SnippetSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CreateSnippets(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self,request):
        try:
            host = request.META['HTTP_HOST']
            snippets = Snippets.objects.all()
            lst = []
            for snippet in snippets:
                record = {
                    "id" : snippet.id,
                    "title" : snippet.title.title,
                    "text" : snippet.text,
                    "created_at" : snippet.created_at,
                    "url" : f"{host}/snippet-details/{str(snippet.id)}"
                }
                lst.append(record)
            print(lst,len(snippets))
            return Response(data={'status': True, 'total_number_of_snippets': len(snippets), "records": lst}, 
            status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response(data={'status': False, 'msg': str(e), "line_number": str(exc_tb.tb_lineno)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        try:
            data = request.data
            print(data)
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                print('valid')
                if len(Tags.objects.filter(title=serializer.data['title'])):
                    tag = Tags.objects.get(title=serializer.data['title'])
                else:
                    tag = Tags.objects.create(title=serializer.data['title'])

                Snippets.objects.create(
                    created_user=request.user, title=tag, text=serializer.data['text'])
                return Response(data={'status': True, 'msg': f"New Snippet Created. "}, status=status.HTTP_201_CREATED)
            else:
                return Response(data={'status': False, 'msg': serializer.errors}, status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response(data={'status': False, 'msg': str(e), "line_number": str(exc_tb.tb_lineno)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SnippetsDetails(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self,request,id):
        try:
            snippet = Snippets.objects.get(id=id)
            record = {
                "id" : snippet.id,
                "title" : snippet.title.title,
                "text" : snippet.text,
                "created_at" : snippet.created_at
                }              

            return Response(data={'status': True, "records": record}, 
            status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response(data={'status': False, 'msg': str(e), "line_number": str(exc_tb.tb_lineno)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request,id):
        try:
            data = request.data
            print(data)
            serializer = SnippetSerializer(data=data)
            if serializer.is_valid():
                print('valid')
                if len(Tags.objects.filter(title=serializer.data['title'])):
                    tag = Tags.objects.get(title=serializer.data['title'])
                else:
                    tag = Tags.objects.create(title=serializer.data['title'])

                snippet = Snippets.objects.get(id=id)
                snippet.created_user = request.user
                snippet.title = tag
                snippet.text = text=serializer.data['text']
                snippet.save()
                
                record = {
                "id" : snippet.id,
                "title" : snippet.title.title,
                "text" : snippet.text,
                "created_at" : snippet.created_at
                } 
                return Response(data={'status': True, "records": record}, 
            status=status.HTTP_205_RESET_CONTENT)
            else:
                return Response(data={'status': False, 'msg': serializer.errors}, status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response(data={'status': False, 'msg': str(e), "line_number": str(exc_tb.tb_lineno)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request,id):
        try:
            sn = Snippets.objects.get(id=id)
            title = sn.title
            print(title)
            print(title.id)
            Snippets.objects.get(id=id).delete()
            if not len(Snippets.objects.filter(title=title)):
                Tags.objects.get(id=title.id).delete()

            host = request.META['HTTP_HOST']
            snippets = Snippets.objects.all()
            lst = []
            for snippet in snippets:
                record = {
                    "id" : snippet.id,
                    "title" : snippet.title.title,
                    "text" : snippet.text,
                    "created_at" : snippet.created_at,
                    "url" : f"{host}/snippet-details/{str(snippet.id)}"
                }
                lst.append(record)
                print(lst,len(snippets))
            return Response(data={'status': True, 'total_number_of_snippets': len(snippets), "records": lst}, 
            status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response(data={'status': False, 'msg': str(e), "line_number": str(exc_tb.tb_lineno)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 

class TagView(APIView):
    
    def get(self,request):
        try:
            host = request.META['HTTP_HOST']
            tags = Tags.objects.all()
            lst = []
            for tag in tags:
                record = {
                    "id" : tag.id,
                    "title" : tag.title,
                    "created_at" : tag.created_at,
                    "url" : f"{host}/tag-details/{str(tag.id)}"
                }
                lst.append(record)
            return Response(data={'status': True,  "records": lst}, 
            status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response(data={'status': False, 'msg': str(e), "line_number": str(exc_tb.tb_lineno)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TagDetailsView(APIView):
    
    def get(self,request,id):
        try:
            host = request.META['HTTP_HOST']
            snippets = Snippets.objects.filter(title__id=id)
            lst = []
            for snippet in snippets:
                record = {
                    "id" : snippet.id,
                    "title" : snippet.title.title,
                    "text" : snippet.text,
                    "created_at" : snippet.created_at,
                    "url" : f"{host}/snippet-details/{str(snippet.id)}"
                }
                lst.append(record)
                print(lst,len(snippets))
            return Response(data={'status': True, 'total_number_of_snippets': len(snippets), "records": lst}, 
            status=status.HTTP_200_OK)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return Response(data={'status': False, 'msg': str(e), "line_number": str(exc_tb.tb_lineno)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



        
