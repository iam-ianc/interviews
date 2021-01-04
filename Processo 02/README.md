<h1 align="center"> 
	 Landing Page 🚀
</h1>

🏠 Landing Page - Nesta primeira parte do teste, foi solicitada o uso do bootstrap na versão 3 que é suportado pelo Internet Explorer 9 e superiores. 
- A página foi criada de forma responsiva e seguindo um layout em PSD previamente disponibilizado.
- Utilizei também por conta própria o SASS para a manipulação de variáveis e mixins, como por exemplo, a construções de espaçamento (margin e padding) e em todos os breakpoints necessários.


<h1 align="center"> 
	 Quiz 🚀
</h1>

✔️ Quiz - Nesta segunda parte do teste, foi solicitado apenas a manipulação de código JavaScript, sendo o HTML e o CSS já disponibilizados.

- O teste consiste em fazer uma requisição via fetch em um banco de dados que retorna um JSON. 
- Dada a pergunta, é necessário percorrer as alternativas onde cada alternativa tem um identificador único que é comparado com o resultado armazenado no banco.
- Caso o usuário selecione alguma alternativa, um botão de "Confirmar" é exibido, se a mesma opção é selecionada novamente pelo usuário, o botão "Confirmar" é ocultado e a seleção é desmarcada. 
- Caso o usuário troque de alternativa, o botão "Confirmar" segue sendo exibido e a seleção é alterada para a nova alternativa.
- Se o usuário confirma a sua seleção, e essa seleção for diferente da armazenada no banco, então é exibido um feedback negativo, e tem a chance de mudar de alternativa.
- Se a seleção confirmada for a mesma da armazenada no banco, então é exibido um feedback positivo e o usuário é impossibilitado de tentar marcar uma nova alternativa, e o botão "Confirmar" é desabilitado.

OBS.: A parte do Quiz deve ser executada pelo Live Server no VS Code ou na pasta ./src você pode utilizar o comando no terminal 'yarn dev'.
