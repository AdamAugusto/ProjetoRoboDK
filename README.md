# ProjetoRoboDK
Projeto de Robótica desenvolvido em Python na Ferramente Robodk


Adam Augusto Lauriano Ferreira


O Projeto (Atividade1.rdk) consiste em um ambiente criado no software Robodk, cujo o ambiente consiste em 2 mesas de trabalho, uma placa (simulando uma chapa metálica) e 2 Robôs, e a programação em python para atuar como o controle de ambos os robôs.
O primeiro Robô tem como ferramenta um laser de corte e como função o corte da chapa metálica no formato da palavra que for digitada, já no segundo sua ferramente é um griper de vácuo e sua função e levar a chapa até a estação de trabalho e retirá-la da mesma.
O mainProgram, que está no GitHub e dentro do Atividade1.rdk ele estará com o nome de Prog1, é o controle do primeiro robô, ele tem definido as coordenadas cartesianas de cada letra do alfabeto e as funções para desenhar as letras, uma genérica para as letras que não possuem curvas como o A, E, F, etc... E então uma específica para cada letra que possue curvatura, como B, C, D, etc...
O controle do Robô 2 é dividido em 3 programas, "Pega Peça", "Volta Home", "Leva Peça", estes estão apenas no arquivo Atividade1.rdk, pois são comandos simples, o "Pega Peça" consiste em uma cadeia de comandos para direcionar o braço robótico, que possuí o gripper de vácuo, até a peça na bancada, "Volta Home" para retornar o braço, com a peça ou sem caso ele já tenha a levado, ao target nomeado de "Home", "Leva Peça" é para mover o braço até a bancada de trabalho, onde o outro robô realizará o corte.
Dentro do Atividade1.rdk existe também um outro programa, chamado Prog3, este é uma simulação da cadeia de comandos que existiria numa linha de produção, chamando na ordem cada um dos programas explicados anteriormente, além de uma função específica do RoboDk que simula a peça presa ao gripper e outra que solta a peça do mesmo, chamadas de Attach to Robot e Detach from Robot.
