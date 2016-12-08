import abc


class Processor(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        return

    @abc.abstractmethod
    def process(self):
        return
