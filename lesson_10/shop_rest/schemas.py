from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length


class AuthorSchema(Schema):
    id = fields.String(dump_only=True)
    first_name = fields.String(validate=Length(min=2, max=65), required=True)
    last_name = fields.String(validate=Length(min=2, max=65), required=True)
    count_post = fields.Integer()


class TagSchema(Schema):
    id = fields.String(dump_only=True)
    text = fields.String(validate=Length(min=2, max=65), required=True)


class BlogPostSchemaRead(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(validate=Length(min=2, max=100), required=True)
    content = fields.String(required=True)
    published = fields.DateTime(format='%Y-%m-%d %H:%M')
    author = fields.Nested(AuthorSchema)
    post_view = fields.Integer()
    tags = fields.List(fields.Nested(TagSchema))


class BlogPostSchemaWrite(BlogPostSchemaRead):
    author = fields.String()