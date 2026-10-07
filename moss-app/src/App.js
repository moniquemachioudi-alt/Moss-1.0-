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
  return (

    <BrowserRouter>
      <Routes>


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

          <SignedIn><MyGarden/></SignedIn>
          <SignedOut><Navigate to="/" /></SignedOut>

          </>
          }
          
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




      
        </Routes>
    </BrowserRouter>

   
  );
}


export default App;