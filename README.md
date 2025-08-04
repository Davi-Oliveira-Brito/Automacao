# 📄 Renomeador de XML e PDF de Notas Fiscais

Este script em Python automatiza o processo de **renomear arquivos XML e PDF de notas fiscais eletrônicas**. Ele extrai o nome do fornecedor e o número da nota do XML, e renomeia os arquivos com base nessas informações.

---

## ⚙️ Como funciona

1. Lê todos os arquivos `.xml` de uma **pasta específica**.
2. Extrai os campos:
   - **xNome** (nome do fornecedor)
   - **nNF** (número da nota)
3. Cria um nome no formato:
   ```
   Nome do Fornecedor - NF 12345
   ```
4. Renomeia o XML e, se houver, o PDF com o mesmo nome base.
5. Garante que não haja sobrescrita de arquivos (usa "(1)", "(2)", etc.).

---

## 🧠 Pré-requisitos

- Python 3 instalado  
- Biblioteca padrão (não usa pacotes externos)

---

## 🛠️ Como usar

1. Clone o repositório ou baixe o arquivo `.py`:

```bash
git clone https://github.com/Davi-Oliveira-Brito/Automacao.git
cd Automacao
```

2. Edite o caminho da pasta no código:

```python
pasta = f"caminho da pasta"
```

> Exemplo real:

```python
pasta = f"T:/Arquivo XML/ANO 2025/08-2025/Autorizada/Recebidas/Ciente"
```

3. Execute o script:

```bash
python renomear_nfe.py
```

---

## 📝 Exemplo de renomeação

Se houver um XML chamado:

```
nota_0001.xml
```

E ele contiver:
- `xNome = "ACME Ltda"`
- `nNF = "12345"`

O arquivo será renomeado para:

```
ACME Ltda - NF 12345.xml
```

Se houver um PDF com mesmo nome base (`nota_0001.pdf`), ele também será renomeado para:

```
ACME Ltda - NF 12345.pdf
```

---

## 🛡️ Observações

- O script ignora XMLs com campos ausentes (`xNome` ou `nNF`).
- Arquivos duplicados recebem um sufixo numérico: `(1)`, `(2)`, etc.
- A acentuação e caracteres inválidos são removidos do nome final.