// import SliderComponent from "./components/SliderComponent";
import useStore from "./store"; // Update the path as needed
import PlayButton from "./components/PlayButton";
import BackgroundVid from "./components/BackgroundVid";
import CharacterInput from "./components/CharacterInput";
import ClassSwitcher from "./components/ClassSwitcher";
import bloodstain from './assets/bloodstain.png';
import "./App.css";


function App() {
  const { displayStain } = useStore();
  return (
    <div className="App">
      <div className="App-body center-style ">
        <BackgroundVid />
        <ClassSwitcher />
        <CharacterInput />
        <PlayButton className="bottom-center" />
      </div>
      <img src={bloodstain} className={`bloodstain ${displayStain ? 'display' : ''}`} />

    </div>
  );
}

export default App;
