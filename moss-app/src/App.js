
import React from 'react';
import { SignedOut, SignedIn } from '@clerk/clerk-react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

// Main pages
import LoginPage from './pages/LoginPage/LoginPage';
import SignUpPage from './pages/SignUpPage/SignUpPage';
import MyGarden from './pages/MyGarden/MyGarden';

// Garden subpages
import Sunlight from './pages/MyGarden/SunLightPage/SunLight';
import SoilMoisture from './pages/MyGarden/SoilMoisturePage/SoilMoisture';
import Humidity from './pages/MyGarden/AtmoHumidityPage/AtmoHumidity';
import Temp from './pages/MyGarden/TempPage/Temp';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Login page */}
        <Route
          path="/"
          element={
            <>
              <SignedOut>
                <LoginPage />
              </SignedOut>
              <SignedIn>
                <Navigate to="/garden" replace />
              </SignedIn>
            </>
          }
        />

        {/* Sign-up page */}
        <Route
          path="/sign-up"
          element={
            <>
              <SignedOut>
                <SignUpPage />
              </SignedOut>
              <SignedIn>
                <Navigate to="/garden" replace />
              </SignedIn>
            </>
          }
        />

        {/* Main garden page */}
        <Route
          path="/garden"
          element={
            <>
              <SignedIn>
                <MyGarden />
              </SignedIn>
              <SignedOut>
                <Navigate to="/" replace />
              </SignedOut>
            </>
          }
        />

        {/* Garden subpages */}
        <Route
          path="/garden/sunlight"
          element={
            <SignedIn>
              <Sunlight />
            </SignedIn>
          }
        />

        <Route
          path="/garden/soilMoisture"
          element={
            <SignedIn>
              <SoilMoisture />
            </SignedIn>
          }
        />

        <Route
          path="/garden/humidity"
          element={
            <SignedIn>
              <Humidity />
            </SignedIn>
          }
        />

        <Route
          path="/garden/temperature"
          element={
            <SignedIn>
              <Temp />
            </SignedIn>
          }
        />

        {/* Unknown routes return to login */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
