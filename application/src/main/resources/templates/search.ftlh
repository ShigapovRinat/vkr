<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <style>
        .gradient-custom {
            /* fallback for old browsers */
            background: #6a11cb;

            /* Chrome 10-25, Safari 5.1-6 */
            background: -webkit-linear-gradient(to right, rgba(106, 17, 203, 1), rgba(37, 117, 252, 1));

            /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
            background: linear-gradient(to right, rgba(106, 17, 203, 1), rgba(37, 117, 252, 1))
        }
    </style>

    <title>Search Players</title>
</head>
<body>
<header>
    <nav class="navbar navbar-expand-lg fixed-top navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Поиск игроков</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown"
                aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#">Хоккей</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Футбол</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Баскетбол</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Волейбол</a>
                </li>
            </ul>
        </div>
    </nav>
</header>

<section class="vh-100 gradient-custom">
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                <div class="card bg-dark text-white" style="border-radius: 1rem;">
                    <div class="card-body p-5 text-center">

                        <div class="mb-md-5 mt-md-4 pb-5">

                            <h2 class="fw-bold mb-2 text-uppercase">Хоккей</h2>
                            <p class="text-white-50 mb-5">Пожалуйста выберите команду и амплуа</p>

                            <form action="/hockey/players" method="post">
                                <div class="form-outline form-white mb-4">
                                    <p><select required name="team">
                                            <option selected disabled>Выберите команду</option>
                                            <option value="Amur (Khabarovsk)">Амур</option>
                                            <option value="Avtomobilist (Ekaterinburg)">Автомобилист</option>
                                            <option value="Avangard (Omsk)">Авангард</option>
                                            <option value="Ak Bars (Kazan)">Ак Барс</option>
                                            <option value="Barys (Nur-Sultan)">Барыс</option>
                                            <option value="Vityaz (Moscow Region)">Витязь</option>
                                            <option value="Dinamo (Minsk)">Динамо Минск</option>
                                            <option value="Dynamo (Moscow)">Динамо Москва</option>
                                            <option value="Neftekhimik (Nizhnekamsk)">Нефтехимик</option>
                                            <option value="SKA (Saint Petersburg)">СКА</option>
                                            <option value="Spartak (Moscow)">Спартак</option>
                                            <option value="Salavat Yulaev (Ufa)">Салават Юлаев</option>
                                            <option value="Severstal (Cherepovets)">Северсталь</option>
                                            <option value="Metallurg (Magnitogorsk)">Металлург</option>
                                            <option value="Kunlun Red Star (Beijing)">Куньлунь Ред Стар</option>
                                            <option value="Sibir (Novosibirsk Region)">Сибирь</option>
                                            <option value="Torpedo (Nizhny Novgorod Region)">Торпедо</option>
                                            <option value="Lokomotiv (Yaroslavl)">Локомотив</option>
                                            <option value="CSKA (Moscow)">ЦСКА</option>
                                        </select></p>
                                </div>

                                <div class="form-outline form-white mb-4">
                                    <p><select required name="position">
                                            <option selected disabled>Выберите амплуа</option>
                                            <option value="forward">Нападающий</option>
                                            <option value="defense">Защитник</option>
                                        </select></p>
                                </div>

                                <button class="btn btn-outline-light btn-lg px-5" type="submit">Найти</button>
                            </form>

                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>
</body>
</html>