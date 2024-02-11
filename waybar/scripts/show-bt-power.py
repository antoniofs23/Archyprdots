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
for idx in keepIdx:
    
    # clean str with regex
    patterns = ["'", "\)","\\","",'n', " "] 
    temp = re.sub("|".join(patterns),"",str(dev[idx]))
    model = re.sub(r"\\",'',temp)

    patterns = "['', ' ', '\\', 'n']"
    temp = re.sub(patterns, '', str(perc[idx]))
    battery = re.sub(r"\\",'',temp) 
    
    # concat the model + battery
    if data == {}:
        data['tooltip'] = f"\n{model}': '{battery}\n"
    else:
        data['tooltip'] +=f"{model}': '{battery}\n"


print(json.dumps(data))

