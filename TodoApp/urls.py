from django.urls import path
from .views import list_item_crud, list_item_delete

urlpatterns = [
    path('todo/', list_item_crud, name='list_item_crud'),  # This handles task listing and creation (no ID)
    path('todo/<int:id>/', list_item_crud, name='list_item_crud'),  # This handles editing tasks (with ID)
    path('todo/delete/<int:id>/', list_item_delete, name='list_item_delete'),  # This handles task deletion
]
