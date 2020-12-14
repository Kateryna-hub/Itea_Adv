import mongoengine as me
import random


me.connect('SHOP10')


class Category(me.Document):
    title = me.StringField(required=True)
    parent = me.ReferenceField('self')
    subcategories = me.ListField(me.ReferenceField('self'))

    def __str__(self):
        return str(self.id)

    def get_products(self):
        return Product.objects(Category=self)

    @classmethod
    def get_root_categories(cls):
        return cls.objects(
            parent=None
        )

    def is_root(self):
        return not bool(self.parent)

    def add_subcategory(self, category):
        category.parent = self
        category.save()
        self.subcategories.append(category)
        self.save()


class Product(me.Document):
    title = me.StringField(required=True, max_length=256)
    description = me.StringField(max_length=512)
    in_stock = me.BooleanField(default=True)
    number = me.IntField(default=0)
    price = me.FloatField(required=True)
    category = me.ReferenceField(Category)
    view = me.IntField(default=0)


if __name__ == '__main__':
    pass
    # for c in categories:
    #     at = Category().save()
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