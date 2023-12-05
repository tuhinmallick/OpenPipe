from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_chat_completion_json_body_functions_item_parameters import (
        CreateChatCompletionJsonBodyFunctionsItemParameters,
    )


T = TypeVar("T", bound="CreateChatCompletionJsonBodyFunctionsItem")


@define
class CreateChatCompletionJsonBodyFunctionsItem:
    """
    Attributes:
        name (str):
        parameters (CreateChatCompletionJsonBodyFunctionsItemParameters):
        description (Union[Unset, str]):
    """

    name: str
    parameters: "CreateChatCompletionJsonBodyFunctionsItemParameters"
    description: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        parameters = self.parameters.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "parameters": parameters,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_chat_completion_json_body_functions_item_parameters import (
            CreateChatCompletionJsonBodyFunctionsItemParameters,
        )

        d = src_dict.copy()
        name = d.pop("name")

        parameters = CreateChatCompletionJsonBodyFunctionsItemParameters.from_dict(d.pop("parameters"))

        description = d.pop("description", UNSET)

        return cls(
            name=name,
            parameters=parameters,
            description=description,
        )
