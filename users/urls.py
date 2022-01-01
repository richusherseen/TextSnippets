from django.urls import path

from users.views import UserAPIView,CreateSnippets,SnippetsDetails,TagView,TagDetailsView

urlpatterns = [
    # Your other URL entries.
    path('api/user/', UserAPIView.as_view(), name='user'),
    path('api/create-snippet/', CreateSnippets.as_view(), name='create-snippet'),
    path('api/list-snippet/', CreateSnippets.as_view(), name='list-snippet'),
    path('api/snippet-details/<int:id>', SnippetsDetails.as_view(), name='snippet-details'),
    path('api/edit-snippet/<int:id>', SnippetsDetails.as_view(), name='edit-snippet'),
    path('api/delete-snippet/<int:id>', SnippetsDetails.as_view(), name='delete-snippet'),
    path('api/list-tags/', TagView.as_view(), name='list-tags'),
    path('api/tag-details/<int:id>', TagDetailsView.as_view(), name='tag-details'),


    
]
