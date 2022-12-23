from django import template
from django.db.models import Count

from ..models import Post
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


# simple tag
@register.simple_tag
def total_posts():
    return Post.published.count()


# inclusion tag
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# simple tag that returns a queryset
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


# creating custom filter supporting Markdown syntax
@register.filter(name="markdown")
def markdown_formats(text):
    return mark_safe(markdown.markdown(text))
