# Esse3Api

> WARNING: this have been hacked together in a couple of hours, don't expect a lot

This python library simplifies the connection of Cineca's REST API for ESSE3. It handles data retrieval transparently and gets the required information on-demand, i.e. API calls are made only when new data is needed.

## Installing

```bash
pip install Esse3Api
```

## Background

ESSE3 is a system developed by [Cineca](http://cineca.it/), used by many Italian Universities, to handle both internal management and students data. It can be used to look at a student's career and exam status, to manage secretary services, book exams, handle student taxes, etc.

Cineca developed a REST API for ESSE3, which unfortunately hasn't been publicized a lot. For this reason **I don't really know if it's intended for public use**, but since there is no block nor any need for an API key, I assume it can be done. Don't trust me on this. If in doubt, take this as an academic experiment.

Finding the API endpoint wasn't easy, but, eventually, I found out (by sheer luck) [my University's one](https://www.studenti.unipi.it/e3rest/api). With it, it comes a not really detailed [documentation](https://www.studenti.unipi.it/e3rest/docs/) (which, again, being accessible to anyone lets me think it is indeed public).

## Documentation

This GitHub project has a wiki page, with full documentation of the library.

## University support

Once you can find an endpoint, you can find them all.

I've made a list of all the endpoints I've found, they are already present in the library. However, since I attend only one of the Universities, I wasn't able to test them all. Please look at the following table for more details:

| University | Tested | Working |
| ---------- | ------ | ------- |
| Politecnico di Bari | :x: | :grey_question: |
| Università degli Studi della Basilicata | :x: | :grey_question: |
| Università degli Studi di Bari Aldo Moro | :x: | :grey_question: |
| Università degli Studi di Bergamo | :x: | :grey_question: |
| Università degli Studi di Brescia | :x: | :grey_question: |
| Università della Calabria | :x: | :grey_question: |
| Università degli Studi della Campania Luigi Vanvitelli | :x: | :grey_question: |
| Università Campus Bio-Medico di Roma | :x: | :grey_question: |
| Università di Camerino | :x: | :grey_question: |
| Università degli Studi di Cagliari | :x: | :grey_question: |
| Università degli Studi G. D'Annunzio Chieti Pescara | :x: | :grey_question: |
| Università degli Studi di Firenze | :x: | :grey_question: |
| Università degli Studi Guglielmo Marconi | :x: | :grey_question: |
| Università degli Studi di Messina | :x: | :grey_question: |
| Università degli Studi di Milano-Bicocca | :x: | :grey_question: |
| Università degli Studi di Modena e Reggio Emilia | :x: | :grey_question: |
| Università degli Studi dell'Insubria | :x: | :grey_question: |
| Università degli Studi di Perugia | :x: | :grey_question: |
| Università di Pisa | :heavy_check_mark: | :heavy_check_mark: |
| Università di Parma | :x: | :grey_question: |
| Università degli Studi di Pavia | :x: | :grey_question: |
| Università degli Studi della Repubblica di San Marino | :x: | :grey_question: |
| Università degli Studi del Sannio | :x: | :grey_question: |
| Università degli Studi di Trento | :x: | :grey_question: |
| Università di Torino | :x: | :grey_question: |
| Università degli Studi di Trieste | :x: | :grey_question: |
| Università degli Studi di Udine | :x: | :grey_question: |
| Università degli Studi di Urbino Carlo Bo | :x: | :grey_question: |
| Università degli Studi dell'Aquila | :x: | :grey_question: |
| Università Ca' Foscari Venezia | :x: | :grey_question: |
| Università Politecnica delle Marche | :x: | :grey_question: |
