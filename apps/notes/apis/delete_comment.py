from rest_framework import views, response, status

from apps.notes.models import Comment

from apps.notes.serializers import GetCommentSerializer


class DeleteCommentsApi(views.APIView):
    models = Comment

    def post(self, request, *args, **kwargs):
        comment_id = self.request.data.get('comment_id', None)
        parent_id = self.request.data.get('parent_id', None)
        comments = None
        if comment_id:
            comments = Comment.objects.filter(id=comment_id)
        elif parent_id:
            comments = Comment.objects.filter(id=parent_id)
        if comments:
            comments.delete()
            # or mark is active false instead of deleting
            return response.Response("Deleted Succesfully", status=status.HTTP_200_OK)
        return response.Response("No Data Found", status=status.HTTP_400_BAD_REQUEST)

