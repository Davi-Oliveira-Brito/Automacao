import os
import xml.etree.ElementTree as ET
import re
import unicodedata
import datetime

# Data atual para uso no nome dos arquivos
data_atual = datetime.datetime.now()
mes = str(data_atual.month).zfill(2)
ano = data_atual.year

# Caminho da pasta com os arquivos (ajustável)
##pasta = f"T:/Arquivo XML/ANO {ano}/{mes}-{ano}/Autorizada/Recebidas/Ciente"
##pasta = f"T:/Arquivo XML/ANO 2025/06-2025/Autorizada/Recebidas/Ciente"
pasta = f"caminho da pasta"

# Remove caracteres inválidos e acentos
def limpar_nome(texto):
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')
    texto = re.sub(r'[\\/:*?"<>|]', '', texto)
    return texto.strip()

# Evita sobrescrever arquivos
def gerar_nome_unico(caminho):
    base, ext = os.path.splitext(caminho)
    contador = 1
    while os.path.exists(caminho):
        caminho = f"{base} ({contador}){ext}"
        contador += 1
    return caminho

# Processa os arquivos da pasta
for arquivo in os.listdir(pasta):
    if arquivo.lower().endswith('.xml'):
        caminho_xml = os.path.join(pasta, arquivo)
        nome_base = os.path.splitext(arquivo)[0]

        try:
            tree = ET.parse(caminho_xml)
            root = tree.getroot()
            ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

            nNF = root.find('.//nfe:infNFe/nfe:ide/nfe:nNF', ns)
            xNome = root.find('.//nfe:infNFe/nfe:emit/nfe:xNome', ns)

            if nNF is not None and xNome is not None:
                numero_nota = nNF.text.strip()
                fornecedor = limpar_nome(xNome.text)
                novo_nome_base = f"{fornecedor} - NF {numero_nota}"

                # Renomear XML
                novo_xml = gerar_nome_unico(os.path.join(pasta, f"{novo_nome_base}.xml"))
                os.rename(caminho_xml, novo_xml)

                # Renomear PDF se existir
                caminho_pdf = os.path.join(pasta, f"{nome_base}.pdf")
                if os.path.exists(caminho_pdf):
                    novo_pdf = gerar_nome_unico(os.path.join(pasta, f"{novo_nome_base}.pdf"))
                    os.rename(caminho_pdf, novo_pdf)

                print(f"Renomeado: {novo_nome_base}.(xml/pdf)")
            else:
                print(f"[AVISO] <nNF> ou <xNome> ausente em {arquivo}")
        except Exception as e:
            print(f"[ERRO] Falha ao processar {arquivo}: {e}")

print("Renomeação concluída.")
