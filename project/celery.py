import os
from celery import Celery

# Ορίζουμε το default Django settings module για το celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery("project")

# Χρήση string εδώ σημαίνει ότι ο worker δεν χρειάζεται να κάνει serialize
# το object των settings. Με το namespace='CELERY' όλες οι ρυθμίσεις του celery
# πρέπει να έχουν το πρόθεμα CELERY_ στο settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Αποθηκεύει και εντοπίζει αυτόματα tasks από όλα τα εγκατεστημένα Django apps
app.autodiscover_tasks()