from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

class Floor(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    created_by = CurrentUserField(related_name='%(class)s_created_by', null=True, blank=True, editable=False)
    updated_by = CurrentUserField(on_update=True, related_name='%(class)s_updated_by', null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.BooleanField(default=True)
    description = models.CharField(max_length=5000, blank=False, null=False, verbose_name='Descripción', unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Pisos'
        db_table = 'tb_security_floor'
        verbose_name = 'Piso'

