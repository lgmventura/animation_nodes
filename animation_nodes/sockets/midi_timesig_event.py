import bpy
from .. data_structures import MIDITimeSignatureEvent
from .. base_types import AnimationNodeSocket, PythonListSocket

class MIDITimeSignatureEventSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_MIDITimeSignatureSocket"
    bl_label = "MIDI Time Signature Socket"
    dataType = "MIDI Time Signature"
    drawColor = (0.6, 0.75, 0.45, 1)
    storable = True
    comparable = False

    @classmethod
    def getDefaultValue(cls):
        return MIDITimeSignatureEvent()

    @classmethod
    def getCopyExpression(cls):
        return "value.copy()"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, MIDITimeSignatureEvent):
            return value, 0
        return cls.getDefaultValue(), 2

class MIDITimeSignatureListSocket(bpy.types.NodeSocket, PythonListSocket):
    bl_idname = "an_MIDITimeSignatureListSocket"
    bl_label = "MIDI Time Signature Event List Socket"
    dataType = "MIDI Time Signature Event List"
    baseType = MIDITimeSignatureEventSocket
    drawColor = (0.6, 0.75, 0.45, 0.5)
    storable = True
    comparable = False

    @classmethod
    def getCopyExpression(cls):
        return "[timeSigEvent.copy() for timeSigEvent in value]"

    @classmethod
    def correctValue(cls, value):
        if isinstance(value, list):
            if all(isinstance(element, MIDITimeSignatureEvent) for element in value):
                return value, 0
        return cls.getDefaultValue(), 2
