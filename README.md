[![Actions Status](https://github.com/yulia-sa/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/yulia-sa/python-project-lvl1/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9041ce594419613b4760/maintainability)](https://codeclimate.com/github/yulia-sa/python-project-lvl1/maintainability)
[![Python CI](https://github.com/yulia-sa/python-project-lvl1/actions/workflows/pyci.yml/badge.svg)](https://github.com/yulia-sa/python-project-lvl1/actions)


# Игры разума

Набор из 5 простых консольных арифметических игр.

## Предварительная установка

Для запуска предварительно потребуется установить: 
1. Python версии 3.6+
1. Pip3 версии 19+
1. Poetry версии 1.0.0 или выше. Нужно настроить Poetry так, чтобы тот создавал виртуальные окружения в директории проекта (poetry config virtualenvs.in-project true).

## Установка пакета из локального окружения

1. Склонировать репозиторий.
1. Из корня репозитория:
    * выполнить установку окружения командой _make install_,
    * затем собрать пакет игр командой _make build_ (будет создана директория /dist с файлами пакетов *.whi и *.gz),
    * установить пакет из локального окружения (директории /dist) командой _make package-install_.

## Запуск игр

### 1. Игра «Проверка на чётность»
Запускается командой _brain-even_  
[![asciicast](https://asciinema.org/a/GlUO4xUdnZPjKdyNsBHvAIHQS.svg)](https://asciinema.org/a/GlUO4xUdnZPjKdyNsBHvAIHQS?t=2)

### 2. Игра «Калькулятор»
Запускается командой _brain-calc_  
[![asciicast](https://asciinema.org/a/wok2ZXG573myNkRCjgiNWwM10.svg)](https://asciinema.org/a/wok2ZXG573myNkRCjgiNWwM10?t=2)

### 3. Игра «Наибольший общий делитель»
Запускается командой _brain-gcd_  
[![asciicast](https://asciinema.org/a/cX7hupMxJJSv7j1aKGIGIlpt5.svg)](https://asciinema.org/a/cX7hupMxJJSv7j1aKGIGIlpt5?t=2)

### 4. Игра «Арифметическая прогрессия»
Запускается командой _brain-progression_  
[![asciicast](https://asciinema.org/a/PkNsnLWPQKBhc0PBOos15gVyz.svg)](https://asciinema.org/a/PkNsnLWPQKBhc0PBOos15gVyz?t=2)

### 5. Игра «Простое ли число?»
Запускается командой _brain-prime_  
[![asciicast](https://asciinema.org/a/oiLPeVdwSJGUAzwCFsioDa3N0.svg)](https://asciinema.org/a/oiLPeVdwSJGUAzwCFsioDa3N0?t=2)

# Цели проекта

Проект выполнен в учебных целях.
