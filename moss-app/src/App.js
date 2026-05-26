import logo from './loading_plant.svg';
import './App.css';

// // src/App.js
// import React, { useState } from 'react';
// import './App.css'; // Global styles loaded here

// // Import your page folders
// import LoginPage from './pages/LoginPage/LoginPage';
// import GardenPage from './pages/GardenPage/GardenPage';

// function App() {
//   const [currentPage, setCurrentPage] = useState('login');

//   return (
//     <div className="app-container">
//       {/* App.js controls the layout skeleton, Pages handle the inside content */}
//       <main className="app-main-content">
//         {currentPage === 'login' && <LoginPage onLogin={() => setCurrentPage('garden')} />}
//         {currentPage === 'garden' && <GardenPage />}
//       </main>
//     </div>
//   );
// }

// export default App;


function App() {
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
export default App;