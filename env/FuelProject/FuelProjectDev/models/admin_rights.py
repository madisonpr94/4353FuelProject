from django.db import models


class AdminRights(models.Model):
    class Meta:
        managed = False

        permissions = {
            ('admin_rights', 'Administrator Rights')
        }
