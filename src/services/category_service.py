from src.models.category import Category
from src.models.subcategory import SubCategory


class CategoryService:

    @staticmethod
    def getSubCategories(id_: int):
        return [subcat.name for subcat in SubCategory.query.filter_by(category=id_)]
