
import subprocess
import sys

class Bot():
    def __init__(self, language = "FR"):
        self.language = language

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

            #format temp in °C
            cpuTemp = float(out) / 1000.0

            return (str(cpuTemp) + " °C")
        
        else:
            return "Commande disponible uniquement sur linux ..."

