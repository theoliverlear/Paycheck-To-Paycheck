from enum import Enum

from rest_framework import status

from backend.apps.comm.response.operation_success_response import \
    OperationSuccessResponse
from backend.apps.models.http.payload_status_response import \
    PayloadStatusResponse


class OperationSuccessStatus(Enum):
    OPERATION_SUCCESS: PayloadStatusResponse[OperationSuccessResponse] = PayloadStatusResponse[OperationSuccessResponse](
        payload=OperationSuccessResponse(True),
        status_code=status.HTTP_200_OK
    )
    OPERATION_DENIED: PayloadStatusResponse[OperationSuccessResponse] = PayloadStatusResponse[OperationSuccessResponse](
        payload=OperationSuccessResponse(False),
        status_code=status.HTTP_400_BAD_REQUEST
    )
    OPERATION_FAILURE: PayloadStatusResponse[OperationSuccessResponse] = PayloadStatusResponse[OperationSuccessResponse](
        payload=OperationSuccessResponse(False),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )