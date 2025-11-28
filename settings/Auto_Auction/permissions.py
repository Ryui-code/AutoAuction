from rest_framework.permissions import BasePermission, SAFE_METHODS


class CheckStatus(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        role = getattr(user, 'role', None)
        try:
            model_name = view.get_queryset().model.__name__

        except Exception:
            return True

        if role == 'Buyer':
            if model_name == 'Car':
                return False
            if model_name == 'Auction':
                return request.method in SAFE_METHODS
            return False

        if role == 'Seller':
            if model_name == 'Auction':
                return True
            if model_name == 'Car':
                return True
            if model_name == 'Feedback':
                return request.method in SAFE_METHODS
            return False