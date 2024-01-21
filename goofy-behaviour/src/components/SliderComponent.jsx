import { useState } from 'react';
import axios from 'axios';

const SliderComponent = () => {
    const [value, setValue] = useState(0);
    const [result, setResult] = useState(null);

    const handleSliderChange = (e) => {
        setValue(e.target.value);
    };

    const handleSliderRelease = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/add', { number: parseInt(value) });
            setResult(response.data.result);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div>
            <input 
                type="range" 
                min="0" 
                max="100" 
                value={value} 
                onChange={handleSliderChange} 
                onMouseUp={handleSliderRelease}
            />
            <p>Value: {value}</p>
            {result !== null && <p>Result from backend: {result}</p>}
        </div>
    );
};

export default SliderComponent;
