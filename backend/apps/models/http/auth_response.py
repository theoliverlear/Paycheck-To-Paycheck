from enum import Enum

from rest_framework import status

from backend.apps.comm.response.auth_status_response import AuthStatusResponse
from backend.apps.models.http.auth_status import AuthStatus
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse


class AuthResponse(Enum):
    UNAUTHORIZED: PayloadStatusResponse[AuthStatusResponse] = PayloadStatusResponse[AuthStatusResponse](
        payload=AuthStatusResponse(auth_status=AuthStatus.UNAUTHORIZED),
        status_code=status.HTTP_401_UNAUTHORIZED
    )
    AUTHORIZED: PayloadStatusResponse[AuthStatusResponse] = PayloadStatusResponse[AuthStatusResponse](
        payload=AuthStatusResponse(auth_status=AuthStatus.AUTHORIZED),
        status_code=status.HTTP_200_OK
    )
    IN_SESSION_CONFLICT: PayloadStatusResponse[AuthStatusResponse] = PayloadStatusResponse[AuthStatusResponse](
        payload=AuthStatusResponse(auth_status=AuthStatus.AUTHORIZED),
        status_code=status.HTTP_409_CONFLICT
    )
    CONFLICT: PayloadStatusResponse[AuthStatusResponse] = PayloadStatusResponse[AuthStatusResponse](
        payload=AuthStatusResponse(auth_status=AuthStatus.UNAUTHORIZED),
        status_code=status.HTTP_409_CONFLICT
    )