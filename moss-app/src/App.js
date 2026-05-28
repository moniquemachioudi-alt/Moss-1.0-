// state refers to data that changes over time based on user interactions 
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import './App.css';
// import {HashRouter as Router, Routes, Route} from "react-router-dom"


// import LoadingPage.js and assign it the name "LoadingPage"
import LoadingPage from './pages/LoadingPage/LoadingPage.js'
import LoginPage from './pages/LoginPage/LoginPage.js'
// import MyGarden  from './pages/LoadingPage/MyGarden.js'
// import PlantInfoPage from './pages/LoadingPage/PlantInfoPage.js'
// import AiAnalysisGraph  from './pages/LoadingPage/AiAnalysisGraph.js'



function App() {
  return (

    <BrowserRouter>

    {/* this will make like header links, uncomment to see what i mean  */}
      <nav>
        {/* <Link to ="/">LoadingPage</Link> | {" "}
        <Link to ="/">LoginPage</Link> | {" "} */}
      </nav>


      <Routes>
        <Route path="/" element={<LoadingPage />} />
        {/* <Route path="/about" element={<LoginPage />} /> */}

      </Routes>

    </BrowserRouter>



  );
}


export default App