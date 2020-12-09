import mongoengine as me
import datetime
import random

authors = [['Nikolay', 'Ivanov'], ['Semen', 'Petrov'], ['Ivan', 'Frolov'], ['Boris', 'Sidorov']]
posts = {'post1': {
            'title': 'Make My Life Easier',
            'content': 'At one point, I worked as the internet sales manager at a car dealership. '
                       'I found a lot of our customers we are not interested in the best way to buy a car, '
                       'which is save money and pay cash. \n They were very interested, however, '
                       'in the easiest way. Our most successful content was helping our customers '
                       'do things easier.',
            'tag': ['sales manager']
            },
        'post2': {
            'title':'Why You Should Forget Facebook',
            'content': "This title, in particular, was especially powerful to me for two reasons. The first, "
                    "The second reason was because it caused cognitive dissonance - Facebook is one of the largest "
                    "platforms available to marketers, yet this title says I should walk away and forget it. "
                    "And it worked. This post was viewed around 300,000 times.",
            'tag': ['Facebook', 'Forget']
            },
        'post3': {
            'title':'Backed By Science',
            'content': "Humans have a thing called a learning bias. No matter how wise a saying is, we are much "
                       "more apt to accept it as true if we trust the source. Not only that, but we are fascinated "
                       "by ultimate truths that spur us into action.",
            'tag': ['Backed', 'Science']
            },
        'post4': {
            'title': "Why Steve Jobs Did not Let His Kids Use iPads ",
            'content': "Experience is the best teacher. But sometimes, the tuition is just too high. Smart people learn "
                       "from other's mistakes. They also learn from other's success.",
            'tag': ['Steve Jobs', 'iPads']
            },
        'post5': {
            'title': 'Why Successful People Never Bring Smartphones',
            'content': "We all want to know how other people 'made it,' and this 'Why X People Do X' headline gives "
                       "insight into how they, too, might be successful.",
            'tag': ['Successful People', 'Smartphones']
            },
        'post6': {
            'title':'7 Things You Need to Know About Narcissists',
            'content':"This 'Don't Be Ignorant' headline makes consumers feel like they need to click on it and be 'in the know'",
            'tag': ['Narcissists', 'Psychology']
          }}




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

