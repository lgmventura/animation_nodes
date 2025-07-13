from dataclasses import dataclass

@dataclass
class MIDITimeSignatureEvent:
    timeInTicks: int = 0
    timeInQuarterNotes: float = 0
    timeInSeconds: float = 0
    numerator: int = 4
    denominator: int = 4
#    clocksPerClick: int
#    thirtySecondPer24Clocks: int

    def copy(self):
        return MIDITimeSignatureEvent(self.timeInTicks, self.timeInQuarterNotes,
                              self.timeInSeconds,
                              self.numerator, self.denominator,
#                              self.clocksPerClick,
#                              self.thirtySecondPer24Clocks
                              )
