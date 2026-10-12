<<<<<<< HEAD
import { useClerk, UserButton, useUser } from "@clerk/clerk-react";
=======
import { SignOutButton, useClerk, useUser } from "@clerk/clerk-react";
import { useState } from "react";
import { Link } from "react-router-dom";
>>>>>>> main



const Navbar = () => {
<<<<<<< HEAD
    return (  
        <nav className ="navbar">
            <h1>Moss</h1>
            <div className="links">
                <a href="/">MyGarden</a>
                <a href="/create"> New Device</a>
                <a href="/modify">New Plant</a>
                <a href="/remove">Remove Device</a>
                {
                    !user ? (<button onClick={openSignIn} className="Login">
                        Login
                        </button>
                    ) : (
                        <UserButton></UserButton>
                    )
                }
            </div>
        </nav>
    );
}
 
const {user} = useUser();
const {openSignIn} = useClerk();
=======
    
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





>>>>>>> main
export default Navbar;