---
## Front matter
title: "ОТЧЕТ ПО ИНДИВИДУАЛЬНОМУ ПРОЕКТУ ЭТАП №5"
subtitle: "Добавление к сайту всех остальных элементов"
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
#tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
#lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Целью данной работы является добавление к сайту всех остальных элементов.

# Задание

Добавить к сайту все остальные элементы.

1. Сделать записи для персональных проектов.
2. Сделать пост по прошедшей неделе.
3. Добавить пост на тему по выбору:
  - Языки научного программирования.

# Выполнение работы

Делаю записи для персональных проектов. (рис. [-@fig:001])

![Сделала записи для персональных проектов](image/ip05_1.png){ #fig:001 width=70% }

Пишу свой пример индивидуального проекта. (рис. [-@fig:002])

![Пишу свой пример индивидуального проекта](image/ip05_2.png){ #fig:002 width=70% }

Пишу пост по прошедшей неделе. (рис. [-@fig:003])

![Пишу пост по прошедшей неделе](image/ip05_3.png){ #fig:003 width=70% }

Добавляю пост на тему по выбору. (рис. [-@fig:004])

![Добавляю пост на тему по выбору](image/ip05_4.png){ #fig:004 width=70% }

# Вывод

В ходе выполнения данной работы я добавила к сайту все остальные элементы.