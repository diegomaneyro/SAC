from django.db import models
"""
modelos de webapp para la creacion de tablas en la db
"""
# modelo de tabla proyecto
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

# modelo de tabla tareas
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name