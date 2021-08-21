from django.urls import path
from .views import (home_view,
                    # about_view,
                    # intrests_view,
                    # projects_view,
                    # project_view,
                    # contact_view,
                    )

app_name = 'ProjectReal'

urlpatterns = [
    path('', home_view, name='home-page'),
]
