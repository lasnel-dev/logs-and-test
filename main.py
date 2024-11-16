# import logging
#
# logging.basicConfig(level=logging.DEBUG,
#                     filename="Logs.log",
#                     filemode="a",
#                     format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s"
#                     )
#
# try:
#     print(10/0)
# except Exception as e:
#     logging.exception(e)


# assert 2 + 2 == 5, "2 + 2 don`t equal 5"
#
# """
# >>> 2 + 2
# 4
#
# >>> 7*2
# 14
# """
# a = 5
# b = 7
#
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass

    for _ in kwargs.values():
        if type(_) == int or type(_) == bool or type(_) == float:
            result += _
        else:
            try:
                result += float(_)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(_)
                continue
            except (ValueError, TypeError):
                pass
    return result