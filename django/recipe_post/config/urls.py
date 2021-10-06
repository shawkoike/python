from django.contrib import admin
from django.urls import path, include
from recipe.views import RecipeListView, RecipeCreateView, RecipeDetailView, RecipeUpdateView, RecipeDeleteView
from lib.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', include("recipe.urls")),
    path('', IndexTemplateView.as_view(), name="index"),
]
