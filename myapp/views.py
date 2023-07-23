from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from myapp.forms import RegistrationForm


def get_country_codes():
    country_codes = [
        "+1 (United States)",
        "+44 (United Kingdom)",
        "+91 (India)",
        "+86 (China)",
        "+81 (Japan)",
        "+49 (Germany)",
        "+33 (France)",
        "+61 (Australia)",
        "+7 (Russia)",
        "+39 (Italy)",
        "+354 (Iceland)",
        "+46 (Sweden)",
        "+64 (New Zealand)",
        "+34 (Spain)",
        "+41 (Switzerland)",
        "+65 (Singapore)",
        "+82 (South Korea)",
        "+55 (Brazil)",
        "+52 (Mexico)",
        "+1 (Canada)",
        "+30 (Greece)",
        "+31 (Netherlands)",
        "+32 (Belgium)",
        "+45 (Denmark)",
        "+353 (Ireland)",
        "+43 (Austria)",
        "+420 (Czech Republic)",
        "+48 (Poland)",
        "+371 (Latvia)",
        "+370 (Lithuania)",
        "+359 (Bulgaria)",
        "+40 (Romania)",
        "+36 (Hungary)",
        "+351 (Portugal)",
        "+377 (Monaco)",
        "+373 (Moldova)",
        "+352 (Luxembourg)",
        "+372 (Estonia)",
        "+376 (Andorra)",
        "+354 (Iceland)",
        "+1 (United States)",
        "+1 (Canada)",
        "+7 (Russia)",
        "+61 (Australia)",
        "+44 (United Kingdom)",
        "+33 (France)",
        "+81 (Japan)",
        "+49 (Germany)",
        "+86 (China)",
        "+91 (India)",
        "+39 (Italy)",
        "+34 (Spain)",
        "+55 (Brazil)",
        "+52 (Mexico)",
        "+61 (Australia)",
        "+64 (New Zealand)",
        "+41 (Switzerland)",
        "+46 (Sweden)",
        "+31 (Netherlands)",
        "+32 (Belgium)",
        "+44 (United Kingdom)",
        "+98 (Iran)",
        "+964 (Iraq)",
        "+972 (Israel)",
        "+966 (Saudi Arabia)",
        "+965 (Kuwait)",
        "+971 (United Arab Emirates)",
        "+20 (Egypt)",
        "+212 (Morocco)",
        "+213 (Algeria)",
        "+216 (Tunisia)",
        "+218 (Libya)",
        "+249 (Sudan)",
        "+253 (Djibouti)",
        "+249 (South Sudan)",
        "+251 (Ethiopia)",
        "+252 (Somalia)",
        "+254 (Kenya)",
        "+255 (Tanzania)",
        "+256 (Uganda)",
        "+257 (Burundi)",
        "+258 (Mozambique)",
        "+260 (Zambia)",
        "+261 (Madagascar)",
        "+262 (Réunion)",
        "+263 (Zimbabwe)",
        "+264 (Namibia)",
        "+265 (Malawi)",
        "+266 (Lesotho)",
        "+267 (Botswana)",
        "+268 (Swaziland)",
        "+269 (Comoros)",
        "+27 (South Africa)",
        "+290 (Saint Helena, Ascension and Tristan da Cunha)",
        "+291 (Eritrea)",
        "+297 (Aruba)",
        "+298 (Faroe Islands)",
        "+299 (Greenland)",
        "+30 (Greece)",
        "+31 (Netherlands)",
        "+32 (Belgium)",
        "+33 (France)",
        "+34 (Spain)",
        "+350 (Gibraltar)",
        "+351 (Portugal)",
        "+352 (Luxembourg)",
        "+353 (Ireland)",
        "+354 (Iceland)",
        "+355 (Albania)",
        "+356 (Malta)",
        "+357 (Cyprus)",
        "+358 (Finland)",
        "+359 (Bulgaria)",
        "+36 (Hungary)",
        "+370 (Lithuania)",
        "+371 (Latvia)",
        "+372 (Estonia)",
        "+373 (Moldova)",
        "+374 (Armenia)",
        "+375 (Belarus)",
        "+376 (Andorra)",
        "+377 (Monaco)",
        "+378 (San Marino)",
        "+379 (Vatican City)",
        "+380 (Ukraine)",
        "+381 (Serbia)",
        "+382 (Montenegro)",
        "+383 (Kosovo)",
        "+385 (Croatia)",
        "+386 (Slovenia)",
        "+387 (Bosnia and Herzegovina)",
        "+389 (North Macedonia)",
        "+39 (Italy)",
        "+40 (Romania)",
        "+41 (Switzerland)",
        "+420 (Czech Republic)",
        "+421 (Slovakia)",
        "+423 (Liechtenstein)",
        "+43 (Austria)",
        "+44 (United Kingdom)",
        "+45 (Denmark)",
        "+46 (Sweden)",
        "+47 (Norway)",
        "+48 (Poland)",
        "+49 (Germany)",
        "+500 (Falkland Islands)",
        "+501 (Belize)",
        "+502 (Guatemala)",
        "+503 (El Salvador)",
        "+504 (Honduras)",
        "+505 (Nicaragua)",
        "+506 (Costa Rica)",
        "+507 (Panama)",
        "+508 (Saint Pierre and Miquelon)",
        "+509 (Haiti)",
        "+51 (Peru)",
        "+52 (Mexico)",
        "+53 (Cuba)",
        "+54 (Argentina)",
        "+55 (Brazil)",
        "+56 (Chile)",
        "+57 (Colombia)",
        "+58 (Venezuela)",
        "+590 (Guadeloupe)",
        "+591 (Bolivia)",
        "+592 (Guyana)",
        "+593 (Ecuador)",
        "+594 (French Guiana)",
        "+595 (Paraguay)",
        "+596 (Martinique)",
        "+597 (Suriname)",
        "+598 (Uruguay)",
        "+599 (Caribbean Netherlands)",
        "+599 (Curaçao)",
        "+60 (Malaysia)",
        "+61 (Australia)",
        "+62 (Indonesia)",
        "+63 (Philippines)",
        "+64 (New Zealand)",
        "+65 (Singapore)",
        "+66 (Thailand)",
        "+670 (Timor-Leste)",
        "+672 (Norfolk Island)",
        "+673 (Brunei)",
        "+674 (Nauru)",
        "+675 (Papua New Guinea)",
        "+676 (Tonga)",
        "+677 (Solomon Islands)",
        "+678 (Vanuatu)",
        "+679 (Fiji)",
        "+680 (Palau)",
        "+681 (Wallis and Futuna)",
        "+682 (Cook Islands)",
        "+683 (Niue)",
        "+685 (Samoa)",
        "+686 (Kiribati)",
        "+687 (New Caledonia)",
        "+688 (Tuvalu)",
        "+689 (French Polynesia)",
        "+690 (Tokelau)",
        "+691 (Micronesia)",
        "+692 (Marshall Islands)",
        "+7 (Russia)",
        "+76 (Kazakhstan)",
        "+77 (Kazakhstan)",
        "+800 (International Freephone)",
        "+808 (International Shared Cost Service)",
        "+81 (Japan)",
        "+82 (South Korea)",
        "+84 (Vietnam)",
        "+850 (North Korea)",
        "+852 (Hong Kong)",
        "+853 (Macau)",
        "+855 (Cambodia)",
        "+856 (Laos)",
        "+86 (China)",
        "+870 (Inmarsat SNAC)",
        "+871 (Inmarsat (Atlantic Ocean - East))",
        "+872 (Inmarsat (Pacific Ocean))",
        "+873 (Inmarsat (Indian Ocean))",
        "+874 (Inmarsat (Atlantic Ocean - West))",
        "+878 (Universal Personal Telecommunications (UPT))",
        "+880 (Bangladesh)",
        "+881 (Global Mobile Satellite System (GMSS))",
        "+882 (International Networks)",
        "+883 (International Networks)",
        "+886 (Taiwan)",
        "+888 (Telecommunications for Disaster Relief by OCHA)",
        "+90 (Turkey)",
        "+91 (India)",
        "+92 (Pakistan)",
        "+93 (Afghanistan)",
        "+94 (Sri Lanka)",
        "+95 (Myanmar)",
        "+960 (Maldives)",
        "+961 (Lebanon)",
        "+962 (Jordan)",
        "+963 (Syria)",
        "+964 (Iraq)",
        "+965 (Kuwait)",
        "+966 (Saudi Arabia)",
        "+967 (Yemen)",
        "+968 (Oman)",
        "+970 (Palestine)",
        "+971 (United Arab Emirates)",
        "+972 (Israel)",
        "+973 (Bahrain)",
        "+974 (Qatar)",
        "+975 (Bhutan)",
        "+976 (Mongolia)",
        "+977 (Nepal)",
        "+979 (International Premium Rate Service)",
        "+98 (Iran)",
        "+990 (ITPCS)",
        "+991 (ITPCS)",
        "+992 (Tajikistan)",
        "+993 (Turkmenistan)",
        "+994 (Azerbaijan)",
        "+995 (Georgia)",
        "+996 (Kyrgyzstan)",
        "+997 (ITPCS)",
        "+998 (Uzbekistan)",
        "+992 (Tajikistan)",
        "+993 (Turkmenistan)",
        "+994 (Azerbaijan)",
        "+995 (Georgia)",
        "+996 (Kyrgyzstan)",
        "+998 (Uzbekistan)"
    ]

    return country_codes


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate the user using the provided email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Login the user and set the user in the session
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        # Process the form submission when it's a POST request
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user data to the database
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            # Form is not valid, display errors to the user
            messages.error(request, 'Invalid form submission. Please correct the errors.')
    else:
        # Display the registration form when it's a GET request
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form, 'country_codes': get_country_codes()})


def logout_view(request):
    # Clear the user session to log them out
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def index_view(request):
    return render(request, 'index.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Perform the logic to handle the password reset process
        # For example, you can send a password reset email to the user

        # After processing the form, redirect to the login page or display a success message
        return redirect('login')  # Redirect to the login page
        # return render(request, 'password_reset_success.html')  # Display a success message

    return render(request, 'forgot_password.html')

def about_us(request):
    return render(request, 'about_us.html')
