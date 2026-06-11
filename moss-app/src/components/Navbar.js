import { SignOutButton, useClerk, useUser } from "@clerk/clerk-react";
import { useState } from "react";
import { Link } from "react-router-dom";



const Navbar = () => {
    
    const {user} = useUser();
    const {openSignIn} = useClerk();
    const [isOpen, setIsOpen] = useState(false);
    
    
    
    
    return (  
        <nav className ="navbar">
            {/* <h1>Moss</h1> */}

            <button onClick={() => setIsOpen(!isOpen)}> Menu </button>

           {isOpen && <div> 
                
                <Link to="/garden">MyGarden</Link> <br/>
                <Link to="/garden/create">NewPlant</Link> <br/>
                <Link to="/garden/modify">ModifyPlant</Link> <br/>
                <Link to="/garden/remove">RemovePlant</Link> <br/>
                
                <div style={{color:"red"}}> <SignOutButton/> </div>
                
                </div>
            }

        </nav>
    );
}





export default Navbar;