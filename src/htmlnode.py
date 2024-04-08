from typing import Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list[HTMLNode]] = None,
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
