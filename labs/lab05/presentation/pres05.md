---
## Front matter
lang: ru-RU
title: Лабораторная работа No 5.
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

# Анализ файловой системы Linux. Команды для работы с файлами и каталогами

## Цель работы

Целью данной работы является ознакомление с файловой системой Linux, её структурой, именами и содержанием каталогов. Приобретение практических навыков по применению команд для работы с файлами и каталогами, по управлению процессами (и работами), по проверке использования диска и обслуживанию файловой системы.

# Выполнение лабораторной работы

## Копирование файла в текущем каталоге.

Выполняю все примеры, приведённые в первой части описания лабораторной работы.

![Копирование файла в текущем каталоге.](../report/image/lab05_1.png)

## Копирование файла в текущем каталоге.

![Копирование файла в текущем каталоге.](../report/image/lab05_2.png)

## Копирование нескольких файлов в каталог

![Копирование нескольких файлов в каталог.](../report/image/lab05_3.png)

## Копирование файлов в произвольном каталоге

![Копирование файлов в произвольном каталоге.](../report/image/lab05_4.png)

## Копирование каталогов в текущем каталоге

![Копирование каталогов в текущем каталоге.](../report/image/lab05_5.png)

## Копирование каталогов в произвольном каталоге

![Копирование каталогов в произвольном каталоге.](../report/image/lab05_6.png)

## Переименование файлов в текущем каталоге

![Переименование файлов в текущем каталоге.](../report/image/lab05_7.png)

## Перемещение файлов в другой каталог

![Перемещение файлов в другой каталог.](../report/image/lab05_8.png)

## Переименование каталогов в текущем каталоге

![Переименование каталогов в текущем каталоге.](../report/image/lab05_9.png)

## Перемещение каталога в другой каталог

![Перемещение каталога в другой каталог.](../report/image/lab05_10.png)

## Переименование каталога, не являющегося текущим

![Переименование каталога, не являющегося текущим.](../report/image/lab05_11.png)

## Требуется создать файл ~/may с правом выполнения для владельца u+x

![Требуется создать файл ~/may с правом выполнения для владельца u+x.](../report/image/lab05_12.png)

## Требуется лишить владельца файла ~/may права на выполнение

![Требуется лишить владельца файла ~/may права на выполнение.](../report/image/lab05_13.png)

## Требуется создать каталог monthly с запретом на чтение для членов группы и всех остальных пользователей

![Требуется создать каталог monthly с запретом на чтение для членов группы и всех остальных пользователей.](../report/image/lab05_14.png)

## Требуется создать файл ~/abc1 с правом записи для членов группы

![Требуется создать файл ~/abc1 с правом записи для членов группы.](../report/image/lab05_15.png)

## Требуется создать файл ~/abc1 с правом записи для членов группы

![Требуется создать файл ~/abc1 с правом записи для членов группы.](../report/image/lab05_16.png)

## Выполню следующие действия, зафиксировав в отчёте по лабораторной работе используемые при этом команды и результаты их выполнения.

Скопирую файл /usr/include/sys/io.h в домашний каталог и назову его equipment. Если файла io.h нет, то использую любой другой файл в каталоге /usr/include/sys/ вместо него.

## Скопирую файл /usr/include/sys/io.h в домашний каталог

![Скопирую файл /usr/include/sys/io.h в домашний каталог.](../report/image/lab05_17.png)

## Назову его equipment

![Назову его equipment.](../report/image/lab05_18.png)

## В домашнем каталоге создам директорию ~/ski.plases

В домашнем каталоге создам директорию ~/ski.plases.

![В домашнем каталоге создам директорию ~/ski.plases.](../report/image/lab05_19.png)

## Переместим файл equipment в каталог ~/ski.plases.

Переместим файл equipment в каталог ~/ski.plases.

![Переместим файл equipment в каталог ~/ski.plases.](../report/image/lab05_20.png)

## Создам в домашнем каталоге файл abc1 и скопирую его в каталог ~/ski.plases, назову его equiplist2

Переименую файл ~/ski.plases/equipment в ~/ski.plases/equiplist. Создам в домашнем каталоге файл abc1 и скопирую его в каталог ~/ski.plases, назову его equiplist2.

![Создам в домашнем каталоге файл abc1 и скопирую его в каталог ~/ski.plases, назову его equiplist2.](../report/image/lab05_21.png)

## Создам каталог с именем equipment в каталоге ~/ski.plases

Создам каталог с именем equipment в каталоге ~/ski.plases.

![Создам каталог с именем equipment в каталоге ~/ski.plases.](../report/image/lab05_22.png)

## Переместим файлы ~/ski.plases/equiplist и equiplist2 в каталог ~/ski.plases/equipment

Переместим файлы ~/ski.plases/equiplist и equiplist2 в каталог ~/ski.plases/equipment.

![Переместим файлы ~/ski.plases/equiplist и equiplist2 в каталог ~/ski.plases/equipment.](../report/image/lab05_23.png)

## Создам и перемещу каталог ~/newdir в каталог ~/ski.plases и назову его plans

Создам и перемещу каталог ~/newdir в каталог ~/ski.plases и назову его plans.

![Создам и перемещу каталог ~/newdir в каталог ~/ski.plases и назову его plans.](../report/image/lab05_24.png)

## Определю опции команды chmod, необходимые для того, чтобы присвоить файлам выделенные права доступа, считая, что в начале таких прав нет

Присвою выделенные права доступа каталогу australia.

![Присвою выделенные права доступа каталогу australia.](../report/image/lab05_25.png)

## Присвою выделенные права доступа каталогу australia

![Присвою выделенные права доступа каталогу australia.](../report/image/lab05_26.png)

## Присвою выделенные права доступа каталогу play

Присвою выделенные права доступа каталогу play.

![Присвою выделенные права доступа каталогу play.](../report/image/lab05_27.png)

## Присвою выделенные права доступа каталогу play

![Присвою выделенные права доступа каталогу play.](../report/image/lab05_28.png)

## Присвою выделенные права доступа файлу my_os

Присвою выделенные права доступа файлу my_os.

![Присвою выделенные права доступа файлу my_os.](../report/image/lab05_29.png)

## Присвою выделенные права доступа файлу my_os

![Присвою выделенные права доступа файлу my_os.](../report/image/lab05_30.png)

## Присвою выделенные права доступа файлу feathers

Присвою выделенные права доступа файлу feathers.

![Присвою выделенные права доступа файлу feathers.](../report/image/lab05_31.png)

## Присвою выделенные права доступа файлу feathers

![Присвою выделенные права доступа файлу feathers.](../report/image/lab05_32.png)

## Проделаю приведённые ниже упражнения, записывая в отчёт по лабораторной работе используемые при этом команды

При помощи команды cat просмотрю содержимое файла /etc/passwd.

![При помощи команды cat просмотрю содержимое файла /etc/passwd.](../report/image/lab05_33.png)

## При помощи команды cp скопирую файл ~/feathers в файл ~/file.old

При помощи команды cp скопирую файл ~/feathers в файл ~/file.old.

![При помощи команды cp скопирую файл ~/feathers в файл ~/file.old.](../report/image/lab05_34.png)

## При помощи команды mv перемещу файл ~/file.old в каталог ~/play

При помощи команды mv перемещу файл ~/file.old в каталог ~/play.

![При помощи команды mv перемещу файл ~/file.old в каталог ~/play.](../report/image/lab05_35.png)

## При помощи команды cp скопирую каталог ~/play в каталог ~/fun

При помощи команды cp скопирую каталог ~/play в каталог ~/fun.

![При помощи команды cp скопирую каталог ~/play в каталог ~/fun.](../report/image/lab05_36.png)

## При помощи команды mv перемещу каталог ~/fun в каталог ~/play и назову его games

При помощи команды mv перемещу каталог ~/fun в каталог ~/play и назову его games.

![При помощи команды mv перемещу каталог ~/fun в каталог ~/play и назову его games.](../report/image/lab05_37.png)

## Лишу владельца файла ~/feathers права на чтение. 

Лишу владельца файла ~/feathers права на чтение.

![Лишу владельца файла ~/feathers права на чтение.](../report/image/lab05_38.png)

## Вот что произойдёт, если я попытаюсь просмотреть файл ~/feathers командой cat.

Вот что произойдёт, если я попытаюсь просмотреть файл ~/feathers командой cat.

![Вот что произойдёт, если я попытаюсь просмотреть файл ~/feathers командой cat.](../report/image/lab05_39.png)

## Вот что произойдёт, если я попытаюсь скопировать файл ~/feathers.

Вот что произойдёт, если я попытаюсь скопировать файл ~/feathers.

![Вот что произойдёт, если я попытаюсь скопировать файл ~/feathers.](../report/image/lab05_40.png)

## Дам владельцу файла ~/feathers право на чтение

Дам владельцу файла ~/feathers право на чтение.

![Дам владельцу файла ~/feathers право на чтение.](../report/image/lab05_41.png)

## Лишу владельца каталога ~/play права на выполнение

Лишу владельца каталога ~/play права на выполнение.

![Лишу владельца каталога ~/play права на выполнение.](../report/image/lab05_42.png)

## Перейду в каталог ~/play. Вот что произошло.

Перейду в каталог ~/play. Вот что произошло.

![Перейду в каталог ~/play. Вот что произошло.](../report/image/lab05_43.png)

## Дам владельцу каталога ~/play право на выполнение.

Дам владельцу каталога ~/play право на выполнение.

![Дам владельцу каталога ~/play право на выполнение.](../report/image/lab05_44.png)

## Прочитаю man по командам mount, fsck, mkfs, kill.

Прочитаю man по командам mount, fsck, mkfs, kill.

![Прочитаю man по команде mount.](../report/image/lab05_45.png)

## Прочитаю man по команде fsck

![Прочитаю man по команде fsck.](../report/image/lab05_46.png)

## Прочитаю man по команде mkfs

![Прочитаю man по команде mkfs.](../report/image/lab05_47.png)

## Прочитаю man по команде kill

![Прочитаю man по команде kill.](../report/image/lab05_48.png)

## Вывод

В ходе выполнения данной лабораторной работы я провела ознакомление с файловой системой Linux, её структурой, именами и содержанием каталогов. Приобрела практические навыки по применению команд для работы с файлами и каталогами, по управлению процессами (и работами), по проверке использования диска и обслуживанию файловой системы.