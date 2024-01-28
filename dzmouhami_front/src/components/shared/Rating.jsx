import { useState, useEffect } from "react";
import Button from "./Button";
import RatingSelect from "../RatingSelect";
import { useContext } from 'react'
import ContextProvider from "../../context/ContextProvider";
import { FaCircleCheck } from "react-icons/fa6";



const Rating = () => {
    const { addFeedback, feedbackEdit, updateFeedback, deleteFeedback } = useContext(ContextProvider)

    const [text, setText] = useState('')
    const [btnDisabled, setBtnDisbaled] = useState(true)
    const [message, setMessage] = useState('')
    const [rating, setRating] = useState(5)
    const [name, setName] = useState('')
    const [formSubmitted, setFormSubmitted] = useState(false)

    const handleTextChange = (e) => {
        if (text === '') {
            setBtnDisbaled(true)
            setMessage(null)
        }
        else if (text !== '' && text.trim().length < 10) {
            setMessage('Feedback text must be at least 10 characters long')
            setBtnDisbaled(true)
        } else {
            setBtnDisbaled(false)
            setMessage(null)
        }
        setText(e.target.value)
    }

    const handleNameChange = (e) => {
        if (name === '') {
            setBtnDisbaled(true)
            setMessage(null)
        }
        else if (name !== '' && name.trim().length < 5) {
            setMessage('Please provide a name')
            setBtnDisbaled(true)
        } else {
            setBtnDisbaled(false)
            setMessage(null)
        }
        setName(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        if (text.trim().length > 10 && name.trim().length > 5 && rating === 5) {
            const newFeedback = {
                id: Math.floor(Math.random() * 10000) + 1,
                name: name,
                text: text,
                rating: rating
            }
            addFeedback(newFeedback)
            setText('')
            setFormSubmitted(true)
        }
        else if (text.trim().length > 10 && name.trim().length > 5 && rating !== 5) {
            const newFeedback = {
                id: Math.floor(Math.random() * 10000) + 1,
                name: name,
                text: text,
                rating: rating
            }
            setText('')
            setFormSubmitted(true)
        }
    }

    return (
        <>
            {!formSubmitted && <form onSubmit={handleSubmit} className="flex flex-col justify-center gap-4 place-items-center p-4">
                <div className='flex justify-center'>
                    <h1 className='text-2xl font-black text-[#800020] z-50 my-4'>Tell us what you think</h1>
                </div>
                <h2>How would you rate your service with us?</h2>
                <input onChange={handleNameChange} value={name} type="text" placeholder="Your name"
                    className="border-red-800 border-2 focus:outline-none p-2
                    rounded-md
                    " />
                <RatingSelect select={(rating) => setRating(rating)} />
                <input onChange={handleTextChange} value={text} type="text" placeholder="Write a review"
                    className="border-red-800 border-2 focus:outline-none p-8 
                    rounded-md
                    " />
                {message && <div className="text-sm text-red-800">{message}</div>}
                <Button type="submit" isDisabled={btnDisabled}>Send</Button>
            </form>}

            {
                formSubmitted && <div className="flex flex-col justify-center gap-4 place-items-center p-4">
                    <h2 className="text-3xl mt-8">Thank you for your feedback!</h2>
                    <FaCircleCheck size={40} />
                </div>
            }
        </>

    );
}

export default Rating;