""" http://tkinter.unpythonic.net/wiki/WidgetWalker """


# TODO: Need examples for this.


def hierarchy(widget):
    """Return the widget hierarchy (from widget, down) as nested dicts.
    Each dict is as follows:
    {"path": path,
     "name": name,
     "id": (integer id),
     "widget": (widget),
     "class": class_string,
     "children": (...,
                  ...)}
    """
    _id = widget.winfo_id()
    return {"path": widget.winfo_pathname(_id),
            "name": widget.winfo_name(),
            "id": _id,
            "widget": widget,
            "class": widget.winfo_class(),
            "children":
                tuple([hierarchy(w)
                       for w in widget.winfo_children()])}

def print_hierarchy(widget):
    """Print the hierarchy of a widget.

    All widgets are shown in the hierarchy;
    WANTED: The widget itself is surrounded with a [[]] marker.
    """
    def print_partial(info, depth):
        spaces = "  "*depth
        content = "{name} [{id}] <{class}>".format(**info)
        print(spaces, end="")
        if info["widget"] == widget:
            print("** {} **".format(content))
        else:
            print(content)
        for child in info["children"]:
            print_partial(child, depth+1)
    print_partial(hierarchy(widget.nametowidget(".")), 0)
