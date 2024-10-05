import os

def deletar_artigos(caminho_base, lista_manter):
    # Normalizando os caminhos dos artigos a manter
    lista_manter = [os.path.join(caminho_base, item) for item in lista_manter]
    
    # Percorrendo todos os arquivos no diretório base
    for root, dirs, files in os.walk(caminho_base):
        for file in files:
            if file.endswith((".html", ".md")):
                caminho_completo = os.path.join(root, file)
                
                # Verificar se o caminho completo do arquivo está na lista de manutenção
                if not any(caminho_completo.startswith(keep) for keep in lista_manter):
                    print(f"Apagando: {caminho_completo}")
                    os.remove(caminho_completo)

# Exemplo de uso:
caminho_base = '/home/marcelo/Documentos/Projetos/g4g/content/'
artigos_manter = [
    "dicas-free-fire/nomes-de-anime-para-colocar-no-free-fire",
    "elden-ring/mapa/qual-o-tamanho-mapa-elden-ring",
    "sensibilidade/calculadora-de-sensibilidade",
    "arena-breakout/tarkov-para-celular",
    "arena-breakout/celular-bom-para-jogar-arena-breakout",
    "arena-breakout/10-dicas-para-se-dar-bem-no-arena-breakout",
    "arena-breakout/qual-o-melhor-mapa-para-se-lootear",
    "anime/naruto/nome-100-personagens-de-naruto",
    "noticias/hogwarts-legacy-mapa-interativo-online",
    "noticias/como-aumentar-a-capacidade-de-municao-em-lords-of-the-fallen",
    "gta-5-macetes/codigos-gta-5-cheats-e-macetes-para-xbox-360-ps3-ps4-e-xbox-one",
    "placa-de-video/rtx-4060-ti",
    "resident-evil-4-remake/qual-o-melhor-rifle",
    "noticias/nick-masculino-nick-free-fire",
    "noticias/onde-conseguir-sementes-de-vestigio-em-lords-of-the-fallen",
    "sensibilidade/qual-sensibilidade-eu-uso-em-cada-arma-no-free-fire",
    "noticias/as-melhores-armas-de-elden-ring",
    "arena-breakout/perguntas-frequentes",
    "fs22/os-melhores-mods-de-tratores-grandes-para-fs22",
    "arena-breakout/comparacao-grafica-lite-normal-ultra",
    "anime/naruto/todos-os-personagens",
    "sensibilidade",
    "noticias/uncharted-4-legacy-of-thieves-travando-no-pc-tela-inicial",
    "sensibilidade/para-celular-de-2gb-4gb-6gb-ram-no-free-fire",
    "noticias/elden-ring-teste-agora-mesmo-o-mapa-online-mostra-tudo-que-existe-no-jogo",
    "tags/free-fire",
    "en/free-fire/free-fire-redeem-code-ff-rewards-2023",
    "elden-ring/mapa/completo",
    "noticias/freefire/fotos-de-free-fire-papel-de-parede-celular",
    "noticias/roblox/blox-fruit-nivel-recomendado-das-ilhas",
    "noticias/freefire/manguezal-free-fire-aonde-fica",
    "noticias/freefire/novo-mapa-free-fire-chamado-nova-terra-tudo-que-voce-precisa-saber",
    "placa-de-video/rtx-3060",
    "noticias/roblox/codigos-marco-de-2023",
    "hogwarts-legacy/mapa-online-interativo-de-hogsmeade",
    "arena-breakout/3-dicas-para-iniciantes-no-arena-breakout",
    "noticias/jogador-de-elden-ring-encontra-a-pele-de-cobra-de-rykard",
    "gta-5-macetes/codigos-gta-5-xbox-360"
]

deletar_artigos(caminho_base, artigos_manter)
