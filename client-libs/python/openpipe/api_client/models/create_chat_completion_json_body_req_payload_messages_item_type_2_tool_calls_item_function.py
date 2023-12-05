from typing import Any, Dict, Type, TypeVar

from attrs import define

T = TypeVar("T", bound="CreateChatCompletionJsonBodyReqPayloadMessagesItemType2ToolCallsItemFunction")


@define
class CreateChatCompletionJsonBodyReqPayloadMessagesItemType2ToolCallsItemFunction:
    """
    Attributes:
        name (str):
        arguments (str):
    """

    name: str
    arguments: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        arguments = self.arguments

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "arguments": arguments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        arguments = d.pop("arguments")

        return cls(
            name=name,
            arguments=arguments,
        )
