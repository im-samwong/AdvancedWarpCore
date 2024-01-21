import SliderComponent from './components/SliderComponent';
import TestComponent from './components/TestComponent';
import TimeEstimatorScreen from './components/TimeEstimatorScreen';
import BackgroundVid from './components/BackgroundVid';
import './App.css'; // Import your CSS file (if it's separate)
//
function App() {
  return (
    <div className="App">
      <BackgroundVid />
      <SliderComponent />
      
      <div className='center-style'>
        <TimeEstimatorScreen />
      </div>
      <TestComponent />

    </div>
  );
}

export default App;
