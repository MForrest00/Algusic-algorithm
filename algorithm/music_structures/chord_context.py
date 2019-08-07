class ChordContext:

    def __init__(self, scale_context):
        self.scale_context = scale_context

    @property
    def chromatic_context(self):
        return self.scale_context.chromatic_context
