import AudioRecorder from "./components/AudioRecorder";
import VideoUpload from "./components/VideoUpload";
import ArticleInput from "./components/ArticleInput";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>SMART TRANSCRIBER</h1>

      <AudioRecorder />
      <hr />
      <VideoUpload />
      <hr />
      <ArticleInput />
    </div>
  );
}

export default App;
