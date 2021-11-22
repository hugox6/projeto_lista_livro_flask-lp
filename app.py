from flask import Flask, render_template, request, redirect, url_for
####
app = Flask(__name__)
app.run(debug=True)
###
index = 0
####
livros = [
    {"nomelivro": "Dia de Folga: Um Conto de Natal", "autor": "John Boyne", "ano": "2013", "genero": "Conto", "paginas": "20", "editora": "Companhia das Letras", "skoob": "3.1", "imagemurl": "https://m.media-amazon.com/images/I/61xI-AXzJKL.jpg", "sinopse": "Neste conto breve e melancólico, John Boyne (autor do best-seller O menino do pijama listrado) acompanha o dia de folga de um jovem soldado inglês e seus companheiros, que passam a véspera de Natal em uma das trincheiras da Primeira Guerra Mundial. Enquanto relembra os natais da infância e o conforto do seu lar, ele vê e ouve as bombas alemãs caindo a sua volta. Em meio a um dos piores conflitos do século XX, o jovem irá vivenciar um espírito natalino muito diferente do que estava acostumado."},
    {"nomelivro": "Esquecer o Natal", "autor": "John Grisham", "ano": "2002", "genero": "Romance, humor", "paginas": "216", "editora": "Rocco", "skoob": "3.7", "imagemurl": "https://img.travessa.com.br/livro/BA/de/de46ac01-fd99-49ac-8b95-b5bdafe88e70.jpg", "sinopse": "Nada de árvores, estresse de shopping lotado, despesas sem controle, cartões com mensagens de paz e felicidade. O Natal dos Krunk será diferente: no lugar da festa, do panetone, do peru ou das luzinhas piscando no quintal, o plano é fazer um cruzeiro ao Caribe e desprezar qualquer emoção natalina que ponha tudo a perder. John Grisham provoca boas gargalhadas no leitor com esta hilariante fábula de Natal para os tempos modernos."},
    {"nomelivro": "Férias de Natal", "autor": "William Somerset Maugham", "ano": "2003", "genero": "Romance, humor", "paginas": "273", "editora": "Globo", "skoob": "3.9", "imagemurl": "https://images-na.ssl-images-amazon.com/images/I/41zOtX7FtZL.jpg", "sinopse": "Em ´Férias de Natal,´ William Somerset Maugham narra a primeira viagem a Paris do jovem inglês Charley Mason sem a companhia de familiares, na época do Natal. O prêmio, oferecido por seu pai, é resultado da escolha de Charley, que troca suas pretensões artísticas pela promessa de vir a substituí-lo no cargo que ocupa na empresa da família. A partir desse enredo o autor cria um romance composto não por uma mas por várias histórias. Personagem principal, Charley Mason tem oportunidade de conhecer uma realidade diferente da sua por meio das histórias de Lídia e Simon. Nesse lançamento da Editora Globo, Maugham discute arte, política e relacionamento humano. De enredo simples, econômico nas personagens e no espaço, Férias de Natal nos arrebata pela maneira como o autor conduz a narrativa: ele quer nos contar uma história, nos convence de sua ´realidade´ e nos propõe uma reflexão. E mais não necessita, afirma Luiz Ruffato, que prefacia a obra. Ao dar início à história, Maugham retorna ao passado da famíia Mason e explica que Charley, nascido durante a Primeira Guerra Mundial, estava com 23 anos no começo da narrativa. Era bisneto de Sibert Mason, chefe dos jardineiros numa grande propriedade do Sussex, que se casou com uma cozinheira. Dono de grande tino para negócios, Sibert juntou suas economias e a da mulher para comprar terras no norte de Londres, onde plantaram e venderam hortaliças. Com o crescimento da cidade, a propriedade desaparece e Sibert deixa de lado a lavoura, construindo lojas, armazéns, fábricas e cortiços no lugar. Seu enriquecimento garante a educação dos filhos nas melhores universidades. Já o pai de Charley, Leslie, foi educado em Cambridge e, através de seu interesse pela arte, acaba conhecendo e se casando com Venetia, filha do pintor John Peron, membro da Real Academia. Em Paris, Charley encontra o amigo Simon Fenimore, comunista violento, que trabalha como correspondente de um jornal inglês, emprego conquistado através da influência de Leslie Mason. Simon apresenta Charley a uma princesa russa chamada Olga, em um prostíbulo de luxo. Seu nome, na verdade, é Lídia, que, junto com a família, perdeu todos os bens durante a Revolução Russa de 1917. Finalmente, o jovem inglês conhece, através de Lídia e Simon, o ladrão de carros, traficante de drogas e assassino Roberto Berger..."},
    {"nomelivro": "Milagre na Rua 34", "autor": "Valentine Davies", "ano": "1990", "genero": "Drama", "paginas": "118", "editora": "Acigi", "skoob": "4.3", "imagemurl": "https://d1pkzhm5uq4mnt.cloudfront.net/imagens/capas/_db2859820ab66828851cacf2ab765885ad3184fd.jpg", "sinopse": "Milagre na Rua 34 é um livro inspirador, que conta a história de uma menina que foi criada para não acreditar em milagres. Mas quando aparece em sua cidade um velhinho que afirma ser o verdadeiro papai noel, seu ponto de vista se transforma completamente."},
    {"nomelivro": "Mistério de Natal", "autor": "Jostein Gaarder", "ano": "2000", "genero": "Romance", "paginas": "263", "editora": "Companhia das Letras", "skoob": "3.9", "imagemurl": "https://images-na.ssl-images-amazon.com/images/I/41Uwx6G-8CL._SX324_BO1,204,203,200_.jpg", "sinopse": "Durante os 24 dias anteriores à noite de Natal, o menino Joaquim acompanha um grupo de peregrinos que voltam no tempo para chegar a Belém, onde vão homenagear um recém-nascido. Uma fábula sobre a tolerância, na qual o autor de O mundo de Sofia traça um roteiro histórico do cristianismo."},
    {"nomelivro": "O Expresso Polar", "autor": "Chris Van Allsburg", "ano": "2004", "genero": "Clássico", "paginas": "32", "editora": "Nova Fronteira", "skoob": "4.1", "imagemurl": "https://photos.enjoei.com.br/livro-o-expresso-polar-do-autor-chris-van-allsburg/1200xN/czM6Ly9waG90b3MuZW5qb2VpLmNvbS5ici9wcm9kdWN0cy8xMzY1MDkyNC9mNWQ5NjcxOTc5OThiY2UyNDBmMDlhZmE4OTliNTIyNi5qcGc", "sinopse": "Na véspera de Natal, um menino ouve um barulho que vem do lado de fora de casa. Quando ele olha pela janela, descobre que há um enorme trem parado logo em frente: é o Expresso Polar, que irá conduzi-lo numa viagem de sonho e fantasia rumo ao Pólo Norte, residência oficial do Papai Noel. Marcado pela simplicidade da história e pelas magníficas ilustrações de Chris Van Allsburg, O Expresso Polar é um clássico natalino que nunca sai de moda, e que, apesar de ter sido lançado originalmente em 1985 e ter vendido milhões de cópias em todo o mundo, ainda hoje, quase quarenta anos depois, é o atual nº 1 na lista dos mais vendidos do jornal New York Times."},
    {"nomelivro": "O Natal de Poirot", "autor": "Agatha Christie", "ano": "2016", "genero": "Mistério", "paginas": "224", "editora": "HarperCollins Brasil", "skoob": "4.2", "imagemurl": "https://images-na.ssl-images-amazon.com/images/I/516cfBG9M+L.jpg", "sinopse":"Para a maioria das pessoas, o Natal é uma época de paz e harmonia, em que famílias se reúnem e deixam de lado suas diferenças em nome de valores como o amor e o perdão. Mas Hercule Poirot sabe quão mal essas confraternizações podem terminar... Acompanhado do coronel Johnson, nosso detetive belga é convidado a investigar um caso de assassinato ocorrido na mansão de um velho e odioso milionário, na véspera de Natal. Quem seria capaz de algo tão atroz, arruinando a noite de todos? Bem, aparentemente, cada membro dessa família tinha motivos bem particulares para tirar a vida de seu patriarca. Como Poirot encontrará o verdadeiro culpado no meio desse covil de lobos?"},
    {"nomelivro": "O Presente do Meu Grande Amor", "autor": "Stephanie Perkins", "ano": "2014", "genero": "Ficção Juvenil", "paginas": "352", "editora": "Intrínseca", "skoob": "3.8", "imagemurl": "https://m.media-amazon.com/images/I/51x5pI72zEL.jpg", "sinopse": "Se você gosta do clima de fim de ano e tudo o que ele envolve, presentes, árvores enfeitadas, luzes pisca-pisca, beijo à meia-noite, vai se apaixonar pelo livro. Nestas doze histórias escritas por alguns dos mais populares autores da atualidade, há um pouco de tudo, não importa se você comemora o Natal, o Ano Novo, o Chanucá ou o solstício de inverno. Casais de formam, famílias se reencontram, seres mágicos surgem e desejos impossíveis se realizam. O pessimismo não tem lugar neste livro, afinal o Natal é época de esperança."},
    {"nomelivro": "Um Conto de Natal", "autor": "Charles Dickens", "ano": "2019", "genero": "Clássico", "paginas": "312", "editora": "Antofágica", "skoob": "4.3", "imagemurl": "https://images-na.ssl-images-amazon.com/images/I/61HXgejhsaL.jpg", "sinopse": "Scrooge é um homem avarento, muquirana, miserável e mão de vaca. Para ele, até mesmo o Natal parece um enorme desperdício de tempo e de dinheiro. Em mais uma lastimável noite natalina, o fantasma de seu sócio Marley aparece para assombrá-lo e lhe fazer um alerta: Scrooge será assombrado por três espíritos, que lhe mostrarão seus erros (e as consequências deles) no Natal passado, presente e futuro."},
    {"nomelivro": "Sete Dias Juntos", "autor": "Francesca Hornak", "ano": "2020", "genero": "Romance", "paginas": "364", "editora": "Bertrand Brasil", "skoob": "3.7", "imagemurl": "https://images-na.ssl-images-amazon.com/images/I/71zRsIOH7IL.jpg", "sinopse": "Uma semana é muito tempo para passar com a família... \n A família Birch irá se reunir em Weyfield Hall, para o Natal, pela primeira vez em muitos anos. Emma está eufórica com a chegada da filha mais velha, Olivia, mesmo sabendo que o único motivo para o seu regresso é a quarentena à qual deverá se submeter após ter sido voluntária no tratamento de uma epidemia devastadora na África. \n Enquanto Emma se esforça para parecer tranquila e para agradar a filha recém-chegada, seu marido, Andrew, jornalista e renomado crítico de restaurantes, passa os dias isolado em seu escritório, revirando o passado e revivendo seus dias de glória como um correspondente de guerra. Phoebe, a filha mais nova, vive em um mundo frívolo que gira somente ao seu redor, e durante a quarentena se dedica de forma obsessiva à organização de sua cerimônia de casamento, para o desgosto de Olivia que tenta superar o choque cultural causado pelo contraste entre os luxos da vida de sua família e as mazelas de um país subdesenvolvido. \n Pelos próximos sete dias ninguém poderá entrar nem sair da casa. Isolados do mundo e presos à companhia indesejada uns dos outros, uma semana pode se tornar uma eternidade para os Birch. Especialmente quando todos têm segredos a esconder. \n Um deles prestes a bater à porta."},
]
####
livros_lidos = []
####
@app.route('/')
def index():
    return render_template('index.html', livros=livros)
####
@app.route('/create')
def create():
    return render_template('create.html')
####
@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    nomelivro = request.form['nomelivro']   
    autor = request.form['autor'] 
    genero = request.form['genero'] 
    editora = request.form['editora']
    paginas = request.form['paginas']
    ano = request.form['ano']  
    skoob = request.form['skoob']     # <input name="texto"/>
    urlimage = request.form['imagemurl']
    sinopse = request.form['sinopse']
    livro = { "nomelivro": nomelivro, "autor": autor, "genero": genero, "editora": editora, "paginas": paginas, "ano": ano, "skoob": skoob, "imagemurl": urlimage, "sinopse": sinopse }
    livros.append(livro)

    return redirect('http://127.0.0.1:5000')
####
@app.route('/search', methods=['POST'])
def search():
    search = request.form['search']
    filtropesquisa = request.form['filtropesquisa']
    return render_template('search.html', search=search, livros=livros, tipopesquisa=filtropesquisa)
####
@app.route('/livrosconcluidos')
def livrostrue():
    return render_template('livrosconcluidos.html', livroslidos = livros_lidos)
####
@app.route('/livroinfo', methods=['POST'])
def livroinfo():
    index = request.form['index']
    index = int(index)
    return render_template('livroinfo.html', livros=livros, indexe=index)
####
@app.route('/concluida', methods=['POST'])
def concluida():
    index = request.form['index']
    index = int(index)
    livros_lidos.append(livros[index])
    livros.pop(index)
    return redirect('http://127.0.0.1:5000')
####
@app.route('/limparlista')
def limparlista():
    livros_lidos.clear()
    return render_template('livrosconcluidos.html', livroslidos = livros_lidos)
###
@app.route('/deletar', methods=['POST'])
def deletar():
    index = request.form['index']
    index = int(index)
    livros.pop(index)
    return redirect('http://127.0.0.1:5000')
### Update da lista ###
@app.route('/update', methods=['POST'])
def update():
    index = request.form['index']
    index = int(index)
    return render_template('updatelivro.html', indexe=index, livros=livros)
##salvar update##
@app.route('/atualizar', methods=['POST'])
def atualizar():
    index = request.form['index']
    index = int(index)
    ###
    livros[index]['nomelivro'] = request.form['nomelivro']
    livros[index]['autor'] = request.form['autor']
    livros[index]['genero'] = request.form['genero']
    livros[index]['editora'] = request.form['editora']
    livros[index]['paginas'] = request.form['paginas']
    livros[index]['ano'] = request.form['ano']
    livros[index]['skoob'] = request.form['skoob']
    livros[index]['imagemurl'] = request.form['imagemurl']
    livros[index]['sinopse'] = request.form['sinopse']
    return redirect('http://127.0.0.1:5000')
# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)