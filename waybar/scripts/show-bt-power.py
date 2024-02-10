#! /usr/bin/env python
import re 
import json 
import subprocess
from collections import OrderedDict

data = {}

device = str(subprocess.getstatusoutput(f'upower -d | grep model'))
percent = str(subprocess.getstatusoutput(f'upower -d | grep percentage'))

# split by device
dev = device.split("model:")
dev.pop(0)  # remove empty space

# split by percent
perc = percent.split("percentage:")
perc.pop(0)

keep = OrderedDict((device, dev.index(device)) for device in dev)
keepIdx = list(keep.values())

# define kept device models and battery percentage
model, battery = [], []
for idx in keepIdx:
    model.append(dev[idx])
    battery.append(perc[idx])

# clean str with regex
patterns = ["'", "\)","\\","", " "] 
model = re.sub("|".join(patterns),"",str(model[0]))
patterns = "['', ' ', '\\', 'n']"
battery = re.sub(patterns, '', str(battery[0]))
battery = re.sub(r"\\",'',battery) # for some reason only the first / is being removed

data['tooltip'] = f"model: {model}\n"
data['tooltip'] +=f"battery: {battery}"

print(json.dumps(data))

