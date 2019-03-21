from django.http import HttpResponseRedirect


def redirect_with_GET(url, *args, **kwargs):
    from django.shortcuts import reverse
    import urllib.parse

    url = reverse(url, args=args)
    params = urllib.parse.urlencode(kwargs['kwargs'])
    return HttpResponseRedirect(url + "?%s" % params)
