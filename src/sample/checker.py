from sample.player import Player

class Checker:
    def __init__(self):
        self.temp = Player()

    def remainder(self, file):
        time = self.temp.getTime()
        if time > 17:
            self.temp.playWavFile(file)
            return self.temp.wavWasPlayed(file)
        else:
            return self.temp.resetWav(file)

