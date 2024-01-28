
import { FaArrowDown, FaArrowUp } from "react-icons/fa";
import { useState, useRef } from "react";
import { Link } from "react-router-dom";
import { useLocation } from "react-router-dom";
import { useEffect } from "react";
import LawyersList from "../../data/FeedbackData";
import SearchBar from "../shared/SearchBar";


const Lawyers = () => {

    const [isOpen, setIsOpen] = useState(false)

    const showMenu = () => {
        setIsOpen(!isOpen)
    }

    const [selectedLocation, setSelectedLocation] = useState('');
    const [selectedSpeciality, setSelectedSpeciality] = useState('');

    const locationDropdownRef = useRef(null);
    const specialityDropdownRef = useRef(null);
    const searchDropdownRef = useRef(null);

    const handleClear = () => {
        setSelectedLocation('');
        setSelectedSpeciality('');
        specialityDropdownRef.current.value = '';
        locationDropdownRef.current.value = '';
    };

    const handleSearch = () => {
        console.log('Searching with Location:', selectedLocation);
        console.log('Searching with Speciality:', selectedSpeciality);
    };


    return (
        <div>
            <section class="bg-white">
                <div class="px-4 mx-auto max-w-screen-xl lg:py-8 lg:px-6 ">
                    <div class="mx-auto max-w-screen-sm text-center lg:mb-4">
                        <h2 class="mb-4 text-4xl tracking-tight font-extrabold text-gray-900">Our Lawyers</h2>
                    </div>

                    <button onClick={showMenu}
                        className="my-4 font-black flex flex-row items-center gap-2">Filter
                        {isOpen ? <FaArrowUp size={13} /> : <FaArrowDown size={13} />}
                    </button>

                    {/* Filtering menu */}
                    {isOpen && <div className="bg-neutral-200 flex flex-col mb-4 rounded-sm p-8 gap-8">
                        {/* Filters */}
                        <div className="flex flex-row justify-between gap-16">
                            {/* Legal issue bar */}
                            <select ref={specialityDropdownRef}
                                onChange={(e) => setSelectedSpeciality(e.target.value)}
                                className="h-14 w-full border-none p-2">
                                <option selected disabled value="">Legal issue</option>
                                <option value="faillite">Avocat de la faillite</option>
                                <option value="emploi">Avocat à l'emploi</option>
                                <option value="famille">Avocat familial</option>
                                <option value="general">Avocat généraliste</option>
                                <option value="fiscal">Avocat fiscaliste</option>
                                <option value="penal">Droit pénal</option>
                                <option value="civil">Droit civil</option>
                                <option value="affaires">Droit des affaires</option>
                                <option value="civil">Droit civil</option>
                                <option value="commercial">Droit commercial</option>
                                <option value="administratif">Administratif</option>
                            </select>
                            {/* Wilaya bar */}
                            <select ref={locationDropdownRef}
                                onChange={(e) => setSelectedLocation(e.target.value)}
                                className="h-14 w-full border-none p-2">
                                <option selected disabled value="">Wilaya</option>
                                <option value="Adrar">Adrar</option>
                                <option value="Chlef">Chlef</option>
                                <option value="Laghouat">Laghouat</option>
                                <option value="Oum El Bouaghi">Oum El Bouaghi</option>
                                <option value="Batna">Batna</option>
                                <option value="Bejaia">Béjaïa</option>
                                <option value="Biskra">Biskra</option>
                                <option value="Bechar">Béchar</option>
                                <option value="Blida">Blida</option>
                                <option value="Bouira">Bouira</option>
                                <option value="Tamanrasset">Tamanrasset</option>
                                <option value="Tebessa">Tébessa</option>
                                <option value="Tlemcen">Tlemcen</option>
                                <option value="Tiaret">Tiaret</option>
                                <option value="Tizi Ouzou">Tizi Ouzou</option>
                                <option value="Alger">Alger</option>
                                <option value="Djelfa">Djelfa</option>
                                <option value="Jijel">Jijel</option>
                                <option value="Setif">Sétif</option>
                                <option value="Saida">Saïda</option>
                                <option value="Skikda">Skikda</option>
                                <option value="Sidi Bel Abbes">Sidi Bel Abbès</option>
                                <option value="Annaba">Annaba</option>
                                <option value="Guelma">Guelma</option>
                                <option value="Constantine">Constantine</option>
                                <option value="Medea">Médéa</option>
                                <option value="Mostaganem">Mostaganem</option>
                                <option value="Msila">M'Sila</option>
                                <option value="Mascara">Mascara</option>
                                <option value="Ouargla">Ouargla</option>
                                <option value="Oran">Oran</option>
                                <option value="El Bayadh">El Bayadh</option>
                                <option value="Illizi">Illizi</option>
                                <option value="Bordj Bou Arreridj">Bordj Bou Arréridj</option>
                                <option value="Boumerdes">Boumerdès</option>
                                <option value="El Tarf">El Tarf</option>
                                <option value="Tindouf">Tindouf</option>
                                <option value="Tissemsilt">Tissemsilt</option>
                                <option value="El Oued">El Oued</option>
                                <option value="Khenchela">Khenchela</option>
                                <option value="Souk Ahras">Souk Ahras</option>
                                <option value="Tipaza">Tipaza</option>
                                <option value="Mila">Mila</option>
                                <option value="Ain Defla">Aïn Defla</option>
                                <option value="Naama">Naâma</option>
                                <option value="Ain Temouchent">Aïn Témouchent</option>
                                <option value="Ghardaia">Ghardaïa</option>
                                <option value="Relizane">Relizane</option>
                                <option value="El Mghair">El M'Ghair</option>
                                <option value="Ouled Djellal">Ouled Djellal</option>
                                <option value="Beni Abbes">Beni Abbes</option>
                                <option value="In Salah">In Salah</option>
                                <option value="In Guezzam">In Guezzam</option>
                            </select>

                        </div>
                        {/* Search bar */}
                        <SearchBar />
                        {/* Clear + search buttons */}
                        <div className="flex justify-end gap-3">
                            <button onClick={handleClear} className="px-8 py-2 bg-[#800020] text-white hover:bg-red-800">Clear</button>
                            <button onClick={handleSearch} className="px-8 py-2 bg-[#800020] text-white hover:bg-red-800">Search</button>
                        </div>
                    </div>}


                    {/* Lawyers */}
                    < div class="grid gap-8 mb-6 lg:mb-16 md:grid-cols-2" >
                        {/* Lawyer */}
                        {LawyersList.map((lawyer) => (
                            <div class="items-center bg-gray-50 rounded-lg shadow sm:flex" key={lawyer.id}>
                                <Link to={`/lawyers/${lawyer.id}`}>
                                    <img class="w-full rounded-lg sm:rounded-none sm:rounded-l-lg" src={lawyer.image}/>
                                </Link>
                                <div class="p-5">
                                    <h3 class="text-xl font-bold tracking-tight text-gray-900">
                                        <Link to={`/lawyers/${lawyer.id}`}>{lawyer.name}</Link>
                                    </h3>
                                    <span class="text-gray-500 capitalize">{lawyer.speciality}</span>
                                    <p class="mt-3 mb-4 font-light text-gray-500">{lawyer.text}</p>
                                    <Link to={`/lawyers/${lawyer.id}`}>
                                        <button className="px-8 py-2 bg-[#800020] text-white hover:bg-red-800">Visit profile</button>
                                    </Link>
                                </div>
                            </div>))}
                    </div>
                </div >
            </section >
        </div >
    );
}

export default Lawyers;
