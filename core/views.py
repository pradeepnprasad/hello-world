from django.shortcuts import render
from django.conf import settings

import requests

from .forms import SubmitEmbed
from .serializer import EmbedSerializer


def save_embed(request):

    if request.method == "POST":
        form = SubmitEmbed(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            # r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
            r = requests.get('http://api.embed.ly/1/oembed?key=0ee90ce5e755485787fde8db8f285ea9&url=https://www.youtube.com/watch?v=VyRK6e8IzU0&index=27&list=RDMMrj65ohO9DL0')
            try:
                jsonoutput = r.json()
                serializer = EmbedSerializer(data=jsonoutput)
                if serializer.is_valid():
                    embed = serializer.save()
                    return render(request, 'embeds.html', {'embed': embed})
                    print(embed)
            except ValueError:
                print("N'est pas JSON")
    else:
        form = SubmitEmbed()

    return render(request, 'index.html', {'form': form})

# Create your views here.
