from injector import inject
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.comm.serialize.entity.wallet.wallet_serializer import \
    WalletSerializer
from backend.apps.comm.serialize.models.http.payload_status_response_serializer import \
    PayloadStatusResponseSerializer
from backend.apps.models.http.operation_sucess_status import \
    OperationSuccessStatus
from backend.apps.services.session.session_service import SessionService
from backend.apps.services.wallet_service import WalletService


class SetWalletView(APIView):
    @inject
    def __init__(self,
                 session_service: SessionService,
                 wallet_service: WalletService):
        super().__init__()
        self.session_service: SessionService = session_service
        self.wallet_service: WalletService = wallet_service

    def post(self, http_request, *args, **kwargs):
        # TODO: Get User object to map
        if not self.session_service.user_in_session(http_request):
            response_serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(OperationSuccessStatus.OPERATION_DENIED.value)
            return Response(response_serializer.data)


        wallet_serializer: WalletSerializer = WalletSerializer(data=http_request.data)
        if wallet_serializer.is_valid():
            wallet = wallet_serializer.get_instance()
            self.wallet_service.save_or_update_wallet(wallet)
            response_serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(OperationSuccessStatus.OPERATION_SUCCESS.value)
            return Response(response_serializer.data)
        else:
            response_serializer: PayloadStatusResponseSerializer = PayloadStatusResponseSerializer(OperationSuccessStatus.OPERATION_FAILURE.value)
            return Response(response_serializer.data)
