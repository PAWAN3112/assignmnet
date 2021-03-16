# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import permissions, views, response, status, generics, parsers
from apps.notes import serializers
from apps.notes.services import AddCommentService

from apps.notes.models import Comment

from apps.notes.enum import CommentHeirarchy

comment_service = AddCommentService()


class AddCommentApi(views.APIView):
    # permission_classes = (
    #     permissions.AllowAny,
    # )
    model = Comment
    serializer_class = serializers.AddCommentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=request)
        if serializer.is_valid():
            data = serializer.validated_data
            data['parent_comment_id'] = data.get('parent_id', None)
            print(data)
            if not data['parent_comment_id']:
                print("-----------------")
                comment_obj = comment_service.add_comment(**data)
                comment_obj.save()
            else:
                print("+++++++++++++++++")
                comment_obj = Comment.objects.filter(id=data['parent_comment_id']).first()
                if not comment_obj:
                    return response.Response("No Parent Comment Found", status=status.HTTP_400_BAD_REQUEST)
                comment_obj.comment_heirarchy = CommentHeirarchy.PARENT
                comment_obj.save()
                data['comment_heirarchy'] = CommentHeirarchy.CHILD
                print("-----------", data)
                comment_child_obj = comment_service.add_comment(**data)
                comment_child_obj.save()
            return response.Response("success", status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # retry = True
        serializer = self.serializer_class(data=request.data, context=request)
        if serializer.is_valid():
            data = serializer.validated_data
            comment_obj = self.model.objects.filter(id=data['id']).first()
            if not comment_obj:
                return response.Response("Invalid Comment Id", status=status.HTTP_400_BAD_REQUEST)
            updated_comment_obj = comment_service.update_comment(comment_obj, **data)
            updated_comment_obj.save()
            return response.Response("success", status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)