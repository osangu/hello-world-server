from typing import Optional

from jwt import decode
from jwt.exceptions import ExpiredSignatureError
from jwt.exceptions import (InvalidKeyError,
                            InvalidTokenError,
                            InvalidSignatureError,
                            InvalidAlgorithmError)

from .data import Payload


class Decoder:

    def __call__(self, jwt: str, key: str) -> Optional[Payload]:
        try:
            payload_dict = decode(jwt=jwt, key=key)

            return Payload(**payload_dict)

        except ExpiredSignatureError as ExpiredError:
            raise ExpiredError

        except (
                InvalidKeyError, InvalidSignatureError,
                InvalidTokenError, InvalidAlgorithmError
        ) as InvalidError:
            raise InvalidError

    def access_token(self, jwt: str) -> Optional[Payload]:
        return self(jwt=jwt, key="")

    def refresh_token(self, jwt: str) -> Optional[Payload]:
        return self(jwt=jwt, key="")
