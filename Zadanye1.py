#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит на экран все его
# предложения в обратном порядке

if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.read().split()
    i = len(text) - 1
    while i >= 0:
        print(text[i])
        i -= 1