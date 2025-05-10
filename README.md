
# Wedding Photo Extractor

## Description
Wedding Photo Extractor is a web application that allows users to upload MP4 video files. The application uses AI to extract beautiful photos from the video and provides tools for the user to edit the photos. After editing, the user can download a zip file containing the photos. This project leverages the power of artificial intelligence for automatic photo selection and offers an intuitive interface for easy editing.

## Features
- **AI-based Photo Extraction**: Extracts beautiful frames from wedding videos (MP4 format).
- **Photo Editing**: Allows the user to make basic edits on extracted photos.
- **Downloadable Zip**: After editing, the user can download a zip file containing the edited photos.
- **Media Handling**: Automatically manages media files for the photos and edited versions.

## Installation

Follow these steps to set up the project locally.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/wedding-photo-extractor.git
cd wedding-photo-extractor
```

### 2. Set up the virtual environment

Make sure you have Python 3.8+ installed. Then create and activate the virtual environment.

#### On Windows:
```bash
python -m venv venv
.env\Scriptsctivate
```

#### On Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```


### 4. Create the media folder 
Make sure to create an empty `media/` folder in the root directory:
```bash
mkdir media
```

### 5. Apply migrations
If you have a database, apply the migrations:
```bash
python manage.py migrate
```

### 6. Run the server
Finally, start the Django development server:
```bash
python manage.py runserver
```

Your application will be accessible at `http://127.0.0.1:8000/`.

## Usage
1. **Upload an MP4 video**: The user can upload a wedding video in MP4 format.
2. **Photo Extraction**: The AI extracts beautiful frames from the video and displays them in the UI.
3. **Edit Photos**: Users can edit the extracted photos using the built-in editing tools (resize, crop, etc.).
4. **Download Zip**: After editing, the user can download a zip file containing the edited images.

## Project Structure
```
wedding-photo-extractor/
│
├── wedding_photo_extractor/       # Django app directory
│   ├── static/                    # Static files (CSS, JavaScript, etc.)
│   ├── templates/                 # HTML templates
│   └── media/                     # Folder for uploaded media files (empty initially)
├── manage.py                      # Django manage script
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore file
├── README.md                      # This file
└── .env                           # Environment variables file (example)
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
