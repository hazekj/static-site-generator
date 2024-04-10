from typing import Optional, Self


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list[Self]] = None,
        props: Optional[dict[str, str]] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        if len(self.props) == 0:
            return ""
        attributes = []
        for k, v in self.props.items():
            attributes.append(f' {k}="{v}"')
        return "".join(attributes)

    def __repr__(self) -> str:
        return f"""HTMLNode(tag: {self.tag},
        value: {self.value},
        children: {self.children},
        props: {self.props})"""


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str, value: str, props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(
        self, tag: str, children: list[Self], props: dict[str, str] | None = None
    ) -> None:

        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Must have tag")
        if self.children is None:
            raise ValueError("Not a parent node")

        children_list = [node.to_html() for node in self.children]
        return "".join(children_list)
