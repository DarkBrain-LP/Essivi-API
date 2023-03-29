from src.models.category import Category


class SubCategoryService:

    @staticmethod
    def getCategoryName(id_: int):
        return Category.query.filter_by(id=id_).first().name
