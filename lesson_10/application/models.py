import mongoengine as me

me.connect('REST_API_LESSON_10')


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=64, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    interests = me.ListField()
    age = me.IntField(min_value=12, max_value=99)
    created_at = me.DateTimeField()


if __name__ == '__main__':
    User(first_name='Nikolai', interests=['cars'], age=23).save()
    User(first_name='James', interests=['programming'], age=20).save()


# User.drop_collection()
# User.objects().delete()