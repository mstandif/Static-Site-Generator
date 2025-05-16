from enum import Enum

class TextType(Enum):
    NORMAL = "1"
    BOLD = "2"
    ITALIC = "3"
    LINKS = "4"
    IMAGES = "5"

class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(first_class, second_class):
        if first_class.text == second_class.text:
            if first_class.text_type.value == second_class.text_type.value:
                if first_class.url == second_class.url:
                    return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"