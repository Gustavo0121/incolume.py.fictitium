def download(tamanho, velocidade):
    """Calcula o tempo de download."""
    tamanho_mb = tamanho * 8
    tempo_download = tamanho_mb / velocidade
    tempo_sec = tempo_download / 60
    print(f"o tempo que esse arquivo baixará é de{tempo_sec: .2f}sec.")


tamanho = float(input("Qual o tamanho em MB para download?"))
velocidade = float(input("Qual a velocidade em Mbps do link de internet?"))
download(tamanho, velocidade)