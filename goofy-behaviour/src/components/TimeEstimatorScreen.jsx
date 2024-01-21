import { useState, useEffect } from 'react';
import './TimeEstimatorScreen.css';

const TimeEstimatorScreen = () => {
    const [estimatedTime, setEstimatedTime] = useState('Calculating...');

    useEffect(() => {
        // Simulate fetching estimated time (e.g., from an API)
        const timer = setTimeout(() => {
            setEstimatedTime('~2 minutes');
        }, 2000);

        return () => clearTimeout(timer);
    }, []);

    return (
        <div className="time-estimator">
            <div className="finding-game">Finding Game</div>
            <div className="estimated-time">{estimatedTime}</div>
            <div className="loader"></div>
        </div>
    );
};

export default TimeEstimatorScreen;
