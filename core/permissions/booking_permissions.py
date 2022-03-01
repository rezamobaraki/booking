def has_search_key(self, request, view):
    search_key = request.data.get('search_key', None)
    if search_key is None:
        return False
    return True
