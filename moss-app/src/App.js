<<<<<<< HEAD
// // state refers to data that changes over time based on user interactions 
// import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
// import './App.css';
// // import {HashRouter as Router, Routes, Route} from "react-router-dom"

// import LoginPage from "./components/Authentication";


// // import LoadingPage.js and assign it the name "LoadingPage"
// import LoadingPage from './pages/LoadingPage/LoadingPage.js'
// import LoginPage from './pages/LoginPage/LoginPage.js'
// // import MyGarden  from './pages/LoadingPage/MyGarden.js'
// // import PlantInfoPage from './pages/LoadingPage/PlantInfoPage.js'
// // import AiAnalysisGraph  from './pages/LoadingPage/AiAnalysisGraph.js'


import React from 'react';
import {SignedOut, SignedIn} from "@clerk/clerk-react";
import LoginPage from './pages/LoginPage/LoginPage';
import MyGarden from'./pages/MyGarden/MyGarden';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

function App() {

  
=======
import React from 'react';
import {SignedOut, SignedIn} from "@clerk/clerk-react";
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

// importing the pages 
import LoginPage from './pages/LoginPage/LoginPage';
import SignUpPage from './pages/SignUpPage/SignUpPage';
import MyGarden from './pages/MyGarden/MyGarden';

// importing the subpages
import Sunlight from './pages/MyGarden/SunLightPage/SunLight';
import SoilMoisture from './pages/MyGarden/SoilMoisturePage/SoilMoisture';
import Humidity from './pages/MyGarden/AtmoHumidityPage/AtmoHumidity';
import Temp from './pages/MyGarden/TempPage/Temp';


function App() {
>>>>>>> main
  return (

    <BrowserRouter>
      <Routes>

<<<<<<< HEAD
        {/*If the User is in Login Page */}  
        <Route path ="/" element={
          <>   
            <SignedOut><LoginPage/></SignedOut>
            <SignedIn><Navigate to="/mygarden" /></SignedIn>
          </>
        }/>

        { /*If the User is in MyGarden Page */}

        <Route path ="/garden" element={
          <>
=======

        {/* <Route path='/' element={<MyGarden/>} />
        <Route path="/garden" element={<MyGarden/>} />
        <Route path="/garden/sunlight" element={<Sunlight/>} />
        <Route path="/garden/soilMoisture" element={<SoilMoisture/>} />
        <Route path="/garden/humidity" element={<Humidity/>} />
        <Route path="/garden/temperature" element={<Temp/>} /> */}
 

        {/* *************** KEEP THIS, i commented it out, for testing purpose ******************
            *************** it bypass 'Login' it so i can go straight to myGarden ***************** */}

        {/* If the User is in Login Page */}
        <Route path ="/" element={
          <>   
            <SignedOut><LoginPage/></SignedOut>
            <SignedIn><Navigate to="/garden" /></SignedIn>
          </>
        }/> 

        {/* Sign up Page */}
        <Route path="https://singular-dove-5.accounts.dev/sign-up" element={<SignUpPage/>} />

        { /*If the User is in MyGarden Page */}

        { <Route path ="/garden" element={
          <>

>>>>>>> main
          <SignedIn><MyGarden/></SignedIn>
          <SignedOut><Navigate to="/" /></SignedOut>

          </>
          }
<<<<<<< HEAD
          />
=======
          
          /> } 

          {/* Garden subpages, They are all connected now with the Sign In*/}

          <Route path="/garden/sunlight" element={

            <>
              <SignedIn><Sunlight/></SignedIn>
              <SignedOut><Navigate to="/" /></SignedOut>

            </>

          }/>

          <Route path="/garden/soilMoisture" element={

            <>
              <SignedIn><SoilMoisture/></SignedIn>
              <SignedOut><Navigate to="/" /></SignedOut>

            </>

          }/>

          <Route path="/garden/humidity" element={

            <>
              <SignedIn><Humidity/></SignedIn>
              <SignedOut><Navigate to="/" /></SignedOut>

            </>

          }/>

          <Route path="/garden/temperature" element={

            <>
              <SignedIn><Temp/></SignedIn>
              <SignedOut><Navigate to="/" /></SignedOut>

            </>

          }/>


>>>>>>> main


      
        </Routes>
    </BrowserRouter>

   
  );
}


export default App;