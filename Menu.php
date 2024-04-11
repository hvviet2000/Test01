Structute:
===================================================
- app
-- views
--- layouts
------- default.blade.php
------- sidebar.blade.php
--- pages
------- home.blade.php
------- about.blade.php
------- projects.blade.php
------- contact.blade.php
--- includes
------- head.blade.php
------- header.blade.php
------- footer.blade.php
------- sidebar.blade.php

===================================================

head.blade.php
<meta charset="utf-8">
<meta name="description" content="">
<meta name="author" content="Scotch">

<title>Super Cool Layouts</title>

<!-- load bootstrap from a cdn -->
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/twitter-bootstrap/3.0.3/css/bootstrap-combined.min.css">


===================================================

header.blade.php
<div class="navbar">
    <div class="navbar-inner">
        <a id="logo" href="/">Single Malt</a>
        <ul class="nav">
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/projects">Projects</a></li>
            <li><a href="/contact">Contact</a></li>
        </ul>
    </div>
</div>

===================================================
Default Layout and Pages (Home, Contact)

<!doctype html>
<html>
<head>
    @include('includes.head')
</head>
<body>
<div class="container">

    <header class="row">
        @include('includes.header')
    </header>

    <div id="main" class="row">

            @yield('content')

    </div>

    <footer class="row">
        @include('includes.footer')
    </footer>

</div>
</body>
</html>
===================================================
pages/home.blade.php
@extends('layouts.default')
@section('content')
    i am the home page
@stop



===================================================
pages/contact.blade.php
@extends('layouts.default')
@section('content')
    i am the contact page
@stop

===================================================
Sidebar Layout and Pages
includes/sidebar.blade.php
<!-- sidebar nav -->
    <nav id="sidebar-nav">
        <ul class="nav nav-pills nav-stacked">
            <li><a href="#">Fly to the Moon</a></li>
            <li><a href="#">Dig to China</a></li>
            <li><a href="#">Swim Across the Sea</a></li>
        </ul>
    </nav>

===================================================
layouts/sidebar.blade.php

<!doctype html>
<html>
<head>
    @include('includes.head')
</head>
<body>
<div class="container">

    <header class="row">
        @include('includes.header')
    </header>

    <div id="main" class="row">

        <!-- sidebar content -->
        <div id="sidebar" class="col-md-4">
            @include('includes.sidebar')
        </div>

        <!-- main content -->
        <div id="content" class="col-md-8">
            @yield('content')
        </div>

    </div>

    <footer class="row">
        @include('includes.footer')
    </footer>

</div>
</body>
</html>

===================================================
pages/about.blade.php
@extends('layouts.sidebar')
@section('content')
    i am the about page
@stop
