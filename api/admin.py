from django.contrib import admin

from .models import UserModel
from .models import ClientModel
from .models import FavoriteModel


admin.site.register(UserModel)
admin.site.register(ClientModel)
admin.site.register(FavoriteModel)
