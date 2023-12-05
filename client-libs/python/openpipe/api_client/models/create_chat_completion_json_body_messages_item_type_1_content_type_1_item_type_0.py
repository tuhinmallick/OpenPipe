from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar

from attrs import define

from ..models.create_chat_completion_json_body_messages_item_type_1_content_type_1_item_type_0_type import (
    CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0Type,
)

if TYPE_CHECKING:
    from ..models.create_chat_completion_json_body_messages_item_type_1_content_type_1_item_type_0_image_url import (
        CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0ImageUrl,
    )


T = TypeVar("T", bound="CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0")


@define
class CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0:
    """
    Attributes:
        type (CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0Type):
        image_url (CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0ImageUrl):
    """

    type: CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0Type
    image_url: "CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0ImageUrl"

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        image_url = self.image_url.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "type": type,
                "image_url": image_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_chat_completion_json_body_messages_item_type_1_content_type_1_item_type_0_image_url import (
            CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0ImageUrl,
        )

        d = src_dict.copy()
        type = CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0Type(d.pop("type"))

        image_url = CreateChatCompletionJsonBodyMessagesItemType1ContentType1ItemType0ImageUrl.from_dict(
            d.pop("image_url")
        )

        return cls(
            type=type,
            image_url=image_url,
        )
