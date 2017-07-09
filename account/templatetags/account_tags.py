from django import template
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth

register = template.Library()


@register.simple_tag
def total_people():
    return User.objects.count()


@register.inclusion_tag('account/social_total_count.html')
def social_people():
    facebook_count = UserSocialAuth.objects.filter(provider='facebook').count()
    github_count = UserSocialAuth.objects.filter(provider='github').count()
    google_count = UserSocialAuth.objects.filter(provider='google-oauth2').count()
    twitter_count = UserSocialAuth.objects.filter(provider='twitter').count()
    return {
        'facebook_count': facebook_count,
        'github_count': github_count,
        'google_count': google_count,
        'twitter_count': twitter_count,
    }


