# Empacotador de complementos

## Nota prévia:

Deve abrir o complemento no menu de ferramentas do NVDA, pois de outra forma não funciona!

Este complemento surge da necessidade de ter um backup dos complementos instalados.
O NVDA possui uma grande coleção de complementos oficiais, fáceis de obter nos repositórios oficiais ou nas diferentes contas dos autores do Github.
Mas, ao mesmo tempo, também possui vários complementos não oficiais, que às vezes são difíceis de se obter, e mesmo saber de onde foram obtidos.
A idéia surgiu quando um amigo me pediu um complemento não oficial e, como eu não tinha o complemento em mãos, tive que empacotá-lo.
O processo de empacotamento do complemento é fácil, mas não é conhecido por todos, pelo que, ocorreu-me, seria ótimo se o NVDA o oferecesse.
É isso o que este complemento faz: empacota automaticamente os complementos que o usuário deseja para poder instalá-lo em outra cópia do NVDA, em uma instalação limpa ou compartilhá-lo.

## Utilização do complemento:

O complemento é dividido em quatro áreas:

* A primeira contém uma lista com todos os complementos instalados, habilitados ou desabilitados. Nesta lista, podemos selecionar todos os acessórios que queremos.
* A segunda apresenta uma linha de botões para selecionar rapidamente todos os complementos ou apagar rapidamente as seleções.
* A terceira é uma caixa de texto de leitura que conterá o diretório de saída e um botão para selecionar esse diretório de saída. Fiz a caixa de texto somente leitura, para que seja fácil verificar o diretório de saída a qualquer momento. E decidi não tornar normal a gravação para evitar qualquer clique por engano e que o diretório pudesse ser afetado.
* A quarta área apresenta botões para gerar os complementos já empacotados ou sair do complemento.

### Teclas de atalho no complemento

(estas teclas só funcionam com o complemento aberto)
* Alt + L: posiciona o foco na lista de complementos.
* Alt + S: selecionar todos os complementos
* Alt + A: limpar a seleção
* Alt + P: selecionar diretório destino
* Alt + C: iniciar geração dos complementos
* Alt + F4: fechar a janela

##Outras informações relevantes:

* O complemento notificará o utilizador o tempo todo com diálogos informativos sobre o curso do manuseio, bem como caso se tente gerar um complemento sem ter nada selecionado.
* Da mesma forma, avisará se o utilizador tentar gerar um plugin sem ter um diretório de saída definido.
* Por fim, notificará, ao fim do trabalho, se o processo foi bem sucedido ou ocorreu algum erro.
* Importante: o diretório de saída será salvo para que seja especificado na próxima vez qu
e usarmos o complemento, mas essa configuração será excluída se o diretório de saída for removido, pelo que o utilizador terá de selecionar outro diretório existente.
* Ao gerar os complementos, o sistema mostra uma barra de progresso que indicará a porcentagem realizada sempre.
* Os arquivos resultantes têm uma tag no nome para identificar que eles foram gerados e não são originais. Essa tag é (gen).

# Nota muito importante: 

os arquivos resultantes são os que temos no diretório Addon, sem adicionar ou remover nada deste plugin. Isso significa que todas as informações do complemento que selecionamos estão incluídas. Bem, não é normal para um desenvolvedor de complementos incluir informações confidenciais dentro do próprio diretório do complemento. Na verdade, é considerado uma má prática, portanto, é improvável que pelo menos nos complementos oficiais isso aconteça.
Mas como existem centenas de tipos diferentes e não oficiais de complementos, é imperioso informar que, se algum complemento incluir informações confidenciais no diretório do seu complemento, essas informações confidenciais serão incluídas no arquivo gerado.
É por isso que precisamos levar em conta esse aspecto de privacidade e segurança para saber se compartilharíamos um complemento gerado se ele trouxer informações confidenciais que não queremos compartilhar.
Como mencionei, isso é quase improvável, mas você é avisado e, com isso, usando este complemento, concorda em saber que foi avisado e que está cumprindo toda a responsabilidade com o autor deste complemento.
(Tradução de: Lucas Antônio)