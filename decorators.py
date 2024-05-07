def GET(path):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator

def PUT(path):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator

def memory_size(arg):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator

def timeout(arg):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator

def environment(*args,  **kwargs):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator

def runtime(arg):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator

def environment(*args):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator

def description(arg):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator

def name(arg):
    def decorator(fun):
        def wrapper(*args,  **kwargs):
            result = fun(*args, **kwargs)
            return result
        return wrapper
    return decorator
