import mongoengine as me

me.commect('BLOGS')


class Post(me.Document):
    title = me.StringField(min_length=2, max_length=100, required=True)
    content = me.StringField(required=True)
    created_at = me.DateTimeField()
    author = me.StringField(min_length=2, max_length=65, required=True)
    count_view = me.IntField(default=0)
    teg = me.ReferenceField(Teg)


class Teg(me.Document):




class Author(me.Document):
    first_name = me.StringField()
    last_name = me.StringField()
    count_post = me.IntField(default=0)
    post = me.ReferenceField(Post)

