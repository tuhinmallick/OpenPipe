from typing import Any, Dict, Type, TypeVar

from attrs import define

T = TypeVar("T", bound="CreateChatCompletionJsonBodyToolChoiceType2Function")


@define
class CreateChatCompletionJsonBodyToolChoiceType2Function:
    """
    Attributes:
        name (str):
    """

    name: str

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        field_dict: Dict[str, Any] = {"name": name}
        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        return cls(
            name=name,
        )
