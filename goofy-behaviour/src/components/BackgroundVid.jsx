import video from '../assets/loopbg.mp4';

const BackgroundVid = () => {
    return (
        <div className='0'>
            <video src={video} autoPlay loop muted className="video-container" />
        </div>
    )
}

export default BackgroundVid