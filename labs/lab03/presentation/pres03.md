---
## Front matter
lang: ru-RU
title: Лабораторная работа No 2.
author: |
	Анастасия Павловна Баранова, НБИбд-01-21\inst{1}
institute: |
	\inst{1}Российский Университет Дружбы Народов

date: 27 апреля, Москва, 2022 г.

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Управление версиями

## Цель работы

Целью данной работы является изучение идеологии и применения средств контроля версий и освоение умений работать с git.

# Выполнение лабораторной работы

## Настройка github

Создаю учетную запись на github и заполняю основные данные.

![Создание учётной записи на github.](../report/image/02_1.png)

## Установка программного обеспечения

Устанавливаю git-flow.

![Установка git-flow.](../report/image/02_2.png)

Устанавливаю gh.

![Установка gh.](../report/image/02_3.png)

## Базовая настройка git

Задаю имя и email владельца репозитория.

![Базовая настройка git.](../report/image/02_4.png)

Настрою utf-8 в выводе сообщений git.

![Базовая настройка git.](../report/image/02_5.png)

Настрою верификацию и подписание коммитов git. Зададам имя начальной ветки (будем называть её master), параметр autocrlf, параметр safecrlf.

![Базовая настройка git.](../report/image/02_6.png)

## Создание ключей ssh

Создам ключ ssh по алгоритму rsa с ключём размером 4096 бит.

![Создание ключа ssh.](../report/image/02_7.png)

Создам ключ ssh по алгоритму ed25519.

![Создание ключа ssh.](../report/image/02_8.png)

## Создание ключей gpg

Генерирую ключ gpg.

![Создание ключа gpg.](../report/image/02_9.png)

## Добавление GPG ключа в GitHub

Добавляю GPG ключ в GitHub. Вывожу список ключей и копирую отпечаток приватного ключа.

![Добавление GPG ключа в GitHub.](../report/image/02_10.png)

![Добавление GPG ключа в GitHub.](../report/image/02_11.png)

Перехожу в настройки GitHub (https://github.com/settings/keys), нажимаю на кнопку New GPG key и вставляю полученный ключ в поле ввода.

![Добавление GPG ключа в GitHub.](../report/image/02_12.png)

## Настройка автоматических подписей коммитов git

Настрою автоматические подписи коммитов git. Используя введёный email, укажу Git применять его при подписи коммитов.

![Настройка автоматических подписей коммитов git.](../report/image/02_13.png)

## Настройка gh

Настрою gh. Авторизуюсь.

![Настройка gh.](../report/image/02_14.png)

## Шаблон для рабочего пространства

Создам репозиторий курса на основе шаблона.

![Создание репозитория курса на основе шаблона.](../report/image/02_15.png)

![Создание репозитория курса на основе шаблона.](../report/image/02_16.png)

Настрою каталог курса.

![Настройка каталога курса.](../report/image/02_17.png)

![Настройка каталога курса.](../report/image/02_18.png)

## Вывод

В ходе выполнения данной лабораторной работы я изучила идеологию и применение средств контроля версий и освоила умения по работе с git.

## {.standout}

