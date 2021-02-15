import matplotlib.pyplot as plt
import wfdb
import numpy as np

record = wfdb.rdsamp("100", pn_dir= "mitdb")[0] #b to n
r_peaks = wfdb.rdann("100", extension="atr", pn_dir= "mitdb").sample


class ECG:
    def __init__(self, record, r_peaks):
        self.record = record
        self.r_peaks = r_peaks
        len_peak = len(r_peaks)
        len_record = len(record)
        self.heartbeats = []

        for i in range(len_peak):

            if i == len_peak-1:
                post_rr = None
            else:
                post_rr = self.r_peaks[i+1] - self.r_peaks[i]

            if self.r_peaks[i] < 90:
                data = self.record[0: 2*self.r_peaks[i]]

            elif self.r_peaks[i] > len_record-90:
                data = self.record[2*self.r_peaks[i]-len_record:len_record]

            else:
                data = self.record[self.r_peaks[i]-90: self.r_peaks[i]+90]

            class Heartbeat:
                def __init__(self,):
                    self.post_rr = post_rr
                    self.data = data

            heartbeat = Heartbeat()
            self.heartbeats.append(heartbeat)

    def extract_beats(self):

            return self.heartbeats

ecg = ECG(record, r_peaks)
heartbeats = ecg.extract_beats()   # only return the valid heartbeats
for heartbeat in heartbeats[:3]:
    #assert len(heartbeat.data)==180
    plt.plot(heartbeat.data)
    #print(len(heartbeat.data))
    print("the post_rr of the heartbeat: {}".format(heartbeat.post_rr))

plt.show()







