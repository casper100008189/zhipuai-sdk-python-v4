from __future__ import annotations

from typing import Union, List, Optional, TYPE_CHECKING

import httpx

from ..core._base_api import BaseAPI
from ..core._base_type import NotGiven, NOT_GIVEN, Headers
from ..core._http_client import make_user_request_input
from ..types.embeddings import EmbeddingsResponded

if TYPE_CHECKING:
    from zhipuai._client import ZhipuAI


class Embeddings(BaseAPI):
    def __init__(self, client: "ZhipuAI") -> None:
        super().__init__(client)

    def create(
            self,
            *,
            input: Union[str, List[str], List[int], List[List[int]]],
            model: Union[str],
            encoding_format: str | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            extra_headers: Headers | None = None,
            disable_strict_validation: Optional[bool] | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingsResponded:
        _cast_type = EmbeddingsResponded
        if disable_strict_validation:
            _cast_type = object
        return self._post(
            "/embeddings",
            body={
                "input": input,
                "model": model,
                "encoding_format": encoding_format,
                "user": user,
            },
            options=make_user_request_input(
                extra_headers=extra_headers, timeout=timeout
            ),
            cast_type=_cast_type,
            enbale_stream=False,
        )
