from django.db import models

class UserProfileQueryset(models.QuerySet):
    def getLeaderboard(self):
        return self.all().order_by('-points','last_answered').exclude(user__is_staff=True).exclude(user__is_active=False)[:5]


class UserProfileManager(models.Manager):

    def get_queryset(self):
        return UserProfileQueryset(self.model,using=self._db)
    
    def getLeaderboard(self):
        return self.get_queryset().getLeaderboard()