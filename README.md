# DUMP

(a DUMP of Unreasonably Mediocre Passwords) 

* Το πρόγραμμα είναι γραμμένο για Python2.7

* Εμπνευσμένο από το cupp και σχεδιασμένο για pentesting στην Ελλάδα.

* Author: Orestis Kranias
* kraniasorestis@protonmail.com
* www.github.com/kraniasorestis
* Copyright (C) 2016
* Contributor: Panagiotis Simakis - https://github.com/sp1thas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

 see <http://www.gnu.org/licenses/>




ΟΔΗΓΙΕΣ ΧΡΗΣΗΣ

Αν θέλετε να δουλέψει σωστά πρέπει να το χρησιμοποιήσετε "ορθογραφημένα" - δηλαδή:

* Τα ήτα να δίνονται με 'h' και όχι με 'i'. (η ανορθογραφία είναι δουλειά του leet)
* Tο ωμέγα να συμβολίζεται με 'w' και όχι με 'ο'
* Οι δίφθογκοι να γράφονται "κανονικά, δηλαδή "mp" και όχι "b", "nt" - όχι "d",
"gk" ή "gg" - όχι "g". Τα διπλά φωνήεντα επίσης: ei, oi, ai, και όχι 'i' kai 'e'.
* Λοιποί κανόνες ορθογραφίας-greeklish

! Tα ονόματα να δίνονται με το πρώτο γράμμα μικρό και την καθημερινή τους μορφή !
! (το Dump θα συμπεριλάβει την επίσημη μορφή και την μορφή με το κεφαλαίο.)     !
πχ dhmhtrhs αντί για Dimitrios


DISCLAIMER

Αυτό το πρόγραμμα έχει γραφτεί για pen-testing εντός Ελλάδας. Δεν φέρω ευθύνη
για τυχόν παράνομη χρήση, στην οποία περίπτωση η ευθύνη βαραίνει τον χρήστη.



ΔΥΟ ΛΟΓΙΑ ΓΙΑ ΤΟ DUMP

Το πρόγραμμα είναι ένα personalized wordlist generator, το οποίο στην δεύτερη έκδοσή του φέρει:

* Διορθωμένο κώδικα που εξαλείφει το 80% των junk passwords του output της προηγούμενης έκδοσης
* Πιο εύλογες υποθέσεις για τους συνδυασμούς στοιχείων προς πιθανούς κωδικούς (πιο reasonable passwords)
* Optional και βελτιωμένο leet mode ( A/4, e/3, v/7/T κτλ)
* Optional επιλογή ένταξης κοινών bad & vulgar passwords στην wordlist
* Δραστικά καλύτερο function για υποκοριστικά
* Δυνατότητα ένταξης επιπλέον wordlists (πχ αποτελέσματα του cewl κτλ) - απλώς ρίχνοντάς τα στον φάκελο additional_wordlists - οι οποίες worldists συνδυάζονται αμέσως με τις χρονολογίες και ενδεχομένως leet mode. 


