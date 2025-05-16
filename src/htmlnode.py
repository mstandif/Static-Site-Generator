class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        my_string = ""
        for key in self.props.keys():
            my_string.append(f" {key}=\"{self.props[key]}\"")
        return my_string

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children.value} {self.props_to_html}"