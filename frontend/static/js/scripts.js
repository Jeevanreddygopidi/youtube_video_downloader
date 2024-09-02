document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const videoUrl = document.getElementById('videoUrl').value;
    const statusMessage = document.getElementById('statusMessage');
    statusMessage.textContent = "Downloading...";

    fetch(`/download/?video_url=${encodeURIComponent(videoUrl)}`)
        .then(response => response.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'video.mp4';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            statusMessage.textContent = "Download Complete!";
        })
        .catch(() => {
            statusMessage.textContent = "Failed to download video.";
        });
});
