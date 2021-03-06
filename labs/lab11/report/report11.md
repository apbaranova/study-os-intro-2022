---
## Front matter
title: "ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ №11"
subtitle: "Программирование в командном процессоре ОС UNIX. Ветвления и циклы"
author: "Анастасия Павловна Баранова, НБИбд-01-21"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
#lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Целью данной работы является изучить основы программирования в оболочке ОС UNIX и научиться писать более сложные командные файлы с использованием логических управляющих конструкций и циклов.

# Выполнение лабораторной работы

Используя команды getopts grep, напишу командный файл, который анализирует
командную строку с ключами:
– -iinputfile — прочитать данные из указанного файла;
– -ooutputfile — вывести данные в указанный файл;
– -pшаблон — указать шаблон для поиска;
– -C — различать большие и малые буквы;
– -n — выдавать номера строк.
а затем ищет в указанном файле нужные строки, определяемые ключом -p.(рис. [-@fig:001], рис. [-@fig:002], рис. [-@fig:003], рис. [-@fig:004])

![Напишу командный файл.](image/11_1.png){#fig:001 width=70%}

![Указанный файл с текстом.](image/11_2.png){#fig:002 width=70%}

![Демонстрирую работу командного файла.](image/11_3.png){#fig:003 width=70%}

![Демонстрирую работу командного файла.](image/11_4.png){#fig:004 width=70%}

Напишу на языке Си программу, которая вводит число и определяет, является ли оно больше нуля, меньше нуля или равно нулю. Затем программа завершается с помощью функции exit(n), передавая информацию в о коде завершения в оболочку. Командный файл должен вызывать эту программу и, проанализировав с помощью команды $?, выдать сообщение о том, какое число было введено. (рис. [-@fig:005], рис. [-@fig:006], рис. [-@fig:007])

![Напишу на языке Си программу.](image/11_5.png){#fig:005 width=70%}

![Напишу командный файл.](image/11_6.png){#fig:006 width=70%}

![Демонстрирую работу командного файла.](image/11_7.png){#fig:007 width=70%}

Напишу командный файл, создающий указанное число файлов, пронумерованных последовательно от 1 до N (например 1.tmp, 2.tmp, 3.tmp,4.tmp и т.д.). Число файлов, которые необходимо создать, передаётся в аргументы командной строки. Этот же командный файл должен уметь удалять все созданные им файлы (если они существуют). (рис. [-@fig:008], рис. [-@fig:009], рис. [-@fig:010], рис. [-@fig:011])

![Напишу командный файл.](image/11_8.png){#fig:008 width=70%}

![Демонстрирую работу командного файла.](image/11_9.png){#fig:009 width=70%}

![Демонстрирую работу командного файла.](image/11_10.png){#fig:010 width=70%}

![Демонстрирую работу командного файла.](image/11_11.png){#fig:011 width=70%}

Напишу командный файл, который с помощью команды tar запаковывает в архив
все файлы в указанной директории. Модифицирую его так, чтобы запаковывались
только те файлы, которые были изменены менее недели тому назад (использую
команду find). (рис. [-@fig:012], рис. [-@fig:013])

![Напишу командный файл.](image/11_12.png){#fig:012 width=70%}

![Демонстрирую работу командного файла.](image/11_13.png){#fig:013 width=70%}

# Вывод

В ходе данной лабораторной работы я изучила основы программирования в оболочке ОС UNIX/Linux, научилась писать более сложные командные файлы с использованием логических управляющих конструкций и циклов.

# Ответы на контрольные вопросы

1. Каково предназначение команды getopts?
  Ответ: Команда getopts является встроенной командой командной оболочки bash, предназначенной для разбора параметров сценариев. Она обрабатывает исключительно однобуквенные параметры как с аргументами, так и без них и этого вполне достаточно для передачи сценариям любых входных данных.
2. Какое отношение метасимволы имеют к генерации имён файлов?
  Ответ: При генерации имен используют метасимволы:

  произвольная (возможно пустая) последовательность символов; ? один произвольный символ; [...] любой из символов, указанных в скобках перечислением и/или с указанием диапазона; cat f* выдаст все файлы каталога, начинающиеся с "f"; cat f выдаст все файлы, содержащие "f"; cat program.? выдаст файлы данного каталога с однобуквенными расширениями, скажем "program.c" и "program.o", но не выдаст "program.com"; cat [a-d]* выдаст файлы, которые начинаются с "a", "b", "c", "d". Аналогичный эффект дадут и команды "cat [abcd]" и "cat [bdac]".

3. Какие операторы управления действиями вы знаете?
  Ответ: Операторы && и || являются управляющими операторами. Если в командной строке стоит command1 && command2, то command2 выполняется в том, и только в том случае, если статус выхода из команды command1 равен нулю, что говорит об успешном ее завершении. Аналогично, если командная строка имеет вид command1 || command2, то команда command2 выполняется тогда, и только тогда, когда статус выхода из команды command1 отличен от нуля.
4. Какие операторы используются для прерывания цикла?
  Ответ: Оператор break завершает выполнение ближайшего включающего цикла или условного оператора, в котором он отображается.
5. Для чего нужны команды false и true?
  Ответ: Команда true всегда возвращает ноль в качестве выходного статуса для индикации успеха. Команда false всегда возвращает не-ноль в качестве выходного статуса для индикации неудачи. Во всех управляющих конструкциях в качестве логического значения используется код возврата из программы, указанной в качестве условия. Код возврата 0 – истина, любое другое значение – ложь. Программа true – всегда завершается с кодом 0, false – всегда завершается с кодом 1.
6. Что означает строка if test -f man$s/$i.$s, встреченная в командном файле?
  Ответ: Введенная строка означает условие существования файла man$s/$i.$s
7. Объясните различия между конструкциями while и until.
  Ответ: Цикл While выполняется до тех пор, пока указанное в нем условие истинно. Когда указанное условие становится ложным - цикл завершается. Цикл Until выполняется до тех пор, пока указанное в нем условие ложно.