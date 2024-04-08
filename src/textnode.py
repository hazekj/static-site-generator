from typing import Optional


class TextNode:
    def __init__(self, text: str, text_type: str, url: Optional[str] = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return all(
            self.text == other.text,
            self.text_type == other.text_type,
            self.url == other.url,
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
