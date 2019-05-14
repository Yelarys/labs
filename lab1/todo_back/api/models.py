from django.db import models

# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
    }    


class Task(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    due_on = models.DateTimeField()
    status = models.CharField(max_length = 200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE) 

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
    }        

    def to_json_long(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at': self.created_at,
            'due_on': self.due_on
        }