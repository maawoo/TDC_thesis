import os
import glob
import math

log_dir = "/home/marco/pypypy/ARDCube_data/log/sentinel2"
f_pattern = "*.log"

time_list = []
for file in glob.iglob(os.path.join(log_dir, f_pattern), recursive=False):
    with open(file, "rt") as f:
        f_content = f.read()
        ind_base = f_content.find("time:")
        ind_min = ind_base + 6
        ind_sec = ind_base + 14
        minutes = f_content[ind_min:ind_min+2]
        seconds = f_content[ind_sec:ind_sec+2]
        sec_total = int(minutes) * 60 + int(seconds)

        time_list.append(sec_total)

avg_time = (sum(i for i in time_list) / len(time_list)) / 60
print(f"Avg processing time per scene: {math.floor(avg_time)} minutes {round((avg_time - math.floor(avg_time)) * 60)} "
      f"seconds")
