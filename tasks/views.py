from django.shortcuts import render,redirect
from firebase_admin import db
from DeloyRender.firebase import *

def add_task(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    due_date = request.POST.get('due_date')
    importance = request.POST.get('importance')
    
    ref = db.reference('tasks')
    new_task = {
      'title': title,
      'due_date': due_date,
      'importance': importance,
      'completed': False
    }
    ref.push(new_task)
    return redirect('add_task')

  return render(request, 'tasks/add_task.html')
