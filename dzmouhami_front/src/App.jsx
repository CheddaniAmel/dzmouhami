import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import HomePage from './components/HomePage'
import Navbar from './components/Navbar'
import Footer from './components/shared/Footer'
import SignIn from './components/pages/SignIn'
import ResetPassword from './components/pages/ResetPassword'
import Lawyers from './components/pages/Lawyers'
import { ContextProvider } from './context/ContextProvider'

function App() {

  return (
    <ContextProvider>
      <Router>
        <div className="">
          <Navbar />
          <div className='flex flex-col bg-[FAF6F6]'>
            <Routes>
              <Route path="/" element={<>
                <HomePage />
              </>} />
              <Route path="/lawyers" element={<>
                <Lawyers />
              </>} />
              <Route path="/signin" element={<>
                <SignIn />
              </>} />
              <Route path="/resetpassword" element={
                <ResetPassword />
              }></Route>
            </Routes>
            <Footer />
          </div>
        </div>
      </Router>
    </ContextProvider>
  )
}

export default App;

