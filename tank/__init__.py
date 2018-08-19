class CommonUtil:
    @staticmethod
    def has_attr(target, key):
        try:
            return object.__getattribute__(target, key)
        except AttributeError:
            return None
