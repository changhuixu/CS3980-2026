from beanie import Document


class Product(Document):
    name: str
    category: str

    class Settings:
        name = "products"  # by default, if not setting this one, then MongoDB will use the class name as the collection name.
