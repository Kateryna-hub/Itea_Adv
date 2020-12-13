import mongoengine as me
import datetime
import random


me.connect('BLOG')


class Author(me.Document):
    first_name = me.StringField(min_length=2, max_length=65)
    last_name = me.StringField(min_length=2, max_length=65)
    count_post = me.IntField(default=0)

    def __str__(self):
        return str(self.id)


class Tag(me.Document):
    text = me.StringField()


class BlogPost(me.Document):
    title = me.StringField(min_length=2, max_length=100)
    content = me.StringField()
    published = me.DateTimeField()
    author = me.ReferenceField(Author, reverse_delete_rule='CASCAD')
    post_view = me.IntField(default=0)
    tags = me.ListField(me.ReferenceField(Tag))

    def save(self, *args, **kwargs):
        self.published = datetime.datetime.now()
        Author.objects(id=self.author).update_one(inc__count_post=1)
        super().save(*args, **kwargs)


if __name__ == '__main__':
    pass
    # for ath in authors:
    #     at = Author(first_name=ath[0], last_name=ath[1]).save()
    #     print(at.id)
    #
    # for dict_ in posts:
    #     blogp = BlogPost(title=posts[dict_]['title'], content=posts[dict_]['content'],
    #                      author=random.choice(Author.objects()))
    #     blogp.save()
    #     for t in posts[dict_]['tag']:
    #         tg = Tag(text=t).save()
    #         blogp.tags.append(tg)
    #         blogp.save()
    #