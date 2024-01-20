import SliderComponent from './components/SliderComponent';
import TimeEstimatorScreen from './components/TimeEstimatorScreen';
import './App.css'; // Import your CSS file (if it's separate)
//
function App() {
  return (
    <div className="App">
      <SliderComponent />
      <div className='center-style'>
        <TimeEstimatorScreen />
      </div>
    </div>
  );
}

export default App;
