from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse,FileResponse
import time
from . import processing
import os
import numpy as np
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from threading import Thread
import base64
import cv2
import os
import shutil
import tempfile



global DONE
DONE=False
def home(request):
    request.session.flush()
    return render(request,'home.html')


@csrf_exempt
def save_images(request):     
    if request.method == 'POST':
        print("inside postt")
        data = json.loads(request.body)
        image_data = data.get('image')
        
        original_path = data.get('path') 
        relative_path = original_path.replace('/media/', '')
        relative_path = relative_path.replace("/","\\").replace("\\","\\\\")
        full_path = os.path.join(settings.MEDIA_ROOT, relative_path).split('?')[0]
        header, encoded = image_data.split(';base64,')
        img_bytes = base64.b64decode(encoded)
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) 
        print(full_path)
        # cv2.imshow('window',img)
        cv2.imwrite(full_path,img)
        cv2.waitKey(0)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "fail", "error": "Not POST"}, status=400)
def process(request):
   try: 
    global DONE
    file=request.session['filename']
    def video_process(file):
        global DONE
        input_video = os.path.join(settings.MEDIA_ROOT, file.split('.')[0], file)
        output_path = os.path.join(settings.MEDIA_ROOT, file.split('.')[0])
        ts=processing.timestamp(input_video)
        print(ts)
        processing.best_frame(ts,input_video,output_path)
        DONE=True
        return
    DONE=False
    thread=Thread(target=video_process, args=(file,))
    thread.start()
    return render(request,'process.html',{'file':file})
   except(KeyError):
       return redirect('home')

def check_status(request):
    global DONE
    return JsonResponse({'done': DONE})
def editor(request):
    file=request.session['filename'].split(".")[0]
    # print(file)
    images_p=show_images(file)
    if images_p:
        return render(request,'editor.html',{"images":zip(images_p['images'],images_p['file_names'])})
    return render(request,'editor.html')

def upload(request):
    if request.method=='POST' and  request.FILES.get('video'):
        print('hello')
        video=request.FILES.get('video')
        file=video.name
        print(file)
        fs = FileSystemStorage(location='media/'+file.split('.')[0])  
        filename = fs.save(video.name, video)         
        request.session['filename']=file
        return redirect('process')
    return redirect('home')

def delete_image(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        path = data.get('path')
        relative_path = path.replace('/media/', '')
        relative_path = relative_path.replace("/","\\").replace("\\","\\\\")
        full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
        print(full_path)
        os.remove(full_path)
        return JsonResponse({"status":"success"})
    return JsonResponse({"Error":"Only post methhod please"})
    
def zip_directory(request):
    dir_name=request.session['filename'].split(".")[0]
    # dir_name= "video2"
    print(dir_name)
    folder_path = os.path.join(settings.MEDIA_ROOT, dir_name)
    temp_dir = tempfile.mkdtemp()
    zip_base = os.path.join(temp_dir, dir_name)
    zip_file = shutil.make_archive(zip_base, 'zip', folder_path)
    return FileResponse(open(zip_file, 'rb'), as_attachment=True, filename=f"{dir_name}.zip")


def show_images(url):
    # url= 'video5/'
    image_folder = os.path.join(settings.MEDIA_ROOT, url)
    image_files = []
    file_names = []
    files = os.listdir(image_folder)
    full_paths = [os.path.join(image_folder, file) for file in files if file.endswith(".jpg")]
    sorted_files = sorted(full_paths, key=os.path.getctime)
    for f in sorted_files:
        if f.endswith(".jpg"):
            timestamp = int(os.path.getmtime(f))
            src="/media"+(f.split("\media")[-1]).replace("\\", "/")+ f"?v={timestamp}"
            image_files.append(src)
            file_names.append(os.path.basename(f))
    return {'images': image_files, 'file_names': file_names}

def resize_image():
    pass