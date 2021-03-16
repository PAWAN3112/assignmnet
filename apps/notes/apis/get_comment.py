from rest_framework import views, response, status

from apps.notes.models import Comment

from apps.notes.serializers import GetCommentSerializer

from apps.notes import serializers

from apps.notes.apis.add_comment import comment_service


class GetCommentsApi(views.APIView):
    models = Comment

    def get(self, request, *args, **kwargs):
        # request_id = self.request.query_params.get('request_id')
        comments = Comment.objects.all().order_by('id')
        if comments:
            serializer = GetCommentSerializer(comments, many=True).data
            return response.Response(serializer, status=status.HTTP_200_OK)
        return response.Response("No Data Found", status=status.HTTP_400_BAD_REQUEST)


