from django.urls import path

from backend.apps.views.welcome.has_completed_welcome_view import \
    HasCompletedWelcomeView
from backend.apps.views.welcome.welcome_survey_view import WelcomeSurveyView

urlpatterns = [
    path('has-completed', HasCompletedWelcomeView.as_view(), name="has_completed"),
    path('survey', WelcomeSurveyView.as_view(), name="survey")
]