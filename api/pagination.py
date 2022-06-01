from rest_framework.pagination import LimitOffsetPagination

class Pag(LimitOffsetPagination):
    default_limit=2