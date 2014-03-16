from django.db import models
from django.db.models import Count, Max
from django.template.defaultfilters import striptags, truncatechars
from django.utils.encoding import force_str, force_text

from ckeditor.fields import RichTextField


class CategoryManager(models.Manager):

    def with_entry_count(self):
        return self.annotate(entries_count=Count('entries', field='CASE WHEN blog_entry.is_published THEN 1 END'))

    def active(self):
        return self.with_entry_count().filter(entries_count__gt=0).order_by('-entries_count')

    def with_last_modified(self):
        return self.annotate(
            modified=Max('entries__created', field='CASE WHEN blog_entry.is_published THEN blog_entry.created END')
        ).exclude(modified=None).order_by('-modified')


class Category(models.Model):
    """
    Every blog entry is put in some category
    This model describe blog entry categories
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)

    objects = CategoryManager()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return force_str(self.title)

    def __unicode__(self):
        return force_text(self.__str__())

    @models.permalink
    def get_absolute_url(self):
        return ('blog:category', (), {'category': self.slug})


class EntryManager(models.Manager):

    def get_query_set(self):
        return super(EntryManager, self).get_query_set().select_related('category')

    def published(self):
        return self.filter(is_published=True)


class Entry(models.Model):
    """
    This models describe every blog entry with his
    category, title, slug and content
    """
    category = models.ForeignKey(Category, related_name='entries')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    content = RichTextField()

    seo_keywords = models.CharField(max_length=128, blank=True, default='')
    seo_description = models.CharField(max_length=256, blank=True, default='')

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)
    is_published = models.BooleanField()

    objects = EntryManager()

    class Meta:
        unique_together = (('category', 'slug',),)
        ordering = ('-created',)
        verbose_name_plural = 'entries'

    def __str__(self):
        return force_str(truncatechars(self.title, 60))

    def __unicode__(self):
        return force_text(self.__str__())

    @models.permalink
    def get_absolute_url(self):
        return ('blog:entry', [], {'category': self.category.slug, 'entry': self.slug})

    def get_identifier(self):
        """
        Identifier used in disqus
        """
        return '%s-%s' % (self.category.slug, self.slug,)

    def get_seo_description(self):
        return self.seo_description or truncatechars(striptags(self.content), 200).replace('\n', ' ').replace('\r', '')
