from django.db.models import Model, CharField, IntegerField, \
    ForeignKey, TextField, DateField, FloatField, BooleanField,\
    DateTimeField, TextChoices, ImageField, FileField, CASCADE,\
    SlugField, ManyToManyField
from django.template.defaultfilters import slugify
from django.db.utils import IntegrityError

class QualityChoices(TextChoices):
    HD = 'hd', 'HD'
    FULL_HD = 'full_hd', 'Full HD'
    _4K = '_4k', '4K'


class MovieStatusChoices(TextChoices):
    RELEASED = 'released', 'Released'
    COMING_SOON = 'coming_soon', 'Coming Soon'
    IN_PRODUCTION = 'in_production', 'In Production'
    POST_PRODUCTION = 'post_production', 'Post Production'
    CANCELLED = 'cancelled', 'Cancelled'
    ANNOUNCED = 'announced', 'Announced'
    AIRING = 'airing', 'Airing'


class MovieTypeChoices(TextChoices):
    REGULAR = 'regular', 'Regular'
    BANNER = 'banner', 'Banner'


class Movie(Model):
    title = CharField(max_length=555, help_text="Kino sarlavhasi")
    description = TextField(help_text="Kino tavsilotlari")
    duration = IntegerField(help_text="Kino davomiyligi (minutda)")
    movie_type = CharField(max_length=255, help_text="Kino janri")
    studios = CharField(max_length=350, help_text="Ishlab chiqaruvchi studio")
    release_date = DateField(help_text="Kino premyerasi sana")
    rating = FloatField(help_text="Kino reytingi")
    views = IntegerField(help_text="Ko'rishlar soni")
    is_active = BooleanField(default=True, help_text="Aktivligi")

    quality = CharField(max_length=20, choices=QualityChoices.choices)
    scores = FloatField(help_text="Scoring")
    
    status = CharField(max_length=25, choices=MovieStatusChoices.choices,
                       default=MovieStatusChoices.COMING_SOON,
                       help_text="Kino statusi")

    image = ImageField(upload_to='movie_images/', help_text="Kino banneri")
    video = FileField(upload_to='movies/', help_text="Kino/Treyler fayli")
    thumb = FileField(upload_to='movie_thumbs/', help_text="Thumb fayli",
                      null=True, blank=True)

    type = CharField(max_length=20, choices=MovieTypeChoices.choices,
                     default=MovieTypeChoices.REGULAR, 
                     help_text="Kino joylashuvi")
    
    slug = SlugField(unique=True, null=True, blank=True)
    created_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)
    movie_genre = ManyToManyField('Genre', through='MovieGenre')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            try:
                self.slug = slugify(self.title)
            except IntegrityError:
                self.slug += str(1)                
            print(f"{self.slug=}")
        super().save(*args, **kwargs)


class Genre(Model):
    name = CharField(max_length=255, help_text="Kino Janri")

    def __str__(self):
        return self.name
  

class MovieGenre(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE)
    genre = ForeignKey(Genre, on_delete=CASCADE)
