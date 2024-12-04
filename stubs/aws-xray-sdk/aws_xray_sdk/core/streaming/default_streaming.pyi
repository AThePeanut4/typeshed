class DefaultStreaming:
    """
    The default streaming strategy. It uses the total count of a
    segment's children subsegments as a threshold. If the threshold is
    breached, it uses subtree streaming to stream out.
    """
    def __init__(self, streaming_threshold: int = 30) -> None: ...
    def is_eligible(self, segment):
        """
        A segment is eligible to have its children subsegments streamed
        if it is sampled and it breaches streaming threshold.
        """
        ...
    def stream(self, entity, callback) -> None:
        """
        Stream out all eligible children of the input entity.

        :param entity: The target entity to be streamed.
        :param callback: The function that takes the node and
            actually send it out.
        """
        ...
    @property
    def streaming_threshold(self): ...
    @streaming_threshold.setter
    def streaming_threshold(self, value) -> None: ...
