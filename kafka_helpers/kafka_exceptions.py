"""
    Purpose:
        File for holding custom exception types that will be generated by the
        kafka_helpers libraries
"""


###
# Consumer Exceptions
###


class TopicNotFound(Exception):
    """
    Purpose:
        The TopicNotFound will be raised when attempting to consume a topic that
        does not exist
    """

    pass


###
# Producer Exceptions
###



