from collections.abc import ItemsView, Iterable, KeysView, Set, ValuesView


def _abc_itemsview_register(view_cls):
    ItemsView.register(view_cls)


def _abc_keysview_register(view_cls):
    KeysView.register(view_cls)


def _abc_valuesview_register(view_cls):
    ValuesView.register(view_cls)


def _viewbaseset_richcmp(view, other, op):
    if op == 0:
        if not isinstance(other, Set):
            return NotImplemented
        return len(view) < len(other) and view <= other
    elif op == 1:
        if not isinstance(other, Set):
            return NotImplemented
        return False if len(view) > len(other) else all(elem in other for elem in view)
    elif op == 2:
        if not isinstance(other, Set):
            return NotImplemented
        return len(view) == len(other) and view <= other
    elif op == 3:
        return view != other
    elif op == 4:
        if not isinstance(other, Set):
            return NotImplemented
        return len(view) > len(other) and view >= other
    elif op == 5:
        if not isinstance(other, Set):
            return NotImplemented
        return False if len(view) < len(other) else all(elem in view for elem in other)


def _viewbaseset_and(view, other):
    if not isinstance(other, Iterable):
        return NotImplemented
    if isinstance(view, Set):
        view = set(iter(view))
    if isinstance(other, Set):
        other = set(iter(other))
    if not isinstance(other, Set):
        other = set(iter(other))
    return view & other


def _viewbaseset_or(view, other):
    if not isinstance(other, Iterable):
        return NotImplemented
    if isinstance(view, Set):
        view = set(iter(view))
    if isinstance(other, Set):
        other = set(iter(other))
    if not isinstance(other, Set):
        other = set(iter(other))
    return view | other


def _viewbaseset_sub(view, other):
    if not isinstance(other, Iterable):
        return NotImplemented
    if isinstance(view, Set):
        view = set(iter(view))
    if isinstance(other, Set):
        other = set(iter(other))
    if not isinstance(other, Set):
        other = set(iter(other))
    return view - other


def _viewbaseset_xor(view, other):
    if not isinstance(other, Iterable):
        return NotImplemented
    if isinstance(view, Set):
        view = set(iter(view))
    if isinstance(other, Set):
        other = set(iter(other))
    if not isinstance(other, Set):
        other = set(iter(other))
    return view ^ other


def _itemsview_isdisjoint(view, other):
    "Return True if two sets have a null intersection."
    return all(v not in view for v in other)


def _itemsview_repr(view):
    lst = ["{!r}: {!r}".format(k, v) for k, v in view]
    body = ", ".join(lst)
    return f"{view.__class__.__name__}({body})"


def _keysview_isdisjoint(view, other):
    "Return True if two sets have a null intersection."
    return all(k not in view for k in other)


def _keysview_repr(view):
    lst = ["{!r}".format(k) for k in view]
    body = ", ".join(lst)
    return f"{view.__class__.__name__}({body})"


def _valuesview_repr(view):
    lst = ["{!r}".format(v) for v in view]
    body = ", ".join(lst)
    return f"{view.__class__.__name__}({body})"


def _mdrepr(md):
    lst = ["'{}': {!r}".format(k, v) for k, v in md.items()]
    body = ", ".join(lst)
    return f"<{md.__class__.__name__}({body})>"
