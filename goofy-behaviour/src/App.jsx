// import SliderComponent from "./components/SliderComponent";
import PlayButton from "./components/PlayButton";
import BackgroundVid from "./components/BackgroundVid";
import CharacterInput from "./components/CharacterInput";
import ClassSwitcher from "./components/ClassSwitcher";
import "./App.css";


function App() {
  return (
    <div className="App">
      <div className="App-body center-style">
        <BackgroundVid />
        <ClassSwitcher />
        {/* <SliderComponent /> */}
        <CharacterInput/>
        <PlayButton className="bottom-center" />
      </div>
    </div>
  );
}

export default App;
