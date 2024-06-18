import burn 
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

design = burn.z1.picorv.picorv32.baseOverlay("picorv32.bit")

while True:
    buf = design.run(6)
    design.chain0.phaseBump.down()
    if (np.mean(burn.parse.Trace.CombinedTrace(buf).pos.pop) != 64.0):
        break

for bump in range(10):
    design.chain0.phaseBump.down()

base_sweep = np.zeros(2688)
for phi in tqdm(range(2688)):
    buf = design.run(8)
    base_sweep[phi] = np.mean(burn.parse.Trace.CombinedTrace(buf).pos.pop)
    design.bumper.phase_bump_target_sensor.down()

    
for phi in range(2688):
    design.bumper.phase_bump_target_sensor.up()

plt.plot(base_sweep)
plt.xlabel("Phi Offset")
plt.ylabel("Popcount")

args = np.array([], np.int32)
design.processor.launch(aes, args)

pico_sweep = np.zeros(2688)
for phi in tqdm(range(2688)):
    buf = design.run(8)
    pico_sweep[phi] = np.mean(burn.parse.Trace.CombinedTrace(buf).pos.pop)
    design.bumper.phase_bump_target_sensor.down()

plt.plot(pico_sweep)
plt.xlabel("Phi Offset")
plt.ylabel("Popcount")

plt.plot(pico_sweep - base_sweep)
plt.xlabel("Phi Offset")
plt.ylabel("Popcount")