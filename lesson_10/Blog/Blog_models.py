import mongoengine as me
import datetime
import random

authors = [['Nikolay', 'Ivanov'], ['Semen', 'Petrov'], ['Ivan', 'Frolov'], ['Boris', 'Sidorov']]
posts = [[['tag1', 'test'], 'title1', 'there must be some kind of text written by '],
         [['tag2', 'some text'], 'title2', 'there must be some kind of text written by '],
         [['tag3', 'tag1'], 'title3', 'there must be some kind of text written by '],
         [['tag4', 'tag'], 'title4', 'there must be some kind of text written by '],
         [['tag5', 'other text'], 'title5', 'there must be some kind of text written by '],
         [['tag6', 'tag3'], 'title6', 'there must be some kind of text written by ']]


me.connect('BLOGS1')


class Author(me.Document):
    first_name = me.StringField()
    last_name = me.StringField()
    count_post = me.IntField(default=0)

    def __str__(self):
        return str(self.id)


class Tag(me.Document):
    text = me.StringField()


class Post(me.Document):
    title = me.StringField(min_length=2, max_length=100, required=True)
    content = me.StringField(required=True)
    published = me.DateTimeField()
    author = me.ReferenceField(Author, reverse_delete_rule='CASCADE')
    count_view = me.IntField(default=0)
    tags = me.ListField(me.StringField(max_length=100))

    def save(self, *args, **kwargs):
        self.published = datetime.datetime.now()
        super().save(*args, **kwargs)

