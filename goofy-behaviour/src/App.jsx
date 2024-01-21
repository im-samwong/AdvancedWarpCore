import SliderComponent from "./components/SliderComponent";
import PlayButton from "./components/PlayButton";
import BackgroundVid from "./components/BackgroundVid";
import "./App.css";
import CharacterInput from "./components/CharacterInput";

function App() {
  return (
    <div className="App">
      <div className="App-body center-style">
        <BackgroundVid />
        <CharacterInput/>
        <SliderComponent />
        <PlayButton className="bottom-center" />
      </div>
    </div>
  );
}

export default App;
