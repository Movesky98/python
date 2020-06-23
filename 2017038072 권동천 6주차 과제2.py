import threading
import time

class calculator :
    cal = 0

    def calculation(self, maxnumber, i) :
        for self.i  in range(1, maxnumber+1, 1) :
            self.cal += self.i
        print("\n1+2+3+ . . . +%d = " % maxnumber)
        print(self.cal, end='')
        time.sleep(0.1)

cal1 = calculator()
cal2 = calculator()
cal3 = calculator()
i = 0


cal1 = threading.Thread(target = cal1.calculation(1000, i))
cal2 = threading.Thread(target = cal2.calculation(100000, i))
cal3 = threading.Thread(target = cal3.calculation(10000000, i))
