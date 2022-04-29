---
## Front matter
lang: ru-RU
title: Лабораторная работа No 4.
author: |
	Анастасия Павловна Баранова, НБИбд-01-21\inst{1}
institute: |
	\inst{1}Российский Университет Дружбы Народов
date: 29 апреля, Москва, 2022 г.

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

# Основы интерфейса взаимодействия пользователя с системой Unix на уровне командной строки

## Цель работы

Целью данной работы является приобретение практических навыков взаимодействия пользователя с системой посредством командной строки.

# Выполнение лабораторной работы

## Определение полного имени домашнего каталога.

Определяю полное имя моего домашнего каталога. Далее относительно этого каталога будут выполняться последующие упражнения.

![Определение полного имени домашнего каталога.](../report/image/04_1.png)

## Переход в каталог /tmp.

Перейду в каталог /tmp.

![Переход в каталог /tmp.](../report/image/04_2.png)

## Вывод на экран содержимого каталога /tmp.

Выведу на экран содержимое каталога /tmp. Для этого использую команду ls с различными опциями. С помощью команды ls -a выведу на экран содержимое каталога включая скрытые файлы.

![Вывод содержимого каталога включая скрытые файлы.](../report/image/04_3.png)

## Вывод подробной информации о файлах и каталогах.

С помощью команды ls -l выведу на экран подробную информацию о файлах и каталогах.

![Вывод подробной информации о файлах и каталогах.](../report/image/04_4.png)

## Вывод содержимого и подробной информации о файлах и каталогах.

С помощью команды ls -alF выведу на экран содержимое каталога включая скрытые файлы, подробную информацию о файлах и каталогах, информацию о типах файлов.

![Вывод содержимого и подробной информации о файлах и каталогах.](../report/image/04_5.png)

## Проверка.

Определю, есть ли в каталоге /var/spool подкаталог с именем cron. Подкаталог с именем cron существует.

![Проверка, есть ли в каталоге /var/spool подкаталог с именем cron.](../report/image/04_6.png)

## Вывод на экран содержимого домашнего каталога.

Перейду в мой домашний каталог и выведу на экран его содержимое. Определю, кто является владельцем файлов и подкаталогов. Владельцем почти всех файлов и каталогов является мой пользователь anastasia, кроме одного каталога, владельцем которого является root (суперпользователь).

![Вывод на экран содержимого домашнего каталога.](../report/image/04_7.png)

## Создание каталога newdir.

В домашнем каталоге создам новый каталог с именем newdir.

![Создание каталога newdir.](../report/image/04_8.png)

## Создание каталога morefun.

В каталоге ~/newdir создам новый каталог с именем morefun.

![Создание каталога morefun.](../report/image/04_9.png)

## Создание трёх каталогов одной командой.

В домашнем каталоге создам одной командой три новых каталога с именами letters, memos, misk. Затем удалю эти каталоги одной командой.

![Создание трёх каталогов одной командой.](../report/image/04_10.png)

## Удаление трёх каталогов одной командой.

![Удаление трёх каталогов одной командой.](../report/image/04_11.png)

## Попытка удалить каталог ~/newdir.

Попробую удалить ранее созданный каталог ~/newdir командой rm. Проверю, был ли каталог удалён. Удаление каталога ~/newdir командой rm невозможно.

![Попытка удалить каталог ~/newdir.](../report/image/04_12.png)

## Успешное удаление каталога ~/newdir.

Удалю каталог ~/newdir/morefun из домашнего каталога с помощью команды rm -r. Проверю, был ли каталог удалён.

![Успешное удаление каталога ~/newdir.](../report/image/04_13.png)

## Выполнение команды man.

С помощью команды man определю, какую опцию команды ls нужно использовать для просмотра содержимого не только указанного каталога, но и подкаталогов, входящих в него. Это опция -R.

![Выполнение команды man.](../report/image/04_14.png)

## Опция команды ls для просмотра содержимого.

![Опция команды ls для просмотра содержимого.](../report/image/04_15.png)

## Выполнение команды man.

С помощью команды man определю набор опций команды ls, позволяющий отсортировать по времени последнего изменения выводимый список содержимого каталога с развёрнутым описанием файлов. Эти опции -l и -t.

![Выполнение команды man.](../report/image/04_16.png)

## Опция -l.

![Опция -l.](../report/image/04_17.png)

## Опция -t.

![Опция -t.](../report/image/04_18.png)

## Невозможно узнать подробнее об опциях команды cd.

Использую команду man для просмотра описания следующих команд: cd, pwd, mkdir, rmdir, rm. Поясню основные опции этих команд.

![Невозможно узнать подробнее об опциях команды cd.](../report/image/04_19.png)

## Выполнение команды man.

![Выполнение команды man.](../report/image/04_20.png)

## Основные опции команды pwd.

![Основные опции команды pwd.](../report/image/04_21.png)

## Выполнение команды man.

![Выполнение команды man.](../report/image/04_22.png)

## Основные опции команды mkdir.

![Основные опции команды mkdir.](../report/image/04_23.png)

## Выполнение команды man.

![Выполнение команды man.](../report/image/04_24.png)

## Основные опции команды rmdir.

![Основные опции команды rmdir.](../report/image/04_25.png)

## Выполнение команды man.

![Выполнение команды man.](../report/image/04_26.png)

## Основные опции команды rm.

![Основные опции команды rm.](../report/image/04_27.png)

## Выполнение команды history.

Используя информацию, полученную при помощи команды history, выполню модификацию и исполнение нескольких команд из буфера команд.

![Выполнение команды history.](../report/image/04_28.png)

## Модификация команды ls -al.

Модификация команды ls -al.

![Модификация команды ls -al.](../report/image/04_29.png)

## Модификация команды ls -a.

Модификация команды ls -a.

![Модификация команды ls -a.](../report/image/04_30.png)

## Вывод

В ходе выполнения данной лабораторной работы я приобрела практические навыки взаимодействия пользователя с системой по-
средством командной строки.