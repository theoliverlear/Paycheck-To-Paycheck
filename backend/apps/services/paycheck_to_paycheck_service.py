from backend.apps.entity.user.user import User


class PaycheckToPaycheckService:
    def __init__(self):
        pass

    def remove_user_from_session(self, http_request):
        if self.user_in_session(http_request):
            del http_request.session['user_id']

    def save_user_to_session(self, user: User, http_request) -> None:
        http_request.session['user_id'] = user.id

    def user_in_session(self, http_request) -> bool:
        return 'user_id' in http_request.session
