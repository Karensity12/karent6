# -*- coding: utf-8 -*-
"""Trabajo clase 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h4FtRCbxPr8XQawWXFfMHVMX6BKr7iTh
"""

A=int(input("Ingrese el primer digito"))
B=int(input("Ingrese el segundo digito"))
ACUMULADOR=0

while True:
  ACUMULADOR+=A
  B-=1

if B==0:
  print(ACUMULADOR)
break

