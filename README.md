# Steganografie

## Utilizare

1. `/image/encode`: Printr-o metoda POST, aceasta ruta accepta o imagine si un text. Textul va fi codat in imagine, iar imaginea rezultata va fi afisata in browser si va putea fi descarcata.
2. `/image/decode`: Printr-o metoda POST, aceasta ruta accepta o imagine. Textul codificat in imagine va fi afisat in browser.
3. `/image/last/encode`: Printr-o metoda GET, aceasta ruta returneaza ultima imagine codificata ca un fisier de descarcat.
4. `/image/last/decode`: Printr-o metoda GET, aceasta ruta returneaza textul codificat ca plain text.

## Implementare

    Pentru implementarea proiectului am folosit urmatoarele biblioteci:
    - flask
    - PIL

*  Am folosit flask pentru a crea un server web care sa returneze imaginile oferite de utilizator ca fisiere de descarcat si pentru a afisa textul decodat. 

*  Biblioteca PIL a fost folosita pentru a reprezenta fiecare pixel ca un triplet de valori RGB.

*  Pentru a codifica textul in imagine am folosit metoda LSB (Least Significant Bit) care consta in inlocuirea ultimului bit din fiecare valoare RGB a pixelului cu un bit din textul ce trebuie codificat. Am facut un si logic cu 0xFE care pune 0 pe ultimul bit si am facut un sau logic cu bitul din textul ce trebuie codificat. Imaginea originala, cea codificata si textul codificat sunt salvate in `./static/image_requests/`.

*  Deoarece am intampinat probleme la decodificare textului (textul returnat avea si alte caractere in afara de cele codificate) am decis sa adaug un '\0' la finalul textului inainte de codificare, iar la decodificare sa returnez textul pana la primul '\0' intalnit.

*  Pentru design-ul site-ului am folosit css. Am decis sa folosesc un design minimalist, pentru a nu distrage atentia de la functionalitatea site-ului. De asemenea, am adaugat scurte glume pe fiecare pagina pentru a face site-ul mai placut.