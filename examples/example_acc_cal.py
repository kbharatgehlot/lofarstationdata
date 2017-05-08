#!/usr/bin/env python

from lofarstation.stationdata import ACCData
from casacore.measures import measures

sd = ACCData("20161231_133057_acc_512x192x192.dat",
             station_name="SE607", rcu_mode=3)
sd.set_station_cal("CalTable-SE607-mode3-2015.10.07.dat")
sd.write_ms("acc1-full.ms")

# If station name is not specified you need to supply an antfile
sd = ACCData("20161231_133057_acc_512x192x192.dat",
             antfile="SE607-AntennaField.conf", rcu_mode=3,
             subband=128)
sd.set_station_cal("CalTable-SE607-mode3-2015.10.07.dat")
sd.write_ms("acc1-s128-cal.ms")

sd = ACCData("20161231_133057_acc_512x192x192.dat",
             station_name="SE607", rcu_mode=3, subband=384)
sd.set_station_cal("CalTable-SE607-mode3-2015.10.07.dat")
sd.write_ms("acc1-s386-cal.ms")
