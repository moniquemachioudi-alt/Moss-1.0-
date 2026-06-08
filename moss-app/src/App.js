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

  
  return (

    <BrowserRouter>
      <Routes>

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
          <SignedIn><MyGarden/></SignedIn>
          <SignedOut><Navigate to="/" /></SignedOut>

          </>
          }
          />


      
        </Routes>
    </BrowserRouter>

   
  );
}


export default App;