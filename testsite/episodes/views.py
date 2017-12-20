from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from reactions.models import ImageReaction, TweetReaction

def index(request, episode_id):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    image_reactions = ImageReaction.objects.filter(episode=episode_id, enabled=True)
    tweet_reactions = TweetReaction.objects.filter(episode=episode_id, enabled=True)

    reactions = list(image_reactions) + list(tweet_reactions)
    reactions_sorted = sorted(reactions, key=lambda x: x.created_at, reverse=True)
    context = {
        'results': reactions_sorted,
    }
    return render(request, 'episodes.html', context)
