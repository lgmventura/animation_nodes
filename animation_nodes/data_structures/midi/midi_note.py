from dataclasses import dataclass

def evaluateEnvelope(time, timeOn, timeOff, attackTime, attackInterpolation, decayTime, decayInterpolation, sustainLevel):
    # find either point in time for envelope or where in envelope the timeOff happened
    relativeTime = min(time, timeOff) - timeOn

    if relativeTime <= 0.0:
        return 0.0

    if relativeTime < attackTime:
        return attackInterpolation(relativeTime / attackTime)

    relativeTime = relativeTime - attackTime

    if relativeTime < decayTime:
        decayNormalized = decayInterpolation(1 - relativeTime/ decayTime)
        return decayNormalized * (1 - sustainLevel) + sustainLevel

    return sustainLevel

@dataclass
class MIDINote:
    channel: int = 0
    noteNumber: int = 0
    timeOn_s: float = 0
    timeOff_s: float = 0
    timeOn_qn: float = 0
    timeOff_qn: float = 0
    velocity: float = 0

    def evaluate(self, time, attackTime, attackInterpolation, decayTime, decayInterpolation, sustainLevel, 
        releaseTime, releaseInterpolation, velocitySensitivity):

        value = evaluateEnvelope(time, self.timeOn_s, self.timeOff_s, attackTime, attackInterpolation, decayTime, decayInterpolation, sustainLevel)

        if time > self.timeOff_s:
            value = value * releaseInterpolation(1 - ((time - self.timeOff_s) / releaseTime))

        # if velocity sensitivity is 25%, then take 75% of envelope and 25% of envelope with velocity
        return (1 - velocitySensitivity) * value + velocitySensitivity * self.velocity * value

    def copy(self):
        return MIDINote(self.channel, self.noteNumber, self.timeOn_s, self.timeOff_s,
                        self.timeOn_qn, self.timeOff_qn, self.velocity)
