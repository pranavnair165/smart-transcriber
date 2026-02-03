function VideoUpload() {
  return (
    <div>
      <h2>Video to Text</h2>
      <input type="file" accept="video/*" />
      <button>Upload Video</button>
      <p>Transcript will appear here.</p>
    </div>
  );
}

export default VideoUpload;
