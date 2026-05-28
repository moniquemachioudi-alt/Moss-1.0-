import React, { useState } from 'react';

// need to acess parent-parent folder, then enter images folder
import logo from '../../images/loading_plant.svg'
import './LoadingPage.css'

// import LoadingPage from './pages/LoadingPage/LoadingPage.js'



// .center-container {
//   display: flex; 
//   justify-content: center; 
//   align-items: center;
//   min-height: 30vh;
//   width: 100vw;
//   margin: 0;
//   box-sizing: border-box;
// }

function LoadingPage() {
  
  return (
    <div className="App">

      <div className="App-header">

        <h1> Welcome to Moss </h1>
          <div className="center-container">

            <img src={logo} className="App-logo" alt="logo" />

          </div>
      </div>



    </div>

  );
}

export default LoadingPage;