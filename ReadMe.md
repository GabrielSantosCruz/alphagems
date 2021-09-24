# Alphagens

## Problema
"A disciplina EXA854 - MI - ALGORITMOS do primeiro semestre do curso de Engenharia de Computação da Universidade Estadual de Feira de Santana (UEFS), que trabalha com o método de ensino `Aprendizagem Baseada em Problemas (PBL)`, visa aproximar o estudante da área  de computação com problemas cotidianos com o fito de estimular o aluno a `buscar conhecimento`. Dito isto, a professora da disciplina resolvou passar o seguinte problema com o objetivo de testar nossos conhecimentos sobre `funções` e `modularização` de um código e ultilizá-los para resolver um problema."

## Enunciado

"O mercado mundial de jogos digitais segue alheio às crises financeiras dos últimos anos. Apenas em 2019 o setor lucrou US$120,1 bilhões, mostrando um crescimento de 4% em relação a 2018. Em 2020, ano extremamente afetado pela pandemia, o mercado voltou a registrar aumento de receita, alcançado incríveis US$126,6 bilhões. Desejando participar deste mercado multimilionário, a `Rookie Software Inc.` iniciou uma busca por profissionais através de uma seleção remota. A Rookie é famosa por contratar jovens talentos, logo, esta será uma excelente oportunidade para iniciantes. O processo de seleção da empresa consiste no desenvolvimento de `uma versão do jogo Gemas`"

## O jogo

"O jogo Gemas consiste em `um tabuleiro com m colunas e n linhas` contendo gemas de cores distintas. `A cada passo do jogo`, o jogador ou jogadora deve `permutar` de posição `duas gemas adjacentes` de tal forma que se crie uma cadeia de `3 ou mais gemas da mesma cor`. Quando tal cadeia é criada, as gemas correspondentes são destruídas (eliminadas), gerando pontos para o jogador (igual ao número de gemas destruídas) e fazendo com que as gemas que se encontram acima “caiam”, tomando o lugar das gemas destruídas. Ao cair, é possível que novas cadeias se formem, causando uma reação em cadeia. `Os espaços vazios` criados pelas gemas que caíram `são então preenchidos por gemas geradas aleatoriamente`. Esse passo também pode criar novas cadeias que são automaticamente eliminadas, reiniciando o ciclo."

### Tabuleiros e gemas

"O tabuleiro deve ser representado por uma `matriz` m x n de strings, onde m e n são fornecidos pelo usuário. Cada tipo (cor) de gema é representado por uma `letra maiúscula` distinta, utilizando-se das c primeiras letras do alfabeto em caixa alta (A, B, C, …).Deve ser assumido que o número de colunas e linhas é no máximo 10."

### Dicas

"Durante o jogo, `é possível obter dicas`, que são fornecidas `na forma da posição` de uma gema cuja `permutação` com outra gema é válida. Cada dica obtida `gera o desconto de 1 gema` do total de pontos (dados pelo total de gemas destruídas)."
