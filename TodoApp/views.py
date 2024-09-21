from django.shortcuts import render, get_object_or_404, redirect
from .models import ListItem

def list_item_crud(request, id=None):
    # Handle task creation or editing
    if id:
        list_item = get_object_or_404(ListItem, id=id)  # Fetch ListItem to edit
    else:
        list_item = None  # No specific ListItem, create a new one

    # If the request method is POST, handle Create/Update
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = 'is_completed' in request.POST
        due_date = request.POST.get('due_date')

        if list_item:
            # Update existing task
            list_item.title = title
            list_item.description = description
            list_item.is_completed = is_completed
            list_item.due_date = due_date
            list_item.save()
        else:
            # Create a new task
            ListItem.objects.create(
                title=title,
                description=description,
                is_completed=is_completed,
                due_date=due_date
            )
        return redirect('list_item_crud')  # Redirect to the main list after saving

    # Handle task deletion if the 'delete' parameter is passed in URL
    if request.GET.get('delete') and list_item:
        list_item.delete()
        return redirect('list_item_crud')

    # Fetch all ListItems for listing (Read)
    list_items = ListItem.objects.all()

    # Render the template and pass all tasks and current task (if editing)
    return render(request, 'todos/todo.html', {'list_items': list_items, 'list_item': list_item})

def list_item_delete(request, id):
    # Handle task deletion
    list_item = get_object_or_404(ListItem, id=id)
    list_item.delete()
    return redirect('list_item_crud')
