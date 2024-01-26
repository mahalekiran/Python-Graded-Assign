# Python script to monitor CPU usage
import psutil

try:
    while True:
        cpu=int(psutil.cpu_percent(5))
        if cpu > 80:
            print ("Alert! CPU usage exceeds threshold: "+ str(cpu) +" %")
        else:
            print("Monitoring CPU usage... "+ str(cpu) +" %")
except Exception as error:
    print("Some error occurred: "+ str(error))
except KeyboardInterrupt as key:
    print("Keyboard Interrupt: "+str(key))
finally:
    cpu=0