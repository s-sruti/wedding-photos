
import subprocess
import os


def timestamp(input_video):
    if not os.path.exists(input_video):
        print("❌ File not found:", input_video)
    command = [
    "ffmpeg", "-i", input_video,
    "-vf", "select='gt(scene,0.1)',metadata=print",
    "-vsync", "vfr", "-f", "null", "-"
]


    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8")
    times=[]
    prev=0
    for line in process.stdout:
        
        if "pts_time" in line:  
            timestamp = line.split("pts_time:")[-1].strip()
            times.append((prev,float(timestamp)))
            prev=float(timestamp)
    return times

   
def best_frame(scenes,video_file,output_path):
    c=0
    for i in scenes:
        c+=1
        val=i[1]-i[0]
        hrs = int(i[0] // 3600)
        mins = int((i[0] % 3600) // 60)
        secs = i[0] % 60

        start_time=f"{hrs:02}:{mins:02}:{secs:06.3f}"
        hrs = int(val // 3600)
        mins = int((val % 3600) // 60)
        secs = val % 60

        duration=f"{hrs:02}:{mins:02}:{secs:06.3f}"
        
        output_file=os.path.join(output_path,f'scene{c}.jpg')
        
        command = [
                "ffmpeg",
                "-ss", start_time,
                "-t", duration,
                "-i", video_file,
                "-vf", "thumbnail,unsharp=5:5:1.0",
                "-frames:v", "1",
                output_file,
                "-y"  
            ]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


