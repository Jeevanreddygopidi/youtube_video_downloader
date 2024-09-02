# YouTube Video Downloader

This project is a web application built using FastAPI that allows users to download YouTube videos. Users can input a YouTube video URL, preview the video’s thumbnail and title, select the desired quality, and download the video in MP4 format.

## Features

- Download videos from YouTube.
- Preview video thumbnail and title.
- Select video quality from available options (144p, 240p, 360p, 480p, 720p, 1080p).
- Default download quality is set to 480p.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Jeevanreddygopidi/youtube_video_downloader.git
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

The application will be accessible at `http://127.0.0.1:8000`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000`.
2. Enter the YouTube video URL in the input field and click "Get Video".
3. Preview the video’s thumbnail and title.
4. Select the desired video quality from the dropdown menu.
5. Click "Download" to start downloading the video.

## Dependencies

- `FastAPI`: For building the web application.
- `yt-dlp`: For downloading YouTube videos.
- `uvicorn`: ASGI server for running FastAPI.
- `ffmpeg`: For video processing (if required).

Check `requirements.txt` for the complete list of dependencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## Contact

For any questions or suggestions, please contact [jeevanreddy.work@gmail.com](mailto:jeevanreddy.work@gmail.com).

