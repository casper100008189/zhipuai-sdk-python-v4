from __future__ import annotations

from typing import Union, List, Optional, TYPE_CHECKING

import httpx
from typing_extensions import Literal

from ...core._base_api import BaseAPI
from ...core._base_type import NotGiven, NOT_GIVEN, Headers
from ...core._http_client import make_user_request_input
from ...core._sse_client import StreamResponse
from ...types.chat import chat_completions_create_param
from ...types.chat.chat_completion import Completion
from ...types.chat.chat_completion_chunk import ChatCompletionChunk

if TYPE_CHECKING:
    from ..._client import ZhipuAI


class Completions(BaseAPI):
    def __init__(self, client: "ZhipuAI") -> None:
        super().__init__(client)

    def create(
            self,
            *,
            model: str,
            request_id: Optional[str] | NotGiven = NOT_GIVEN,
            do_sample: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            max_tokens: int | NotGiven = NOT_GIVEN,
            seed: int | NotGiven = NOT_GIVEN,
            messages: Union[str, List[str], List[int], object, None],
            stop: Optional[Union[str, List[str], None]] | NotGiven = NOT_GIVEN,
            tools: Optional[str] | NotGiven = NOT_GIVEN,
            tool_choice: str | NotGiven = NOT_GIVEN,
            extra_headers: Headers | None = None,
            disable_strict_validation: Optional[bool] | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion | StreamResponse[ChatCompletionChunk]:
        _cast_type = Completion
        _stream_cls = StreamResponse[ChatCompletionChunk]
        if disable_strict_validation:
            _cast_type = object
            _stream_cls = StreamResponse[object]
        return self._post(
            "/chat/completions",
            body={
                "model": model,
                "request_id": request_id,
                "temperature": temperature,
                "top_p": top_p,
                "do_sample": do_sample,
                "max_tokens": max_tokens,
                "seed": seed,
                "messages": messages,
                "stop": stop,
                "stream": stream,
                "tools": tools,
                "tool_choice": tool_choice,
            },
            options=make_user_request_input(
                extra_headers=extra_headers,
            ),
            cast_type=_cast_type,
            enbale_stream=stream or False,
            stream_cls=_stream_cls,
        )
