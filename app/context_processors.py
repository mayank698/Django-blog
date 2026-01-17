from .models import Category
from assignments.models import SocialLink


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_social_link(request):
    socialLink = SocialLink.objects.all()
    return dict(socialLink=socialLink)
