package jogo.personagem;

import jogo.ambiente.Evento;
import maqest.Estado;
import maqest.MaquinaEstados;

/**
 * A classe Controlo é responsável por permitir que a personagem interaja com o
 * ambiente em que está inserida, utilizando as informações coletadas pelo
 * objeto da classe Percepcao.
 * 
 * Além disso, essa classe utiliza um objeto da classe MaquinaEstados,
 * que é um modelo que define o comportamento da personagem,
 * indicando os possíveis estados que ela pode assumir e as ações
 * que podem ser realizadas para transitar de um estado para outro.
 * 
 * @author amvlf
 *
 */

public class Controlo {

	/**
	 * Método construtor da classe Controlo
	 * Cria 4 estados, procura, inspeccao, observacao, registo
	 * Respeitando o diagrama UML é feito as transicoes possíveis para cada estados
	 */
	
	public Controlo() {
		Estado<Evento, Accao> procura = new Estado<>("Procura");
		Estado<Evento, Accao> inspeccao = new Estado<>("Inspecção");
		Estado<Evento, Accao> observacao = new Estado<>("Observação");
		Estado<Evento, Accao> registo = new Estado<>("Registo");

		//Estados
		procura
			.transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
			.transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
			.transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

		inspeccao
			.transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
			.transicao(Evento.RUIDO, inspeccao, Accao.PROCURAR)
			.transicao(Evento.SILENCIO, procura);

		observacao
			.transicao(Evento.ANIMAL, registo, Accao.OBSERVAR)
			.transicao(Evento.FUGA, inspeccao);

		registo
			.transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR)
			.transicao(Evento.FUGA, procura)
			.transicao(Evento.FOTOGRAFIA, procura);

		//Instanciar a máquina de estados, passando como estado inicial o estado de procura
		maqEst = new MaquinaEstados<>(procura);
	}

	// Atributo privado que faz referência à classe MaquinaEstados
	private MaquinaEstados<Evento, Accao> maqEst;

	/**
	 * Método getter do estado que está na máquina de estados.
	 * @return maqEst.getEstado()
	 */
	public Estado<Evento, Accao> getEstado() {
		return maqEst.getEstado();
	}

	/**
	 * Método processar faz com que a personagem, de acordo com a percepção que tem do ambiente,
	 * poder saber reagir conforme pretendido.
	 * 
	 * Vai buscar o evento actual à percepção e em conforme a máquina de estados ativa-se o processamento obtendo 
	 * 
	 * @param percepcao
	 * @return accao
	 */
	public Accao processar(Percepcao percepcao) {
		Evento evento = percepcao.getEvento();
		Accao accao   = maqEst.processar(evento);
		mostrar();
		return accao;
	}

	/**
	 * É um método privado que faz print na consola do nome do estado em UpperCase
	 */
	private void mostrar() {
		System.out.println("Estado: " + getEstado().getNome().toUpperCase());
	}
}
