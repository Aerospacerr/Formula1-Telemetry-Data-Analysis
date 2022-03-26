import matplotlib.pyplot as plt
import fastf1.plotting
import fastf1
import numpy as np
import pandas as pd

#fastf1.Cache.enable_cache('C:/Users/husey/Desktop/Case-Task/Formula1/cache/')  # replace with your cache directory

# enable some matplotlib patches for plotting timedelta values and load
# FastF1's default color scheme
fastf1.plotting.setup_mpl()

# load a session and its telemetry data
session = fastf1.get_session(2022, 2, 'Q')
session.load()

per_lap = session.laps.pick_driver('PER').pick_fastest()
lec_lap = session.laps.pick_driver('LEC').pick_fastest()

per_tel = per_lap.get_car_data().add_distance()
lec_tel = lec_lap.get_car_data().add_distance()

rbr_color = fastf1.plotting.team_color('RBR')
fer_color = fastf1.plotting.team_color('FER')

fig, ax = plt.subplots()
ax.plot(per_tel['Time'], per_tel['Speed'], color=rbr_color, label='PER')
ax.plot(lec_tel['Time'], lec_tel['Speed'], color=fer_color, label='LEC')

ax.set_xlabel('Time in sec')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Fastest Lap Comparison \n "
             f"{session.event['EventName']} {session.event.year} Qualifying")




fig, ax = plt.subplots()
ax.plot(per_lap.get_telemetry().Time, per_lap.get_telemetry().Brake, color=rbr_color, label='PER')
ax.plot(lec_lap.get_telemetry().Time, lec_lap.get_telemetry().Brake, color=fer_color, label='LEC')


fig, ax = plt.subplots()
ax.plot(per_lap.get_telemetry().Time, per_lap.get_telemetry().Throttle, color=rbr_color, label='PER')
ax.plot(lec_lap.get_telemetry().Time, lec_lap.get_telemetry().Throttle, color=fer_color, label='LEC')




#################
fig, ax = plt.subplots()
ax.plot(per_lap.get_telemetry().Time, per_lap.get_telemetry().nGear, color=rbr_color, label='PER')
ax.plot(lec_lap.get_telemetry().Time, lec_lap.get_telemetry().nGear, color=fer_color, label='LEC')

ax.legend()
plt.suptitle(f"Gear Shift Comparison \n "
             f"{session.event['EventName']} {session.event.year} Qualifying")



##########-------------############
####### HAM VS RUS ######

ham_lap = session.laps.pick_driver('HAM').pick_fastest()
rus_lap = session.laps.pick_driver('RUS').pick_fastest()

ham_tel = ham_lap.get_car_data().add_distance()
rus_tel = rus_lap.get_car_data().add_distance()

mer_color = fastf1.plotting.team_color('MER')
has_color = fastf1.plotting.team_color('HAS')

fig, ax = plt.subplots()
ax.plot(ham_tel['Time'], ham_tel['Speed'], color=mer_color, label='HAM')
ax.plot(rus_tel['Time'], rus_tel['Speed'], color=has_color, label='RUS')

ax.set_xlabel('Time in sec')
ax.set_ylabel('Speed in km/h')

ax.legend()
plt.suptitle(f"Fastest Lap Comparison \n "
             f"{session.event['EventName']} {session.event.year} Qualifying")



### throttle ###
fig, ax = plt.subplots()
ax.plot(ham_lap.get_telemetry().Time, ham_lap.get_telemetry().Throttle, color=mer_color, label='HAM')
ax.plot(rus_lap.get_telemetry().Time, rus_lap.get_telemetry().Throttle, color=has_color, label='RUS')

ax.set_xlabel('Time in sec')
ax.set_ylabel('Throttle %')

ax.legend()
plt.suptitle(f"Fastest Lap Throttle Comparison \n "
             f"{session.event['EventName']} {session.event.year} Qualifying")
plt.show()

##########-------------############





#############
laps.columns=[['Driver','LapTime']]
for i in range(326):
    if session.laps['IsAccurate'][i]==True:
        laps[i:i+1]=session.laps[['Driver','LapTime']][i:i+1]