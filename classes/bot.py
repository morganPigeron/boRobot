
import subprocess
import sys

class Bot():
    def __init__(self, language = "FR", talk = False):
        self.language = language
        self.talk = talk

    def getCpuTemp(self): #TODO add windows compatibility
        """
        IN : none
        OUT : str temp in °c
        """
        #check if we are on linux
        if sys.platform == "linux":
            #if yes get temp
            out = subprocess.Popen(
                ["cat","/sys/class/thermal/thermal_zone0/temp"],
                stdout = subprocess.PIPE,
                stderr = subprocess.STDOUT,
            )

            stdout,stderr = out.communicate()

            #format temp in °C
            cpuTemp = float(stdout) / 1000.0

            return ("Mon processeur est à " + str(cpuTemp) + " °C")
        
        else:
            return "Commande disponible uniquement sur linux ..."

    def ttsSwitch(self):
        self.talk = not self.talk

    async def send(self, ctx, message):
        await ctx.send(message, tts=self.talk )
