# Empacotador de extras

## Nota prévia:

Para que o extra possa funcionar, terá que ser iniciado, primeiro, no menu de ferramentas do NVDA

Esta ferramenta surge da necessidade de ter uma cópia de segurança dos extras instalados.

O NVDA possui uma grande colecção de extras oficiais, fáceis de obter desde os repositórios oficiais ou nas diferentes contas do GitUb dos respectivos autores.

No entanto, possui também uma série de extras não oficiais, cuja fonte é por vezes difícil de determinar.

A ideia surgiu quando um amigo me pediu um determinado extra não oficial, e como eu não o tinha em mãos, tive de o empacotar de forma a poder enviar-lho.

O processo de empacotamento de extras é fácil, mas não é conhecido por todos, pelo que me ocorreu a ideia de que seria fantástico  se o NVDA  oferecesse tal possibilidade.

Eis o que faz este extra: Empacota automaticamente os extras que o utilizador tem instalados, quer seja para instalar em uma cópia limpa do NVDA, quer seja para partilhar com outras pessoas ou mesmo para instalar noutra cópia do NVDA.

## Utilização do extra

Este extra é dividido em 4 secções:

* A primeira, que contém uma lista com todos os extras instalados, quer estejam activados ou desactivados. Nesta lista é possível seleccionar todos os extras pretendidos.
* A segunda, que apresenta uma linha de botões para marcar rapidamente todos os extras ou limpar rapidamente a selecção dos extras seleccionados.
* A terceira, é uma caixa de texto só de leitura que conterá a pasta de saída e um botão para escolher a respectiva pasta.
Fiz esta caixa de texto só de leitura de forma a se poder verificar facilmente a pasta de saída em qualquer altura. E decidi-me por não a colocar como uma caixa normal de edição, para evitar qualquer pressão acidental de teclas  e, com isso, afectar a pasta de saída.
* A quarta e última secção contém uma linha de botões com um botão para gerar os extras empacotados e outro para sair do diálodo do Empacotador de Extras.

### Teclas de acesso rápido para o extra

(estas teclas só funcionam após a inicialização do extra, como explicado na nota prévia)
* ALT+L: Levará o foco para a lista dos extras.
* ALT+S: Irá seleccionar rapidamente todos os extras, independentemente de já haver algum seleccionado ou não seleccionado.
* ALT+A: Irá limpar a selecção de todos os extras seleccionados.
* ALT+p: Abrirá uma janela para definir a pasta de saída.
* ALT+C: Iniciará a criação dos extras.
* ALT+F4: Irá fechar a caixa de diálogo.

## Outra informação relevante::

* O utilizador será notificado, a todo o momento, com diálogos de informação acerca do progresso da operação, bem como, caso esteja a tentar criar um extra e não tenha seleccionado nenhum a partir da lista.
* Da mesma forma, avisará se o utilizador tentar criar um extra sem ter definido a pasta de saída.
* Por fim, notificará, ao fim do processo, se a operação foi concluída com êxito ou ocorreu um erro.
* Importante: A definição da pasta de saída será mantida para que não seja necessário defini-la, da próxima vez; no entanto, perder-se-á caso a pasta seja eliminada, pelo que o utilizador terá de definir outra pasta existente.
* Ao criar os extras, o sistema mostrará uma barra de progressão que indicará a percentagem actual durante todo o processo.
* Os ficheiros resultantes terão a etiqueta  (gen), para indicar que foram gerados e não são originais.

# Nota muito importante

Os ficheiros resultantes serão tal qual a pasta respectiva do extra pretendido, sem adicionar nem eliminar absolutamente nada, durante o processo, o que quer dizer que estão incluídas todas e quaisquer informações constantes no extra actualmente seleccionado.
Se bem que não seja normal para um desenvolvedor de extras incluir informação confidencial dentro da pasta do próprio extra, na verdade, é considerada má prática, pelo que é improvável que, pelo menos, nos extras oficiais, isto aconteça...
Porém, dada a existência de centenas de diferentes tipos de extras não oficiais e obtidos através de inúmeras fontes, o utilizador está avisado que, se o extra em questão incluir informação sensível dentro da pasta do próprio extra, esta informação será incluída no ficheiro criado.
Tenha em conta este aspecto de privacidade e segurança, para saber se algum extra criado que deseja partilhar contém informação sencível que não deva ser partilhada.
Como referi, isto é quase improvável, mas o utilizador está avisado e, com a utilização deste extra, concorda em saber que foi avisado e que o autor deste extra está isento de quaisquer responsabilidades.
(Tradução: Wendril Brandão)