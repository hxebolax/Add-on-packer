# Manual do utilitário para extras do NVDA

Este extra tenta ser um pacote de utilitários para os nossos extras instalados e não instalados.

Nas diferentes áreas tenta-se ser o mais rápido possível dando a hipótese de efetuar ações sobre os nossos extras de maneira massiva e não ter que ir de um a um como acontece no Gestor de extras.

As áreas já adicionadas serão aprimoradas nas diferentes versões à medida que novas funções forem adicionadas.

Este add-on pode ser lançado a partir do menu Ferramentas / Utilitários para extras do NVDA.

O extra não possui um atalho de tecla atribuído para uso rápido.

Um atalho pode ser adicionado no menu Preferências / definir comandos... e procurar a categoria Utilitários para extras do NVDA.

## Isenção de responsabilidade

O utilizador final é o último responsável pela utilização do extra.

Tenta-se que tudo seja o mais fiável possível mas sempre podem surgir problemas pelo que o autor do extra não será responsável por qualquer problema surgido pela utilização deste extra.

# Visão geral

O extra está dividido em 3 secções.

* 1 secção: Lista onde podemos escolher a categoria que queremos usar. É onde fica o foco toda vez que chamamos o extra.

Vamos mover-nos com seta para cima e para baixo nessa lista.

* 2 secção: a área que compreende o conteúdo da categoria que escolhemos.

Essa área é mutável dependendo da categoria. Ver Descrição das categorias abaixo.

Podemos aceder a partir das categorias com atalhos de tecla ou tabulação.

* 3 secção: Esta secção contém uma caixa de edição que será ativada quando alguma ação for executada, dando ao utilizador informações sobre o que está a acontecer. O utilizador também será informado com uma barra de progresso em todas as ações.

Também compreende os botões que nos permitirão interagir, dependendo do que aconteceu ao fazer a ação, como um botão Fechar, o qual fechará o extra.

Enquanto não houver uma ação em andamento, o extra poderá ser fechado com Escape, Alt + F4 ou tabulando até o botão Fechar.

## Empacotador de extras

Se escolhermos esta categoria, quando tabularmos, cairemos numa lista com todos os extras que temos instalados, independentemente de estarem ativados, desativados ou não compatíveis.

Podemos também ir, rapidamente, com Alt + L; nesta lista, podemos selecionar, com a barra de espaço, todos aqueles extras que desejemos escolher para fazer uma cópia de segurança em um diretório que escolhamos.

Cada extra será gerado com o seu nome, versão e um elemento de identificação "_gen", esses extras gerados poderão ser instalados com o NVDA sem nenhum problema.

Se tabularmos, cairemos num botão chamado "seleção", ou podemos acessá-lo rapidamente com Alt+S. O dito botão, se o pressionarmos, será mostrado um menu para podermos selecionar ou desmarcar todos os extras rapidamente.

Se voltarmos a tabular, cairemos no botão gerar, atalho Alt + G. Se pressionarmos esse botão e tivermos pelo menos um extra marcado, ele abrirá uma janela para escolher a pasta onde queremos guardar os extras selecionados.

Uma vez escolhido o diretório e ativando "aceitar", começará a geração dos extras. O foco ficará numa caixa de somente leitura, na qual aparecerão informações ao lado de uma barra de progresso que nos avisará da percentagem decorrida. O botão Fechar, assim como o restante da interface, será desativado até que a ação de gerar os extras termine.
*/*
Uma vez que a ação termine nos informará se tudo foi bem sucedido ou houve algum problema e se agora tabularmos podemos escolher aceitar (Alt+A), Cancelar (Alt+C) ou fechar a interface se quisermos.

Os botões OK e Cancelar sairão de acordo com a conclusão da ação.

Para gerar os extras é indispensável ter marcado pelo menos um caso contrário nos informará com uma mensagem explicativa.

## Instalador múltiplo

Esta categoria nos permitirá escolher um diretório onde temos extras e podemos instalá-los todos de uma só vez.

Quando entramos nessa categoria, cairemos em um botão chamado " selecione um diretório com extras a serem instalados..."ou atalho (Alt+S), Se o pressionarmos nos dará uma janela para escolher o diretório que contém extras.

O resto da interface nesta categoria está desativado até que não escolhamos um diretório.

Quando escolhermos um diretório, o foco nos deixará na caixa somente leitura, onde seremos informados do que está acontecendo enquanto se verifica em busca de extras, também receberemos informações da barra de progresso.

Uma vez concluída a digitalização, seremos informados se houve algum problema e como agir. Dizer que só aceitará extras que cumpram com a API do NVDA que tenhamos instalado descartando qualquer extra incompatível ou que esteja corrompido.

Uma vez terminado o escaneamento e se encontrou extras e damos a aceitar se ativará a lista com os nomes dos extras que tenha encontrado nesse diretório.

Podemos ir rapidamente para essa lista com (Alt + L), nessa lista podemos escolher quantos extras quisermos marcando-os com espaço.

Se tabularmos teremos o mesmo botão Seleção que há na tela empacotadores de extras e que não vou explicar por que é seu mesmo uso.

Se tabularmos novamente cairemos no botão Instalar ou acesso rápido (Alt+I).

Se tivermos pelo menos um extra selecionado e pressionarmos esse botão, a instalação do extra será feita de um ou vários sem mostrar a janela clássica do NVDA de instalação, com isso agilizamos a instalação de extras.

Dizer que esta etapa também tem proteções como verificação de API, que o extra não está corrompido e outras coisas internas do NVDA. Tudo para tentar sempre o melhor desempenho do nosso leitor.

Quando dermos o botão Instalar o foco ficará na caixa de somente leitura onde se informará do que está realizando o extra.

Da mesma forma, quando terminar, seremos informados se tudo foi um sucesso ou se houve algum extra que não pôde ser instalado ou se houve erros.

Dependendo do que aconteceu, ativaremos o botão OK ou Cancelar ao lado do botão Fechar.

Se você ativar o botão OK, é porque o NVDA instalou algum extra e, para aplicar as alterações, ele precisa ser reiniciado, se pressionarmos o NVDA será reiniciado e já teremos os extras ou extras instalados.

Se não aceitarmos e fecharmos, não poderemos usar o extra novamente até reiniciarmos o NVDA.

Caso contrário, houve falhas e apenas o botão Cancelar é apresentado, podemos pressioná-lo e voltar para a interface para fazer outras coisas.

### Aviso

Esta categoria é implementada para agilizar a instalação de Add-Ons, mas mal utilizada instalando add-ons por instalar pode resultar em um mau funcionamento do leitor. É responsabilidade do Usuário usá-lo adequadamente.

## Desinstale extras

Esta categoria nos permitirá desinstalar extras de uma maneira rápida e de uma só vez.

Podemos escolher na lista qualquer um dos extras que temos instalados. Podemos selecionar com espaço. Para ir rapidamente para a lista (Alt + L).

Dispomos também do botão Seleção (Alt + S) que cumpre a função exatamente como nas anteriores categorias e não voltarei a explicar.

Se tabularmos encontraremos o botão Desinstalar ou acesso rápido (Alt+D) Se o pressionarmos e tivermos um ou mais extras selecionados nos deixará o foco no campo de somente leitura e nos informará do que está realizando.

Você também será informado através da barra de progresso.

Uma vez concluído, informaremos o resultado e, como na categoria Instalador múltiplo, receberemos o botão OK informando que você precisa reiniciar o NVDA ou Cancelar informando que algo deu errado e o botão Fechar.

Lembre - se de que, se fecharmos nesta categoria e não atendermos à necessidade de reiniciar o extra, ele não poderá ser usado novamente até que o NVDA não seja reiniciado.

### Aviso

A desinstalação de extras uma vez que demos o botão Desinstalar não tem como voltar, por isso é conveniente garantir que sabemos de onde obter os extras que removemos, caso desejemos reinstalá-los, assim como se o referido extra contiver informações no diretório do extra em si, essas informações serão excluídas.

Geralmente não é de boa prática e o NVDA não recomenda que os extras salvem informações no mesmo diretório do extra, mas isso já é decisão do programador do extra.

Portanto, repito usar esta categoria sob sua responsabilidade.

## Ativar / desativar extras

Esta categoria nos permitirá ativar ou desativar em massa nossos extras.

Se entrarmos na categoria cairemos na lista dos extras que estão habilitados podemos aceder rapidamente com (Alt + L), poderemos marcar os extras que desejamos desativar com a barra de espaço.

Se tivermos extras desativados, então teremos uma segunda lista com esses extras, podemos nos mover rapidamente entre listagens com (Alt + L) nessa lista de extras desativados também podemos marcar aqueles que queremos habilitar com a barra de espaço.

Podemos marcar extras nas duas listagens tendo em conta que a ação se executará ao contrário desabilitando os extras marcados na lista de extras habilitados como habilitando os extras que estejam marcados na lista de extras desabilitados.

Esta categoria também tem um botão de seleção, mas com uma pequena diferença, quando pressioná-lo conterá um submenu para cada listagem, podendo selecionar ou desmarcar tudo para a listagem que escolhermos.

Se tabularmos nos encontraremos com o botão Processar ou acesso rápido (Alt + P), Se o pressionarmos nos deixará o foco na caixa de somente leitura e nos informará do que está realizando.

Uma vez concluída a ação acontecerá da mesma forma que nas categorias anteriores, informando - nos e ativando os botões correspondentes.

Novamente, se a ação for bem-sucedida e não reiniciarmos, o extra não poderá ser usado até que o NVDA seja reiniciado.

## Modificador de manifesto

Nesta categoria podemos alterar o Manifesto e assim poder compatibilizar os extras com a API que requer NVDA. Podemos alterar o manifesto para extras instalados ou extras que temos em um arquivo de extras do NVDA.

Agora, de acordo com a política mais recente do NVDA e até novas alterações, todos os anos na primeira versão do NVDA, os programadores terão que alterar a versão para combinar seu manifesto com a versão do NVDA.

Bem, haverá programadores que o fazem imediatamente, outros que demoram e outros que simplesmente não o fazem por abandono de extras ou por qualquer motivo.

Neste último caso, teremos que fazer a mudança da propriedade lastTestedNVDAVersion manualmente e, se tivermos muitos extras, teremos que perder tempo, além disso, não é uma tarefa para todos os utilizadors, pois há muitos níveis de utilizadors.

Além disso, se quisermos testar os betas e os RC, teremos que alterar esse parâmetro nos manifestos, caso contrário, não poderemos ter o extra instalado.

Bem, o NVDA é um leitor em constante evolução, por isso muitas vezes há extras que ficam no caminho por falta de desenvolvimento e por falta de adaptá-los às mudanças que o NVDA em sua evolução traz.

Isso significa que alterar a data nos manifestos corrige um problema momentâneo para que você possa continuar usando os extras que não estão sendo atualizados ou que o desenvolvedor está demorando para atualizá-los. Mas haverá extras que não servem apenas para alterar o Manifesto e precisam de alterações internas para se adaptar às novas versões, nesse caso o extra será quebrado e só resta entrar em contato com o autor do extra.

Bem aconselho atualizar os extras que saiam já com as mudanças nos manifestos, embora tenhamos mudado com este utilitário a data já que é possível que esses extras tragam além da adaptação do manifesto outras modificações que o desenvolvedor tenha feito.

Uma vez acedemos a esta categoria cairemos na lista que conterá todos os extras que temos instalados junto à sua versão API. Podemos aceder rapidamente com (Alt + L), podemos selecionar os extras que queremos alterar seu manifesto clicando sobre eles e quantos desejarmos.

Se tabularmos, cairemos em três caixas de combinação:

* Selecione Versão maior: esta caixa de combinação tem que coincidir com a data da versão que você vai ter NVDA.

* Selecione versão Menor: aqui com deixá-lo em 1 é suficiente no entanto e Posto as quatro versões que saem anuais para o caso de haver mudanças. (Tudo pode acontecer)

* Selecione uma revisão: Nesta caixa de combinação com deixá-lo para 0 é suficiente no entanto eu coloquei até 9 também apenas no caso.

Se tabularmos temos novamente o botão Seleção que nos permitirá selecionar ou desmarcar todos os extras que há na lista.

Se voltarmos a tabular, cairemos no botão Processar ou acederemos rapidamente com (Alt + P).

Bem, se pressionarmos este botão, um menu com as seguintes opções será exibido:

* Processar instalados, se escolhermos esta opção iniciará o processo de mudar o manifesto para os extras que tenhamos instalados e tenhamos selecionado. Ele será alterado para o que tivermos escolhido nas caixas de combinação de versão maior, menor e revisão.

* Processar um arquivo de extra, se escolhermos esta opção nos abrirá uma janela de Abrir Arquivo onde teremos que escolher o arquivo de extra que desejamos alterar o manifesto. Dizer que antes temos que escolher a versão maior, menor e revisão para que se aplique a ela.

Se optarmos por mudar o manifesto para um arquivo e o processo foi satisfatório, no diretório de origem do plugin será gerado outro plugin com o mesmo nome, mas com a Tag de identificação "_gen_modify_manifest" este será o que contém o manifesto modificado para ser usado.

Com qualquer uma das duas opções, deixaremos o foco na caixa somente leitura e seremos informados com o que acontece.

O comportamento será o mesmo que nas categorias anteriores com os botões OK e Cancelar.

Lembre-se de que, se escolhermos um arquivo de extra antes, devemos alterar as caixas de combinação de versão maior, menor e revisão para que se aplique ao arquivo que escolhemos essa configuração para o manifesto.

### Aviso

O uso deste utilitário e seus resultados fica exclusivamente sob a responsabilidade do utilizador final.

## Documentação do plugin

Nesta categoria e visto que há pessoas que têm dificuldade em encontrar como ler a documentação dos extras, podemos fazer exatamente isso, consultar a documentação que os autores escreveram para saber o manuseio dos extras.

Nesta categoria encontraremos uma lista com acesso rápido (Alt + L) na qual se mostrarão todos os extras que têm documentação ficando excluídos aqueles que por qualquer motivo não têm documentação.

Se tabularmos encontraremos um botão chamado "Abrir documentação do extra" ou acesso rápido (Alt+a), se pressionarmos ou chamarmos esse botão a partir da lista será aberta em nosso navegador por padrão a documentação do extra que tenhamos escolhido na lista.

# Tradutores e colaboradores:

Se alguém quiser colaborar com traduções pode fazê-lo através do repositório Github do plugin ou enviando um e-mail para xebolax@gmail.com

* Inglês: Dragan Ratkovich (documentação tradução automática)
* Turco: Umut korkmaz
* Francês: Rémy Ruiz
* Árabe: Wafiq Taher
* Alemão: Moritz Wolfart
* Russo: Valentin Kupriyanov (comunidade russa NVDA.RU)
* Italiano: Leonardo Marenda
* Ucraniano: Vova Mobile

# Registro de alterações.
## Informações sobre atualizações:

Este plugin seguirá o seguinte caminho de atualizações:

Apenas as versões de tipo maior.menor (por exemplo v3. 1) são listados neste histórico.

Versões de tipo maior.menor.x (por exemplo v3. 1. 2) são atualizações de tradução.

As alterações no extra serão refletidas nesta seção explicando o que há de novo.

O documento principal não será modificado sendo uma orientação para o utilizador.

O Usuário é responsável por revisar esta seção para ser informado das alterações.

## Versão 1.2.

* Corrigido erros graves no backup.

## Versão 1.1.

* Bugs corrigidos.

* Adicionado a capacidade de fazer e restaurar backups.

Agora teremos uma nova seção chamada fazer / restaurar backups.

Essa seção mostrará em uma lista as opções que podemos fazer backup.

As opções que nesta versão podem ser salvas em um backup são:

* Diretório dicionários (\speechDicts)
* Diretório perfis (\profiles)
* Diretório Scratchpad (\scratchpad)
* Arquivo configuração disparadores de perfil (profileTriggers.ini)
* Arquivo de configuração gestos de entrada (gestures.ini)
* Arquivo de configuração do NVDA (nvda.ini)

A lista mostrará apenas os itens que estão presentes em nossa cópia do NVDA, assim como os diretórios que têm conteúdo.

Se, por exemplo, o diretório de perfis este vazio não deixar fazer backup.

Teremos que selecionar pelo menos um item da lista para poder fazer o backup.

Se tabularmos encontraremos dois botões:

* Criar cópia de segurança

Se pressionarmos este botão abrirá uma janela clássica de salvar de Windows dizendo para colocar o nome do nosso backup e onde queremos salvá-lo.

Quando lhe dermos para salvar começará a cópia de segurança e na caixa de somente leitura de estado nos dirá o resultado se tudo correu bem ou se ocorreram erros.

* Restaurar backup

Quando pressionarmos este botão, uma janela clássica do Windows será aberta para abrir um arquivo de backup, teremos que procurá-lo onde salvamos a cópia e abri-lo.

Uma vez aberto o arquivo, será mostrada uma janela com o conteúdo do backup, nessa janela aparecerá uma lista para selecionar os itens que queremos restaurar.

Quando quisermos, clique em restaurar e, na caixa de status, informaremos a restauração se foi correta ou houve algum problema.

Aviso:

Quando restaurarmos um elemento do NVDA será necessário reiniciar o NVDA para que qualquer ação que façamos em utilitários para os extras do NVDA sua consequência será reiniciar o NVDA e pressionemos ok, cancelar, fechar, escape ou Alt + F4.

Se ocorrer um erro ao restaurar vários itens com apenas um sendo restaurado, o NVDA também será reiniciado.

## Versão 1.0.

* Versão inicial.

Foi reescrito do zero o que era o antigo empacotador de extras junto com a adição de novas funções.

O extra é renomeado para utilitários para extras NVDA, mas ainda mantém o nome interno que o NVDA manipula em (addonPackager).

Ao lançar esta versão o extra cricricri ficará sem manutenção já que este extra já inclui a mudança de manifestos.