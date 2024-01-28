const Footer = () => {
    return (
    <footer class="shadow bg-black mt-8">
        <div class="w-full max-w-screen-xl mx-auto p-4 md:py-8">
            <div class="sm:flex sm:items-center sm:justify-between">
                <a href="" class="flex items-center mb-4 sm:mb-0 space-x-3 rtl:space-x-reverse">
                    <span class="self-center text-2xl font-semibold whitespace-nowrap text-white hover:text-red-800">DZ Mouhami</span>
                </a>
                <ul class="flex flex-wrap items-center mb-6 text-sm font-medium sm:mb-0 text-white">
                    <li>
                        <a href="#" class="hover:underline hover:text-red-800 me-4 md:me-6">About</a>
                    </li>
                    <li>
                        <a href="#" class="hover:underline hover:text-red-800 me-4 md:me-6">Privacy Policy</a>
                    </li>
                    <li>
                        <a href="#" class="hover:underline hover:text-red-800 me-4 md:me-6">Licensing</a>
                    </li>
                    <li>
                        <a href="#" class="hover:underline hover:text-red-800">Contact</a>
                    </li>
                </ul>
            </div>
            <hr class="my-6 border-white sm:mx-auto lg:my-8" />
            <span class="block text-sm text-white sm:text-center">© 2023 <a href="" class="hover:underline hover:text-red-800">DZ Mouhami™</a>. All Rights Reserved.</span>
        </div>
    </footer>);
}

export default Footer;