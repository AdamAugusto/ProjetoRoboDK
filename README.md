# ProjetoRoboDK
Projeto de Robótica desenvolvido em Python na Ferramente Robodk


Adam Augusto Lauriano Ferreira


O Projeto consiste em um ambiente criado no software Robodk, cujo o ambiente consiste em 2 mesas de trabalho, uma placa (simulando uma chapa metálica) e 2 Robôs,
o primeiro Robô tem como ferramenta um laser de corte e como função o corte da chapa metálica no formato da palavra que for digitada, já no segundo sua ferramente é um griper de vácuo e sua função e levar a chapa até a estação de trabalho e retirá-la da mesma.
O mainProgram, que está no GitHub, é o controle do primeiro robô, ele tem definido as coordenadas cartesianas de cada letra do alfabeto e as funções para desenhar as letras, uma genérica para as letras que não possuem curvas como o A, E, F, etc... E então uma específica para cada letra que possue curvatura, como B, C, D, etc...
O controle do Robô 2 é dividido em 3 programas, "Pega Peça", "Volta Home", "Leva Peça", 
