from django.conf import settings
from django.core.cache import cache

from blog.models import Post


def get_posts_from_cache():
    queryset = Post.objects.filter(is_published=True)
    if settings.CACHE_ENABLED:
        key = 'posts'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data

    return queryset
