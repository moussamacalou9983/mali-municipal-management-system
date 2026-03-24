<!-- Last Modified Date: 18-04-2024
Personnalisation Mali -->
<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />

    <title>{{ config('branding.app_name') }} - Accueil</title>
    <!-- Google Fonts -->
    <link
        href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Roboto:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i"
        rel="stylesheet" />

    <!-- Vendor CSS Files -->
    <!-- <link href="{{ asset('landingpage/vendor/aos/aos.css') }}" rel="stylesheet" /> -->
    <link rel="stylesheet" href="{{asset('css/app.css')}}">
    <link rel="stylesheet" href="{{asset('css/style.css')}}">

</head>

<body>
    <!-- ======= Top Bar ======= -->
    <section id="topbar" class="d-flex align-items-center">
        <div class="container d-flex justify-content-center justify-content-md-between">
            <div class="contact-info d-flex align-items-center">
                <div class="d-flex p-4">
                    <i class="fas fa-envelope d-flex align-items-center"></i> 
                    <span class="p-2">{{ config('branding.contact_email') }}</span>
                </div>

                <div class="d-flex">
                    <i class="fas fa-phone d-flex align-items-center "></i>
                    <span class="p-2"> </span>
                </div>
            </div>
        </div>
    </section>

    <!-- ======= Header ======= -->
    <header id="header" class="d-flex align-items-center">
        <div class="container d-flex align-items-center justify-content-between">
            <a href="{{URL::to('/')}}" class="logo"><img src="{{ asset('img/logo-imis.png') }}" alt="{{ config('branding.app_name') }}" /></a>

            <nav id="navbar" class="navbar-landing">
                <ul>
                    <li><a class="nav-link scrollto active" href="#hero">{{ __('Home') }}</a></li>
                    <li><a class="nav-link scrollto" href="#about">{{ __('About') }}</a></li>
                    <li><a class="nav-link scrollto" href="#cwis">CWIS</a></li>
                    <li><a class="nav-link scrollto" href="#features">{{ __('Features') }}</a></li>
                    <li><a class="nav-link scrollto" href="#services">{{ __('Functional Modules') }}</a></li>
                    <li><a class="nav-link scrollto" href="#contact">{{ __('Contact') }}</a></li>
                    <li>
                        <button type="button" class="btn btn-get-started" data-toggle="modal" data-target="#loginModal">
                            {{ __('Log In') }}
                        </button>
                    </li>
                </ul>
                <i class="fa fa-bars  mobile-nav-toggle"></i>
            </nav>
            <!--navbar -->
        </div>

    </header>
    <!-- End Header -->

    <!-- ======= Hero Section ======= -->
    <section id="hero" class="d-flex align-items-center">

        <div class="container">
            <div class="row">
                <div class="col-lg-6 pt-4 pt-lg-0 order-2 order-lg-1 d-flex flex-column justify-content-center"
                    data-aos="zoom-out" data-aos-delay="100">
                    <div>
                        <h1>{{ config('branding.app_name') }}</h1>
                    </div>
                    <h2>{{ config('branding.tagline') }}</h2>
                </div>
                <div class="col-lg-6 order-1 order-lg-2 hero-img" data-aos="zoom-out" data-aos-delay="100">
                    <img src="{{ asset('/img/imislogo.svg') }}" class="img-fluid" alt="">
                </div>
            </div>
        </div>

    </section><!-- End Hero -->



    <main id="main">
         <!-- ======= About Section ======= -->
         <section id="about" class="about section-bg">
            <div class="container" data-aos="fade-up">
                <div class="section-title">
                    <!--<h2>About</h2>-->
                    <h3>{{ __('About') }} <span>{{ config('branding.short_name') }}</span></h3>
                </div>
               <div class="text-left">
                <p>
                Ce projet adapte Base IMIS pour un usage municipal au Mali. Il fournit une plateforme numerique fondee sur les SIG qui centralise les donnees, les processus et les services utiles a la gestion communale, en particulier pour l'assainissement, les infrastructures et le suivi des services urbains.
                <ul>
                   <li>Planification, gestion et suivi des services d'assainissement selon l'approche CWIS.</li>
                    <li>Suivi de bout en bout de la chaine de gestion des boues de vidange.</li>
                    <li>Production et visualisation d'indicateurs utiles a la prise de decision.</li>
                    <li>Tableaux de bord pour les metriques de gouvernance municipale et les services urbains.</li>
                </ul>

                Avec son architecture modulaire, cette version peut etre personnalisee pour les besoins d'une mairie, d'un service technique local ou d'un dispositif administratif territorial au Mali.
                </p>
                </div>
            </div>
        </section>
        <!-- End About Section -->

          <!-- ======= About Section ======= -->
          <section id="cwis" class="about">
            <div class="container" data-aos="fade-up">
                <div class="section-title">
                    <!--<h2>About</h2>-->
                    <h3>{{ __('Citywide Inclusive Sanitation') }} <span>(CWIS)</span></h3>
                </div>
                <div class="text-left">
                <p>
                CWIS is an approach to achieve SDG 6.2 for safe, equitable and financially viable sanitation systems and services. CWIS ensures everyone in a city has access to safely managed sanitation, and human waste is safely managed along the whole sanitation service chain ensuring protection of the environment and human health.
                </p>
                <img src="{{ asset('img/svg/landing-page/cwis.jpg') }}" class="cwis-img" alt="CWIS">
                <p>CWIS approach focuses on service provision and its enabling environment rather than on building infrastructure, therefore, reliable data is the key success factor for CWIS. UN Water SDG 6 global acceleration framework has also identified data and information as one of the five accelerators of SDG 6 outcomes.</p>
                </div>
            </div>
        </section>
        <!-- End About Section -->

        <!-- ======= Feature Section ======= -->
        <section id="features" class="about section-bg">
            <div class="container" data-aos="fade-up">
                <div class="section-title">
                    <!--<h2>About</h2>-->
                    <h3>{{ __('Features of') }} <span>{{ config('branding.short_name') }}</span></h3>
                </div>
                <div class="text-left">
                <ul>
                    <li>Visualisation cartographique des donnees municipales, des infrastructures et des services.</li>
<li>Gestion structuree des donnees techniques et administratives.</li>
<li>Integration des donnees CWIS pour la planification et le suivi des services d'assainissement.</li>
<li>Outils d'aide a la decision bases sur l'analyse spatiale et les tableaux de bord.</li>
<li>Interfaces utilisateurs avec gestion des roles et des acces.</li>
<li>Architecture extensible pour integrer d'autres besoins municipaux.</li>
<li>Connexion possible avec des donnees fiscales, sanitaires ou operationnelles.</li>
<li>Socle reutilisable pour une gouvernance locale plus fiable et plus transparente.</li>
</ul>
                </div>
                <div style="text-align: center">
                    <!-- <button class="btn-get-started"> Learn More</button> -->
                </div>

            </div>
        </section>
        <!-- End Feature Section -->

        <!-- ======= Services Section ======= -->
        <section id="services" class="service">
            <div class="container" data-aos="fade-up">
                <div class="section-title">
                    <!--<h2>Functionalities</h2>-->
                    <h3>{{ __('Functional') }}<span> {{ __('Modules') }}</span></h3>
                </div>

                <div class="row">
                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="100">
                        <div class="icon-box">
                           <img src="{{ asset('img/svg/landing-page/buildingIMS.svg') }}" class="icon" alt="Building Icon">
                            <div class="card-body float-right ">

                                <h5 class=" text-center ">Building Information Management System</h5>

                                <div class="card-text text-left">
                                    <ul>
                                        <li>Maintains information about all existing and new buildings with their building footprints, sanitation system, socio-economic condition, etc</li>
                                        <li>Maintains information about low-income communities with their geographic coverage and sanitation system
                                        </li>
                                    </ul>

                                </div>
                            </div>

                        </div>

                    </div>

                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="200">

                        <div class="icon-box">
                        <img src="{{ asset('img/svg/landing-page/propertyTaxCollectionIMS.svg')}}" class="icon">

                            <!--Card content-->
                            <div class="card-body">
                                <!--Title-->
                                <h5 class=" text-center ">Property Tax Collection Support System</h5>
                                <!--Text-->
                                <div class="card-text text-left ">
                                    <ul>
                                    <li>Enables to import of property tax or other revenue data into IMIS for spatial visualization of buildings or containments with their tax or revenue collection status</li>
                                    </ul>
                                </div>
                            </div>

                        </div>
                        <!--/.Card-->

                    </div>

                    <div class="col-md-4 mb-4 d-flex align-items-stretch " data-aos="zoom-in" data-aos-delay="300">
                        <div class="icon-box">
                        <img src="{{ asset('img/svg/landing-page/urbanManagementDSS.svg')}}" class="icon" alt="Urban Management DSS">

                                <div class="card-body">
                                    <!--Title-->
                                    <h5 class=" text-center ">Urban Management Decision Support System</h5>
                                    <!--Text-->
                                    <div class="card-text text-left">
                                        <ul>
                                        <li>Dashboard for monitoring the situation of sanitation and other elements required for planning, management and monitoring and evaluation of CWIS </li>
                                        <li>Dashboards for monitoring KPIs and CWIS indicators</li>
                                        <li>Tools for real-time monitoring of the sanitation service chain</li>
                                        <li>Spatial analysis tools</li>
                                        <li>Query and attribute analysis tools</li>
                                        <li>Basic navigation tools for exploration, analysis, and visualization of spatial data within a GIS environment and tools for printing maps</li>

                                        </ul>
                                    </div>
                                </div>

                            </div>
                            <!--/.Card-->
                        </div>
                    </div>


                <div class="row">
                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="100">
                        <div class="icon-box">
                        <img src="{{ asset('img/svg/landing-page/utilityIMS.svg')}}" class="icon" alt="Utility Icon">
                            <!--Card content-->
                            <div class="card-body">
                                <!--Title-->
                                <h5 class="text-center  ">Utility Information Management System</h5>
                                <!--Text-->
                                <div class="card-text text-left ">
                                    <ul>
                                    <li>Maintains road network information</li>
                                    <li>Maintains water supply network information</li>
                                    <li>Maintains sewerage network information</li>
                                    <li>Maintains drainage network information</li>
                                    </ul>
                                </div>
                            </div>

                        </div>
                        <!--/.Card-->
                    </div>

                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="100">

                        <div class="icon-box">
                        <img src="{{ asset('img/svg/landing-page/swmPaymentStatus.svg')}}" class="icon">
                            <!--Card content-->
                            <div class="card-body">
                                <!--Title-->
                                <h5 class=" text-center ">Solid Waste Information Support System</h5>
                                <!--Text-->
                                <div class="card-text text-left ">
                                    <ul>
                                    <li>Enables import of solid waste management data into the system for spatial visualization of buildings with their solid waste management status</li>
                                    </ul>
                                </div>
                            </div>

                        </div>
                        <!--/.Card-->
                    </div>


                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="300">

                        <div class="icon-box">
                        <img src="{{ asset('img/svg/landing-page/watersupplyISS.svg')}}" class="icon" alt="Water Supply ISS Icon">
                            <!--Card content-->
                            <div class="card-body">
                                <!--Title-->
                                <h5 class=" text-center ">Water Supply Information Support System</h5>
                                <!--Text-->
                                <div class="card-text text-left">
                                    <ul><li>Enables to import of water supply bill payment data into the system for spatial visualization of buildings with their bill payment status</li></ul>
                                </div>
                            </div>

                        </div>
                        <!--/.Card-->
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="200">

                        <div class="icon-box">
                        <img src="{{ asset('img/svg/landing-page/publicHealthISS.svg')}}" class="icon" alt="Fecal Sludge Icon">
                            <!--Card content-->
                            <div class="card-body">
                                <!--Title-->
                                <h5 class=" text-center ">Public Health Information Support System</h5>
                                <!--Text-->
                                <div class="card-text text-left ">
                                    <ul><li>Maintains information about hotspot areas where waterborne diseases occurred </li></ul>
                                </div>
                            </div>

                        </div>
                        <!--/.Card-->

                    </div>
                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="200">

                        <div class="icon-box">
                        <img src="{{ asset('img/svg/landing-page/ptctIMS.svg')}}" class="icon" alt="PTCT  Icon">

                                <!--Card content-->
                                <div class="card-body">
                                    <!--Title-->
                                    <h5 class=" text-center ">Public/Community Toilet (PT/CT) Information Management System</h5>
                                    <!--Text-->
                                    <div class="card-text text-left ">
                                        <ul>
                                            <li>
                                                Maintains information about all PTs and CTs in the city with the number of users used and their feedback
                                            </li>
                                        </ul>
                                    </div>
                                </div>

                        </div>
                        <!--/.Card-->
                    </div>

                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="200">

                        <div class="icon-box">
                        <img src="{{ asset('img/svg/landing-page/sewerConnectionIMS.svg')}}" class="icon" alt="PTCT  Icon">


                                <!--Card content-->
                                <div class="card-body">
                                    <!--Title-->
                                    <h5 class=" text-center ">Sewer Connection Information Management System</h5>
                                    <!--Text-->
                                    <div class="card-text text-left ">
                                        <ul>
                                            <li>
                                                Maintains information about all buildings and their corresponding sewer network
                                            </li>
                                        </ul>
                                    </div>
                                </div>

                        </div>
                        <!--/.Card-->
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-4 mb-4 d-flex align-items-stretch" data-aos="zoom-in" data-aos-delay="200">

                            <div class="icon-box">
                            <img src="{{ asset('img/svg/landing-page/fecalSludgeIMS.svg') }}" class="icon" alt="Fecal Sludge Icon">

                                    <!--Card content-->
                                    <div class="card-body p">
                                        <!--Title-->
                                        <h5 class=" text-center ">Fecal Sludge Information Management System</h5>
                                        <!--Text-->
                                        <div class="card-text text-left">
                                            <ul>
                                                <li>Maintains information about all containments with their geographic location </li>
                                                <li>Maintains information about FSM service providers and their resources</li>
                                                <li>Maintains information about the Fecal Sludge Treatment Plant and the FS disposed records</li>
                                                <li>Maintains the quality test record of treated wastewater and compost generated from the treatment plant</li>
                                                <li>Maintains records of services from containment emptying to transport, and desludging of FS in the treatment plant</li>
                                                <li>Maintains the customer feedback data</li>

                                            </ul>

                                        </div>
                                    </div>

                                </div>
                                <!--/.Card-->
                            </div>

                    </div>
                </div>
            </div>

        </section>

        <!-- ======= Contact Section ======= -->
        <section class="contact " id="contact">
            <div class="container" data-aos="fade-up">
                <div class="section-title">
                    <!--<h2>Contact</h2>-->
                    <h3>{{ __('Send a') }} <span>{{ __('message') }}</span></h3>
                </div>

                <div class="row ">

                    <div class="col-lg-4">
                        <div class="info">

                            <div class="address">
                                <i class="fas fa-map-marker-alt"></i>
                                <h4>{{ __('Location') }}:</h4>
                                <p></p>
                            </div>

                            <div class="email">
                                <i class=" icon far fa-envelope"></i>
                                <h4>{{ __('Email') }}:</h4>
                                <p>{{ config('branding.contact_email') }}</p>
                            </div>

                            <div class="phone">
                                <i class="fas fa-mobile-alt"></i>
                                <h4>{{ __('Call') }}:</h4>
                                <p>{{ config('branding.contact_phone') }}</p>
                            </div>

                        </div>

                    </div>

                    <div class="col-lg-8 mt-5 mt-lg-0">

                        <form action="{{ route('contact.send') }}" method="POST">
                            @csrf
                            <div class="row">
                                <div class="col-md-6 form-group">
                                    <input type="text" name="name" class="form-control" id="name" placeholder="{{ __('Your Name') }}" required>
                                </div>
                                <div class="col-md-6 form-group mt-3 mt-md-0">
                                    <input type="email" class="form-control" name="email" id="email" placeholder="{{ __('Your Email') }}" required>
                                </div>
                            </div>
                            <div class="form-group mt-3">
                                <input type="text" class="form-control" name="subject" id="subject" placeholder="{{ __('Subject') }}" required>
                            </div>
                            <div class="form-group mt-3">
                                <textarea class="form-control" name="message" rows="5" placeholder="{{ __('Message') }}" required></textarea>
                            </div>
                            <div class="text-center">
                                <button type="submit" class="btn btn-block">{{ __('Send Now!') }}</button>
                            </div>
                        </form>
                    </div>

                </div>
            </div>
        </section>
        <!-- End Contact Section -->
    </main>
    <!-- End #main -->

    <!-- ======= Footer ======= -->
    <footer id="footer" class="section-bg">
        <div class="container py-4">
        <div class="copyright">
            @include('includes.credits')
        </div>
        </div>
    </footer>
    <!-- End Footer -->

    <div id="preloader"></div>
    <a href="#" class="back-to-top d-flex align-items-center justify-content-center">
        <i class="fa fa-arrow-circle-up"></i></a>
    <div class="modal" id="loginModal">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header d-block">
                    <h5 class=" text-center ">{{ config('branding.app_name') }}</h5>
                </div>
                <div class="modal-body">
                    @include('auth.login')
                </div>
            </div>
        </div>
    </div>

    <!-- Vendor JS Files -->
    <script src="{{asset('js/app.js')}}"></script>
    <!-- Template Main JS File -->
    <script src="{{ asset('js/main.js')}}"></script>
    <script>
        function myFunction() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
    $(document).ready(function() {

        // var myModal = document.getElementById('loginModal');
        var error = <?php echo ($errors); ?>;

        if (error.length > 0) {
        $('#loginModal').modal('show');
    }
    })
    </script>
     <script>
        // JavaScript code to get and display the current year
        var currentYear = new Date().getFullYear();
        document.getElementById("currentYear").textContent = currentYear;
    </script>
</body>

</html>


