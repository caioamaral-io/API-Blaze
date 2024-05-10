<h1>API Double Blaze</h1>

<p>A API Double Blaze é uma ferramenta em Python que permite acessar os dados do jogo Double na plataforma Blaze e enviar sinais para um grupo no Telegram.</p>

<h2>Funcionalidades</h2>

<ul>
  <li><strong>Acesso aos dados do jogo:</strong> Esta API utiliza Selenium e BeautifulSoup para extrair informações do jogo na plataforma Blaze, como estatísticas, resultados recentes e outras métricas relevantes.</li>
  
  <li><strong>Envio de sinais para o Telegram:</strong> Além disso, ela é capaz de enviar sinais diretamente para um grupo no Telegram com base nos resultados do jogo, permitindo que os usuários recebam notificações em tempo real sobre eventos importantes.</li>
  
  <li><strong>Suporte a múltiplos gales:</strong> A API suporta múltiplos gales e estratégias de gestão, permitindo uma operação flexível e personalizável.</li>
</ul>

<h2>Como Usar</h2>

<p>Para utilizar a API, basta seguir os seguintes passos:</p>

<ol>
  <li>Instale a API utilizando o pip:</li>
  
  <pre><code>pip install double-blaze-api</code></pre>
  
  <li>Configure suas credenciais para acesso ao Telegram e inicie a API:</li>
  
  <pre><code>from double_blaze_api import DoubleBlazeAPI

api = DoubleBlazeAPI(api_key='SUA_CHAVE_API_DO_TELEGRAM', chat_id='ID_DO_SEU_GRUPO_NO_TELEGRAM')
api.start()</code></pre>
  
  <li>Agora a API está pronta para acessar os dados do jogo na Blaze e enviar sinais para o Telegram.</li>
</ol>

<h2>Contribuição</h2>

<p>Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar esta API.</p>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a Licença MIT - consulte o arquivo <a href="LICENSE.txt">LICENSE.txt</a> para mais detalhes.</p>
