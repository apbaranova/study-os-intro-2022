---
## Front matter
title: "Индивидуальный проект - 2 этап"
subtitle: "Работа с сайтом"
author: "Баранова Анастасия НБИбд-01-21"

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
lot: true # List of tables
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
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы: 

Научиться оформлять сайт, менять информацию о себе и создавать несколько постов.

# Ход работы:

Для начала я должна добавить на свой сайт фотографию, сделала это через файлы в папке blog. (рис. [-@fig:001])

![Личная фотография на сайте](image/1.png){ #fig:001 width=70% } 

Далее я добавила информацию о себе, а именно свое имя, вуз и биографию.(рис. [-@fig:002])

![bio](image/2.png){ #fig:002 width=70% } 

Далее я должна добавить пост по прошедшей неделе(рис. [-@fig:003])

![post last week](image/3.png){ #fig:003 width=70% } 

Также пишу еще один пост на тему по выбору, я выбрала тему - Управление версиями Гит(рис. [-@fig:004])(рис. [-@fig:005])

![Еще один пост](image/4.png){ #fig:004 width=70% } 

![Еще один пост](image/5.png){ #fig:005 width=70% } 


Итоговый внешний вид сайта:(рис. [-@fig:006])

![Сайт](image/2.png){ #fig:006 width=70% } 

# Вывод:

Я научилась оформлять личный сайт, а также создавать посты.

















