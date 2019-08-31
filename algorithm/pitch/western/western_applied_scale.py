from algorithm.pitch.applied_scale import AppliedOctavedScale
from algorithm.pitch.western.western_abstract_scale import WesternOctavedAbstractScale
from algorithm.pitch.western.western_chromatic_context import WesternChromaticContext


class WesternAppliedScale(AppliedOctavedScale):

    def __init__(self, chromatic_context, abstract_scale, scale_anchor=None):
        super().__init__(chromatic_context, abstract_scale, scale_anchor)

    @property
    def chromatic_context(self):
        return self._chromatic_context

    @chromatic_context.setter
    def chromatic_context(self, chromatic_context):
        if not issubclass(chromatic_context, WesternChromaticContext):
            raise TypeError('Chromatic context must be a subclass of WesternChromaticContext')
        self._chromatic_context = chromatic_context

    @property
    def abstract_scale(self):
        return self._abstract_scale

    @abstract_scale.setter
    def abstract_scale(self, abstract_scale):
        if not isinstance(abstract_scale, WesternOctavedAbstractScale):
            raise TypeError('Abstract scale must be of type WesternOctavedAbstractScale')
        self._abstract_scale = abstract_scale

    @property
    def name(self):
        return self.abstract_scale.render_name(self.scale_note)
