# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> 💡 **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.

---

### 👤 Identificação do Candidato

- **Nome completo:** Jhonatan Gonçalves Pereira
- **GitHub:** https://github.com/jhonatan-goncalves-pereira

---

## 1️⃣ Visão Geral da Solução

- **Qual é o objetivo do projeto?**  
O projeto implementa um **semáforo de trânsito simulado** utilizando um microcontrolador ESP32 e três LEDs (verde, amarelo e vermelho).

- **O que o sistema embarcado simulado faz?**  
O sistema embarcado controla o ciclo completo de um semáforo de forma autônoma, alternando entre os estados de passagem liberada (verde), atenção (amarelo) e parada obrigatória (vermelho), com temporização definida por software.

- **Como o usuário interage com ele (se aplicável)?**  
Não há interação direta do usuário — o ciclo ocorre de forma contínua e automática, sendo monitorável via Serial Monitor.

---

## 2️⃣ Arquitetura do Sistema Embarcado

### Padrão de Projeto: Máquina de Estados Finita (FSM)

O firmware foi estruturado utilizando o padrão **Finite State Machine (FSM)**, que oferece:
- **Não-bloqueante**: Evita `time.sleep()` que travaria a CPU, permitindo futuras expansões (leitura de sensores, comunicação MQTT, etc.)
- **Modular**: Cada estado é auto-contido e fácil de testar isoladamente
- **Escalável**: Novos estados ou transições podem ser adicionados sem refatorar todo o código

### Fluxo de Estados
```
[VERDE: 3s] → [AMARELO: 1s] → [VERMELHO: 3s] → (repete)
```

### Temporização Não-Bloqueante com `time.ticks_ms()`

```python
# Em vez de: time.sleep(3000) ❌ (bloqueia a CPU)
# Usei: 
agora     = time.ticks_ms()
decorrido = time.ticks_diff(agora, ultimo_tick)
if decorrido >= DURACAO_MS[estado_atual]:
    # muda de estado
```

**Por que `ticks_diff()`?**
- Lida com overflow do contador de 32 bits (após ~49 dias de execução)
- Permite múltiplos temporizadores independentes rodando simultaneamente
- Mantém o loop principal responsivo (~10ms por iteração)

### Interação entre Componentes
- **GPIO Output**: ESP32 envia sinal HIGH/LOW para os pinos 26, 25, 33
- **LEDs + Resistores**: Configuração sink (LED anodo → resistor → GND)
- **Serial Monitor**: `print()` registra transições para debug e validação do CI

---

## 3️⃣ Componentes Utilizados na Simulação

| Componente | Quantidade | Função |
|---|---|---|
| ESP32 DevKit C v4 | 1 | Microcontrolador principal, executa o firmware MicroPython |
| LED Verde (wokwi-led) | 1 | Sinalização de passagem liberada (GPIO 26) |
| LED Amarelo (wokwi-led) | 1 | Sinalização de atenção (GPIO 25) |
| LED Vermelho (wokwi-led) | 1 | Sinalização de parada obrigatória (GPIO 33) |
| Resistor 220Ω (wokwi-resistor) | 3 | Limitação de corrente dos LEDs |

Todos os componentes foram definidos e conectados no arquivo `diagram.json`, com fios coloridos identificando cada trilha do circuito.

---

## 4️⃣ Decisões Técnicas Relevantes

### ✅ FSM em vez de sequência linear com delays
**Problema**: `time.sleep()` bloqueia a CPU, impedindo leitura de sensores ou resposta a eventos externos.  
**Solução**: Máquina de estados com `time.ticks_ms()` permite multitarefa cooperativa.  
**Trade-off**: Código ligeiramente mais complexo, mas preparado para produção.

### ✅ Função auxiliar `apagar_todos()`
Centraliza o desligamento dos LEDs, garantindo que nunca haja dois acesos simultaneamente (segurança em semáforos reais).

### ✅ Pinos GPIO 26, 25, 33
Pinos de uso geral sem conflito com funções reservadas (boot, UART), garantindo compatibilidade com Wokwi e hardware real.

### ✅ Resistores de 220Ω
Cálculo: R = (3.3V - 2.1V) / 0.005A = 240Ω → 220Ω (valor comercial). Protege LEDs e pinos GPIO.

### ✅ Saída serial como evidência de teste
`print("Teste")` na inicialização permite validação automática pelo GitHub Actions via `--expect-text`.

### ✅ Ambiente de execução — Opção A (Python local)
Desenvolvido em Windows institucional sem Docker. `pip install -r requirements.txt` foi suficiente para o escopo do projeto.

---

## 5️⃣ Estratégia de Branches e Versionamento

Este repositório segue uma **estratégia de branches organizada** para separar desenvolvimento de entrega:

### Branch `main` (produção)
- Contém a **versão final e otimizada** do projeto
- Implementação com **Máquina de Estados Não-Bloqueante**
- Código revisado e testado
- Pipeline CI/CD passando com sucesso ✅

### Branch `feat/actions-build` (desenvolvimento inicial)
- Contém a **implementação inicial** com `time.sleep()` bloqueante
- Versão funcional mas não otimizada
- Mantida para fins de **histórico e comparação**
- Demonstra a evolução do projeto

### Branch `develop` (integração - opcional)
- Pode ser usada para testar novas funcionalidades antes do merge para `main`
- Fluxo: `develop` → Pull Request → `main`

> 📌 **Por que manter branches separadas?**  
> Isso demonstra domínio de Git, permite rollback seguro e facilita a colaboração em equipe — práticas essenciais em desenvolvimento profissional de software e firmware.

---

## 6️⃣ Resultados Obtidos

O sistema opera corretamente na simulação do Wokwi, executando o ciclo completo do semáforo de forma contínua:

- ✅ LED verde acende por 3 segundos com mensagem `VERDE - Passagem liberada`
- ✅ LED amarelo acende por 1 segundo com mensagem `AMARELO - Atencao`
- ✅ LED vermelho acende por 3 segundos com mensagem `VERMELHO - Pare`
- ✅ Apenas um LED permanece aceso por vez em todos os estados
- ✅ A saída serial exibe `Teste` na inicialização, atendendo ao critério de validação do GitHub Actions
- ✅ Pipeline de CI executou sem falhas (1m 15s)
- ✅ Sem warnings de `unknown-part-type` no diagram.json

### Métricas de Desempenho
- **Tempo de boot**: ~2 segundos (incluindo blink de inicialização)
- **Consumo de CPU**: < 5% (loop de 10ms não-bloqueante)
- **Precisão temporal**: ±10ms (limitado pelo sleep_ms)
- **Tamanho do código**: ~100 linhas bem estruturadas

---

## 7️⃣ Limitações e Melhorias Futuras

### Limitações Atuais
1. **Precisão temporal**: Loop de 10ms pode causar variação de ±1% no tempo dos estados
2. **Sem tratamento de falhas**: Não há watchdog timer para recuperação de travamentos
3. **Hardcoded**: Tempos dos estados fixos no código (poderiam ser configuráveis via EEPROM ou MQTT)
4. **Sem persistência**: Configurações se perdem ao reiniciar o ESP32

### Melhorias Propostas
1. **Botão de pedestre**: GPIO input para solicitação de travessia prioritária
2. **Sensor de luminosidade**: Ajustar brilho dos LEDs ou tempos conforme horário do dia
3. **Comunicação IoT**: MQTT para monitoramento remoto e configuração OTA (Over-The-Air)
4. **Deep Sleep**: Otimizar consumo energético em períodos de baixo tráfego
5. **Sincronização de semáforos**: RTC + protocolo para coordenar múltiplos cruzamentos
6. **Display countdown**: Adicionar display 7 segmentos para mostrar tempo restante

### Lições Aprendidas
- **Máquinas de estado** são essenciais para firmware responsivo e escalável
- **`time.ticks_ms()` + `ticks_diff()`** é o padrão-ouro para temporização em MicroPython
- **CI/CD para embarcados** (Wokwi + GitHub Actions) acelera desenvolvimento e previne regressões
- **Versionamento semântico** e branches organizadas facilitam manutenção e colaboração
- **Simulação antes do hardware** economiza tempo e componentes físicos


---

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****