from rest_framework import pagination


class Pagination(pagination.PageNumberPagination):
    page_size = 45
    page_size_query_param = "page_size"