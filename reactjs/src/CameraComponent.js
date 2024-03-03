import React, { useRef, useEffect, useState } from 'react';
import './CameraComponent.css'; // Import CSS file for styling

const CameraComponent = () => {
  const videoRef = useRef(null);
  const [capturedImage, setCapturedImage] = useState(null);

  useEffect(() => {
    // Access the user's camera
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
          if (videoRef.current) {
            videoRef.current.srcObject = stream;
          }
        })
        .catch(error => {
          console.error('Error accessing camera:', error);
        });
    } else {
      console.error('getUserMedia is not supported');
    }
  }, []);
  
  const takePicture = () => {
    const canvas = document.createElement('canvas');
    canvas.width = videoRef.current.videoWidth;
    canvas.height = videoRef.current.videoHeight;
    canvas.getContext('2d').drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
    const imageDataUrl = canvas.toDataURL('image/png');
    setCapturedImage(imageDataUrl);
  };

  return (
    <div className="camera-container">

      <video ref={videoRef} autoPlay={true} className="camera-video" />
      <button onClick={takePicture} className="test">Take Picture</button> {/* Button to take picture */}
      {capturedImage && (
        <div>
          <h3>Preview:</h3>
          <img src={capturedImage} alt="Captured" />
        </div>
      )}
    </div>
  );
};

export default CameraComponent;