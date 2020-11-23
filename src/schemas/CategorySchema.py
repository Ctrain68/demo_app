from main import ma                                                   
from models.Category import Category                                      
from marshmallow.validate import Length                               
from schemas.UserSchema import UserSchema


class CategorySchema(ma.SQLAlchemyAutoSchema):                          
    class Meta:
        model = Category                                                

    title = ma.String(required=True, validate=Length(min=1))          
    description = ma.String(required=True, validate=Length(min=1))    
    private = db.Column(required=True)
    owner = ma.Nested(UserSchema) 
    
category_schema = CategorySchema()                                       
categories_schema = CategorySchema(many=True)     