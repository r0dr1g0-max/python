#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# whois.py3 CODIGOS

import socket
import whois

def desenho():
    print("\###################################################/")
    print(" \##########\ GARIMPEIRO /##########/")
    print("Enumerate_DNS [1]:")
    print("Consulta whois [2]")
    print("Scanner [3]:")

    print(" ")
    print("|-----------------------------------------------------|")
    n1 = input("|==>")

    if n1 == "1":
        def enumerate_dns():
            print("!\===========\  ->  Enumerate de DNS  <-  /===========/!")
            print("Example: google.com")
            print(" ")
            dominio = input("Digite um domínio: ")
            nomes = ["ns1", "ns2", "www", "ftp", "intranet"]
            print("loading...")
            def arquivo():
                with open("log.txt", "a") as dns:
                    return dns.write("\n#Aqui estão todos os nomes e dominios\n")

            arquivo()
            for nome in nomes:
                DNS = (nome + "." + dominio)
                try:
                    tudo = (DNS + ": " + socket.gethostbyname(DNS))
                    print(tudo)
                except socket.gaierror:
                    pass
                with open("log.txt", "a") as dns:
                    dns.write("\n")
                    dns.write(tudo)

            return print("Pronto!")
        enumerate_dns()

    elif n1 == "3":
        def scanner():
            print("!\==========\ ->  SCANNER_DE_PORTAS  <-  /==========/!")
            print("Example: 192.192.0.50")
            print(" ")
            host = input("Digite o ip: ")
            portas = [20, 21, 22, 23, 25, 53, 80, 110, 119, 143, 161, 443]

            print("loading...")

            for porta in portas:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                codigoRetorno = sock.connect_ex((host, porta))
                sock.close()
                if codigoRetorno == 0:
                    n = print(f"Esta porta está aberta: {porta}, neste IP: {host}")
                    if n == "":
                        print("erro")
                    else:
                        print("\==================> Obrigado! <=====================/")

        scanner()

    elif n1 == "2":
        def whos():
            print("!\===========\ ->  Consulta WHOIS  <- /===========/!")
            print("Example: teste.com.br")
            print(" ")
            dominio = input("Digite o domínio: ")
            print("loading...")
            consultaWhois = whois.whois(dominio)

            n1 = (consultaWhois.email)
            n2 = (consultaWhois["email"])
            n3 = (consultaWhois.text)

            with open("log.txt", "a") as arquivo:
                arquivo.write(n1)
                arquivo.write(n2)
                arquivo.write(n3)

            print(n1, n2, n3)
            print("Pronto!")

        whos()

    else:
        print("TypeError")


desenho()
