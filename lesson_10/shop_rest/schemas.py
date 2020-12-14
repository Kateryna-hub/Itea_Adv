from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length


class CategorySchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(validate=Length(min=2, max=65), required=True)
    parent = fields.Nested('self')
    subcategories = fields.Nested('self')


class ShopProductSchemaRead(Schema):
    id = fields.String(dump_only=True)
    title = fields.String(required=True, max_length=256)
    description = fields.String(max_length=512)
    in_stock = fields.Boolean(default=True)
    number = fields.Integer(default=0)
    price = fields.Float(required=True)
    category = fields.Nested(CategorySchema)
    view = fields.Integer(default=0)


class ShopProductSchemaWrite(ShopProductSchemaRead):
    category = fields.String()