import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Pagination, Scrollbar, A11y } from 'swiper/modules';
import { FaStar } from 'react-icons/fa'
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import { useContext } from 'react';
import ContextProvider from '../../context/ContextProvider';

const Slider = () => {

    const { feedback, isLoading } = useContext(ContextProvider)

    function renderStars(rating) {
        const stars = [];
        for (let i = 0; i < rating; i++) {
            stars.push(<FaStar key={i} />);
        }
        return stars;
    }

    return (
        <div>
            <Swiper
                modules={[Navigation, Pagination, Scrollbar, A11y]}
                spaceBetween={50}
                slidesPerView={1}
                navigation
                scrollbar={{ draggable: true }}
                onSlideChange={() => console.log('slide change')}
                onSwiper={(swiper) => console.log(swiper)}
            >
                {feedback.map((item) => (
                    <SwiperSlide>
                        <div className='shadow-2xl mx-24 md:mx-96 border-[#800020] border-[1px] md:p-12 flex flex-col place-items-center gap-6 p-8'>

                            <><h1 className='font-black text-2xl text-[#800020]'>{item.name}</h1><p className='text-center text-pretty'>{item.text}</p>
                                <div className='flex flex-row gap-1 text-2xl text-[#800020]'>
                                    {renderStars(item.rating)}
                                </div></>
                        </div>
                    </SwiperSlide>))}
            </Swiper>
        </div>
    );
}

export default Slider;