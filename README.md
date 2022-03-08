# [Intermediário] Previsão do Tempo com a API do Open Weather Map

Este programa faz uma requisão para a API do [Open Weather Map](https://openweathermap.org/) para obter dados climáticos de uma cidade especificada.

A URL da requisição é montada a partir de quatro parâmetros:

- Nome da cidade;
- Idioma;
- Sistema de unidades;
- Token de acesso à API.

Defini o idioma de exibição dos resultados para Português do Brasil (pt_BR) e o sistema de unidades para métrico. Já o token de acesso à API foi salvo no arquivo .env. Assim, caso você deseje usar este programa, deverá primeiro criar sua conta no site do Open Weather Map e depois obter seu token da API e salvá-lo no seu próprio arquivo .env.
