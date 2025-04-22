## P.R.O.M.P.T

Planejar, criar e testar prompts para gerar melhores respostas em grandes modelos de linguagem (GML/LLM). É a meta habilidade que destrava todas as outras.

## Estrutura básica PROMPT

## Processo

- Definir a tarefa e os critérios de sucesso:

* Desempenho e precisão: Quão bem o modelo precisa executar na tarefa?

- Desenvolver casos de teste e tratamento de erros
- Escrever o prompt inicial pensando em quais instruções daria para que outro ser humano fosse fazer aquela tarefa.
- Testar contra exemplos
- Refinar o prompt

## Dica PROMPT:

- Não complique. Prompts simples vão resolver a maioria dos problemas;
- Os PROMPTS do ChatGPT vão até 8.000 caracteres. Se passar disso, suba arquivos em PDF para ele consultar ao invés de jogar o texto ali.

## Fundamento #1: Use a Estrutura P.R.O.M.P.T

- Persona: Serve para direcionar o modelo de linguagem sobre como ele deve se comportar. Ex: Haja como um especialista em marketing;
- Roteiro: Serve para direcionar O QUE você pretende fazer. Ex: Criar um planejamento semestral de marketing;
- Objetivo: Serve para direcionar a sua intenção com esse trabalho, ou seja, o que você pretende alcançar com aquilo. Ex: Apresentar para um cliente.
- Modelo: Serve para direcionar o formato em que você quer aquele resultado. Ex: No formato de 8-10 slides;
- Panorama: Serve para dar mais contexto e exemplos de boas respostas (títulos, por exemplo) para o modelo de linguagem para aumentar as chances de ele acertar o que foi pedido. Ex: A empresa para qual vou fazer o planejamento semestral é assim (...). Um bom planejamento semestral é assim.
- Transformar: Serve para melhorar os resultados que o modelo de linguagem trouxe. Ex: Altere x, y, z.

## 💡 Prompt base para adaptar no dia a dia

"Quero que você atue como [função desejada: ex. desenvolvedor fullstack experiente / mentor de carreira / especialista em IA]. Estou trabalhando em [explique o projeto ou tarefa], usando [tecnologias]. Meu objetivo com isso é [explique o porquê do projeto]. Preciso de ajuda com [explique o que precisa]. Considere que [coloque limitações ou contexto adicional]."

## Fundamento #2: Use Markdowns para obter resultados melhores dos seus prompts.

- Formatando o prompt de forma organizado, a LLM vai trazer respostas melhores.
- A LLM costuma se perder em textos muito longos. Colocando referências e outras informações entre <> ...</> ajuda o modelo a se localizar. Ex: Escreva considerando as transcrições. <Transcrição> (lorem ipsum) </Transcrição>
- Em documentos longos, coloque as instruções ANTES do P.R.O.M.P.T para garantir respostas melhores.

## Fundamento #3: Dê EXEMPLOS para que a LMM entregue respostas melhores.

- Tendo uma referência para se basear, a LLM gera respostas muito mais adequadas. Forneça algo semelhante ou aproximado do resultado que você pretende alcançar.

## Técnica #1: Dê estimulos direcionais;

- Direcione a resposta do LLM para o resultado que você deseja alcançar. Ex: Ao invés de dizer: "Faça um resumo", diga "Faça um resumo considerando as palavras-chaves ao lado: Palavra 1, Palavra 2, Palavra 3, etc.". Desse modo, a LMM já vai direcionar a sua analise e resumo para os tópicos que você sugeriu.

## Técnica #2: Estimule uma cadeia de pensamento.

- Quando há problemas de raciocinio lógico, deixar o modelo pensar de forma explícita, passo a passo, funciona melhor do que pedir uma resposta direta.
- Use tags para mostrar onde a LLM deve pensar <pensamento> Lorem Ipsum </pensamento> e onde deve responder <responder> Lorem Ipsum </responder>

## Técnica #3: Compare cadeias de pensamentos.

- Estimule o LLM a dar algumas cadeias de pensamentos para que você possa comparar umas com as outras e ver qual está mais correta.
