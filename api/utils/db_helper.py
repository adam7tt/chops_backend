'''
    Database Helpers
'''

def _unique(session, cls, hashfunc, queryfunc, constructor, arg, kw):
    # debug = True
    is_new = True
    cache = getattr(session, '_unique_cache', None)
    if cache is None:
        session._unique_cache = cache = {}

    key = (cls, hashfunc(*arg, **kw))
    if key in cache:
        # print("\nFound on cache {}".format(cache[key]))
        is_new = False
        # return cache[key], is_new
    else:
        with session.no_autoflush:
            q = session.query(cls)
            q = queryfunc(query=q, *arg, **kw)
            obj = q.first()
            # print(obj)
            if not obj:
                obj = constructor(*arg, **kw)
                # print('\nNew created, {}'.format(obj))
                session.add(obj)
                session.flush()
            else:
                # print('\n{} found on DB {} with id {}'.format(cls, obj, obj.id))
                is_new = False
        cache[key] = obj
        # return obj, is_new
    return cache[key], is_new


class UniqueMixin(object):
    @classmethod
    def unique_hash(cls, *arg, **kw):
        raise NotImplementedError()

    @classmethod
    def unique_filter(cls, query, *arg, **kw):
        raise NotImplementedError()

    @classmethod
    def as_unique(cls, session, *arg, **kw):
        return _unique(
            session,
            cls,
            cls.unique_hash,
            cls.unique_filter,
            cls,
            arg, kw
        )