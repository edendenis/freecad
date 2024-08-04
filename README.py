#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar o `FreeCAD` no Linux Ubuntu
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `FreeCAD` no Linux Ubuntu.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install the `FreeCAD` on Linux Ubuntu._

# ## Descrição [2]
# 
# `FreeCAD`
# 
# O `FreeCAD` é uma poderosa e versátil plataforma de modelagem paramétrica 3D de código aberto, projetada principalmente para o design e modelagem de peças e conjuntos em engenharia mecânica e design de produtos. Com uma interface de usuário intuitiva e uma ampla gama de recursos, o `FreeCAD` permite criar modelos 3D precisos e detalhados. Ele suporta a criação de sólidos, superfícies, esboços 2D e montagens complexas, tornando-o uma ferramenta valiosa para projetistas, engenheiros e entusiastas de CAD. Além disso, o `FreeCAD` é altamente personalizável e possui uma comunidade ativa de desenvolvedores e usuários que contribuem com extensões e módulos para estender ainda mais sua funcionalidade, o que o torna uma opção popular para modelagem 3D no mundo do código aberto.
# 
# Add-in `Modern UI` [2]
# 
# O `ModernUI` é uma interface de usuário alternativa para o `FreeCAD`, uma plataforma de modelagem 3D de código aberto. O `ModernUI` oferece uma abordagem de interface mais moderna e simplificada em comparação com a interface de usuário padrão do `FreeCAD`, projetada para tornar a experiência do usuário mais amigável e eficiente. Ele apresenta ícones e layouts de menus atualizados, bem como uma organização mais intuitiva das ferramentas e comandos, tornando mais fácil para os usuários acessar e navegar pelas funcionalidades do `FreeCAD`. O `ModernUI` é uma opção atraente para aqueles que preferem uma interface de usuário mais contemporânea e amigável, e oferece uma alternativa à interface de usuário padrão do `FreeCAD`, permitindo aos usuários escolher a que melhor se adapta às suas preferências e fluxos de trabalho.
# 
# Add-in `A2plus` [2]
# 
# A extensão `"A2Plus"` no `FreeCAD` é um módulo que permite a importação e edição de arquivos no formato de montagem Assembly 2 para criar conjuntos de peças complexos em projetos CAD. Essa extensão é particularmente útil para designers e engenheiros que trabalham em projetos que envolvem múltiplas peças e montagens, permitindo que eles criem e gerenciem montagens complexas com facilidade. Com o `A2Plus`, os usuários podem importar peças existentes, posicionar e alinhar essas peças em relação umas às outras, criar restrições e relações entre elas e, assim, criar montagens mais elaboradas dentro do ambiente do `FreeCAD`. Essa extensão aprimora a funcionalidade do `FreeCAD`, tornando-o uma ferramenta mais poderosa para o design e a modelagem paramétrica de montagens mecânicas.
# 
# `Path Workbench` [2]
# 
# O `Path Workbench` (ou Workbench de Caminho) é um dos ambientes de trabalho no `FreeCAD`, um software de modelagem 3D de código aberto. O Path Workbench é projetado para lidar com tarefas relacionadas à criação de trajetórias de ferramentas para máquinas CNC (Controle Numérico Computadorizado). Ele permite aos usuários gerar caminhos de ferramentas para usinagem CNC, incluindo fresamento e corte, definindo trajetórias e operações de usinagem para criar peças de trabalho precisas. O Path Workbench oferece ferramentas para criar geometria de corte, configurar parâmetros de usinagem, simular a usinagem e gerar código G para máquinas CNC. É uma ferramenta valiosa para engenheiros e projetistas que trabalham com fabricação CNC, permitindo a criação e a otimização de caminhos de ferramentas para produzir peças com precisão a partir de modelos 3D no `FreeCAD`.

# ## 1. Como configurar/instalar/usar o `FreeCAD` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `FreeCAD`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. Instale o `FreeCAD` usando o comando a seguir: `sudo apt install freecad -y`
# 
#     Aguarde o processo de instalação ser concluído. O sistema irá baixar e instalar o `FreeCAD` e suas dependências.
# 
# 4. Após a instalação, você pode abrir o `FreeCAD` a partir do menu de aplicativos do `Linux Ubuntu` ou executando o seguinte comando no `Terminal Emulator`: `freecad`
# 
# Agora, o `FreeCAD` estará instalado e pronto para uso no seu sistema `Linux Ubuntu`.
# 

# ### 1.1 Codigo completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `FreeCAD` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install freecad -y
#     ```
# 

# ## 2 Ativar o `ModerUI` no `FreeCAD` [3]
# 
# Para ativar o `ModerUI` no `FreeCAD`, você precisa seguir alguns passos simples. O `ModerUI` é um ambiente de trabalho (_workbench_) que proporciona uma interface mais moderna e simplificada para o `FreeCAD`. Aqui estão os passos para ativá-lo:
# 
# 1. **Abra o `FreeCAD`:** Inicie o `FreeCAD` no seu computador.
# 
# 2. **Verifique se o `ModerUI` está instalado:** O `ModerUI` pode **NÃO** estar pré-instalado no `FreeCAD`. Para verificar isso, vá até a barra de menu e clique em:
#     
#     2.1 `"View"` > `"Workbenche"` (ou `"Ambiente de Trabalho"`).
#     
#     Se o `ModerUI` estiver na lista, você pode pular o passo 3.
# 
# 3. **Instale o `ModerUI` (se necessário):** Se o `ModerUI` **NÃO** estiver na lista de ambientes de trabalho, você precisará instalá-lo. Para isso:
# 
#     3.1 Vá até o menu `Tools` (ou `Ferramentas`);
#     
#     3.2 `Addon Manager` (ou `Gerenciador de Complementos`).
#     
#     3.3 Procure por `ModerUI` na lista de complementos disponíveis e clique em `Install` (`Instalar`).
# 
# 4. **Ative o ModerUI:** Após a instalação, você pode ativar o `ModerUI`. Vá novamente até a barra de menu, clique em: `"Ver" > "Ambientes de Trabalho" e selecione "ModerUI"`.
# 
# 5. **Explore a nova interface:** Com o `ModerUI` ativado, você notará uma mudança na interface do `FreeCAD`, com uma aparência mais moderna e talvez um conjunto diferente de ferramentas e opções disponíveis.
# 
# Lembre-se de que as versões do `FreeCAD` e dos complementos podem variar, então os passos exatos podem ser um pouco diferentes dependendo da versão que você está usando. Se tiver dificuldades, consulte a documentação do `FreeCAD` ou fóruns da comunidade para obter ajuda específica para a sua versão.
# 

# ## 3. Ativar o `A2plus` no `FreeCAD` [4]
# 
# Para ativar o `A2plus` no `FreeCAD`, você precisa seguir alguns passos simples. O `A2plus` é um workbench (bancada de trabalho) dentro do `FreeCAD` que permite o trabalho com montagens mecânicas. Aqui está o processo:
# 
# 1. **Instalação do `A2plus`:** Primeiro, certifique-se de que o `FreeCAD` esteja instalado no seu computador.
# 
#     1.1 Abra o `FreeCAD`.
# 
#     1.2 Vá até o menu `Tools` e selecione `Addon Manager`.
# 
#     1.3 Na janela do `Addon Manager`, procure por `A2plus` na lista de workbenches disponíveis.
# 
#     1.4 Clique em `A2plus` e depois no botão Instalar.
# 
#     1.5 Aguarde a conclusão da instalação e reinicie o `FreeCAD`.
# 
# 2. **Ativação do `A2plus`:**
# 
#     2.1 Após reiniciar o `FreeCAD`, clique no menu de seleção de workbenches (geralmente localizado no canto superior direito da janela do `FreeCAD`, com um ícone de uma pequena casa ou uma lista de ícones).
# 
#     2.2 Selecione `A2plus` na lista de workbenches disponíveis.
# 
#     Com isso, o workbench `A2plus` será ativado e você poderá começar a usar suas funcionalidades para montagens.
# 
# 3. **Utilização do `A2plus`:**
# 
#     3.1 Com o `A2plus` ativo, você terá acesso a várias ferramentas específicas para montagem de peças.
# 
#     3.2 Explore as ferramentas disponíveis na barra de ferramentas do `A2plus` para começar a montar suas peças.
# 
#     3.3 Caso encontre algum problema durante a instalação ou a utilização do `A2plus`, consulte a documentação do FreeCAD ou fóruns da comunidade para obter ajuda adicional.

# ## 4. `Path Workbench`
# 
# Para habilitar e usar o `Path Workbench` no `FreeCAD`, siga os passos abaixo. Vou assumir que você já tem o `FreeCAD` instalado no seu sistema. Se não tiver, você precisará instalar o `FreeCAD` primeiro.
# 
# **Passos para Habilitar o `Path Workbench` no `FreeCAD`**
# 
# 1. **Abrir o `FreeCAD`:** Inicie o `FreeCAD` no seu computador.
# 
# 2. **Selecionar o `Path Workbench`:**
# 
#     - Na interface do `FreeCAD`, você encontrará uma barra de menu na parte superior ou uma lista de _workbenches_ na lateral (a disposição pode variar dependendo da versão do `FreeCAD` e das suas configurações de interface).
# 
#     - Procure pelo ícone do `Path Workbench`, que geralmente tem um símbolo de uma ferramenta de corte ou um caminho de ferramenta. O ícone pode ser encontrado na lista de workbenches disponíveis.
# 
#     - Clique no ícone do `Path Workbench` para ativá-lo.
# 
# 3. **Familiarize-se com a Interface:**
# 
#     - Uma vez no `Path Workbench`, você verá um conjunto de ferramentas específicas para operações de CAM.
# 
#     - A interface incluirá opções para criar novas operações de caminho, configurar ferramentas e materiais, e gerar simulações de caminhos de ferramentas.
# 
# 4. **Criar ou Importar um Desenho:**
# 
#     - Antes de criar caminhos de ferramentas, você precisa ter um modelo 3D. Você pode criar um novo desenho usando outro workbench do `FreeCAD`, como o PartDesign, ou importar um desenho existente.
# 
#     - Certifique-se de que o desenho esteja pronto e apropriado para as operações de usinagem.
# 
# 5. **Usar as Ferramentas do `Path Workbench`:**
# 
#     - Utilize as ferramentas do `Path Workbench` para criar operações de caminho, como contornar, perfurar, gravar, etc.
# 
#     - Configure as propriedades de cada operação, como profundidade, velocidade de corte, e seleção de ferramenta.
# 
# 6. **Simular o Caminho de Ferramentas:**
# 
#     - Após configurar as operações, use a ferramenta de simulação para visualizar o caminho de ferramentas. Isso é crucial para garantir que tudo está configurado corretamente antes da usinagem real.
# 
# 7. **Exportar o Código G:**
# 
#     - Quando estiver satisfeito com a configuração, você pode exportar o caminho de ferramentas como código G, que será usado pela sua máquina CNC.
# 
# **Dicas Adicionais**
# 
# - **Explorar Tutoriais e Documentação:** Se você é novo no Path Workbench ou no CAM em geral, explorar tutoriais online e a documentação do `FreeCAD` pode ser muito útil.
# 
# - **Configurações de Máquina:** Lembre-se de que diferentes máquinas CNC podem requerer configurações específicas no código G. Verifique as especificações da sua máquina e ajuste as configurações conforme necessário.
# 
# - **Prática e Experimentação:** Como qualquer ferramenta poderosa, o Path Workbench tem uma curva de aprendizado. Pratique com projetos simples para se familiarizar com as funcionalidades e capacidades do workbench.
# 
# Ao seguir estes passos, você será capaz de ativar e começar a usar o Path Workbench no FreeCAD para suas necessidades de CAM.
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar freecad 0.19 no ubuntu:*** https://chat.openai.com/c/f3fbd8b3-8f3c-478f-9cda-568f7da146d8 (texto adaptado). ChatGPT. Acessado em: 16/11/2023 10:06.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). ChatGPT. Acessado em: 16/11/2023 10:06.
# 
# [3] OPENAI. ***Ativar ModerUI no FreeCAD:*** https://chat.openai.com/c/7d74a9a2-f569-4ef0-8e2b-3421e67dc053 (texto adaptado). ChatGPT. Acessado em: 05/12/2023 20:07. 
# 
# [4] OPENAI. ***Ativar a2plus no freecad:*** https://chat.openai.com/c/51b969b1-a80b-48fa-84dc-4f019ba41ba7 (texto adaptado). ChatGPT. Acessado em: 05/12/2023 20:08.
