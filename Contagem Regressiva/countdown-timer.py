import time #importação da biblioteca tempo

def countdown(t): #função countdown
    print('Countdown: \n')
    while t: # enquanto tiver 't' = tempo
        mins, secs = divmod(t, 60) # divisor
        timer = '{0}' ':' '{1}'.format(mins , secs) # formatação para o countdowcar
        print(timer, end="\r") # exibição do countdown
        time.sleep(1) # Intervalo
        t -= 1 #Regressão
        
    print('Tempo completo!') # Mensagem ao esgotar o tempo
        
t = int(input('Digite o tempo em segundos:\n')) # Entrada dos segundo desejados
countdown(t) # Chamada para função