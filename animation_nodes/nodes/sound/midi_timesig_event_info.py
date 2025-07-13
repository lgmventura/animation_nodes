import bpy
from ... base_types import AnimationNode, VectorizedSocket

class MIDITimeSignatureInfoNode(AnimationNode, bpy.types.Node):
    bl_idname = "an_MIDITimeSignatureInfoNode"
    bl_label = "MIDI Time Signature Info"

    useTimeSigsList: VectorizedSocket.newProperty()

    def create(self):
        self.newInput(VectorizedSocket("MIDI Time Signature", "useTimeSigsList",
            ("Time Signature Event", "timeSigEvent"), ("Time Signature Events", "timeSigEvents")))
        self.newOutput(VectorizedSocket("Float", "useTimeSigsList",
            ("Time in Quarter Note", "timeInQuarterNotes"), ("Times in Quarter Note", "timesInQuarterNotes")))
        self.newOutput(VectorizedSocket("Float", "useTimeSigsList",
            ("Time in seconds", "timeInSeconds"), ("Times in seconds", "timesInSeconds")))
        self.newOutput(VectorizedSocket("Integer", "useTimeSigsList",
            ("Numerator", "numerator"), ("Numerators", "numerators")))
        self.newOutput(VectorizedSocket("Integer", "useTimeSigsList",
            ("Denominator", "denominator"), ("Denominators", "denominators")))

    def getExecutionCode(self, required):
        if not self.useTimeSigsList:
            if "timeInQuarterNotes" in required:
                yield "timeInQuarterNotes = timeSigEvent.timeInQuarterNotes"
            if "timeInSeconds" in required:
                yield "timeInSeconds = timeSigEvent.timeInSeconds"
            if "numerator" in required:
                yield "numerator = timeSigEvent.numerator"
            if "denominator" in required:
                yield "denominator = timeSigEvent.denominator"
        else:
            if "timesInQuarterNotes" in required:
                yield "timesInQuarterNotes = DoubleList.fromValues(timeSigEvent.timeInQuarterNotes for timeSigEvent in timeSigEvents)"
            if "timesInSeconds" in required:
                yield "timesInSeconds = DoubleList.fromValues(timeSigEvent.timeInSeconds for timeSigEvent in timeSigEvents)"
            if "numerators" in required:
                yield "numerators = LongList.fromValues(timeSigEvent.numerator for timeSigEvent in timeSigEvents)"
            if "denominators" in required:
                yield "denominators = LongList.fromValues(timeSigEvent.denominator for timeSigEvent in timeSigEvents)"
