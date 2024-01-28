import React, { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'

const Navbar = () => {
    const [nav, setNav] = useState(false)
    const location = useLocation()

    return (
        <div className="flex items-center justify-between p-4 bg-transparent">
            {/* Logo */}
            <Link to="/" className="font-bold text-black">DZ<span className='font-normal'> Mouhami</span></Link>
            {/* Sign in button */}
            {location.pathname !== '/signin' && <Link to="/signin">
                <button className='bg-black font-semibold px-10 py-2 text-white hover:bg-[#800020] hover:outline-none'>Sign in</button></Link>
            }
        </div>
    );
}

export default Navbar;