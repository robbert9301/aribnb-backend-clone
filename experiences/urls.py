from django.urls import path
from .views import PerkDetail, Perks, Experiences, ExperiencesDetail, ExperienceReview, ExperiencePerk, ExperiencePhotos, ExperienceBookings

urlpatterns = [
    path("", Experiences.as_view()),
    path("<int:pk>",ExperiencesDetail.as_view()),
    path("<int:pk>/reviews",ExperienceReview.as_view()),
    path("<int:pk>/perks",ExperiencePerk.as_view()),
    path("<int:pk>/photos", ExperiencePhotos.as_view()),
    path("<int:pk>/bookings", ExperienceBookings.as_view()),    
    path("perks/", Perks.as_view()),
    path("perks/<int:pk>", PerkDetail.as_view()),
]