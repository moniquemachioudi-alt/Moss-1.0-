import logo from './loading_plant.svg';
import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="Loading">
        
//         <img src={logo} className="App-logo" alt="logo" />

//         <p>
          
//           Loading...
          
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
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