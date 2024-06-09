from django import forms
from .models import Task, SubTask


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateTaskForm(forms.ModelForm):
    importance = forms.ChoiceField(choices=Task.IMPORTANCE_CHOICES ,label='Важность')

    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date')
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'due_date': 'Планируемая дата выполнения',
            'importance': 'Важность',
        }
        help_texts = {
            'title': 'Пробежать 2 км'
        }


class UpdateTaskForm(forms.ModelForm):
    creation_d = forms.DateField(label='Дата создания', required=False)
    class Meta:
        model = Task
        fields = ('title', 'description', 'creation_d', 'due_date', 'importance', 'days_left')
        labels = {
            'title': 'Название задачи',
            'description': 'Описание',
            'due_date': 'Планируемая дата выполнения',
            'days_left': 'Осталось дней',
            'importance': 'Важность',
        }


