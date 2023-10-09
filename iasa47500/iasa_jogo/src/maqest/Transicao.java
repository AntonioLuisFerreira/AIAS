package maqest;

/**
 * 
 * A classe representa uma transição entre dois estados de uma Máquina de Estados.
 * Tem conhecimento do estado de destino para onde a transição leva e das ações que devem ser executadas quando essa transição ocorrer.
 * Ou seja, a classe descreve a passagem de um estado para outro e sabe o que deve ser feito quando essa transição acontecer.
 * 
 * @param <EV> Mapeado com tipo Evento
 * @param <AC> Mapeado com tipo de Accao
 */

public class Transicao<EV, AC> {
	
	
	/**
	 * Atributos privados
	 * estadoSucessor
	 * accao
	 */
	private Estado<EV,AC> estadoSucessor;
	private AC accao;
	
	/**
	 * Método construtor da classe Transicao
	 * 
	 * @param estadoSucessor
	 * @param accao
	 * 
	 * guarda os parametros como atributos
	 */
	public Transicao(Estado<EV,AC> estadoSucessor, AC accao) {
		this.estadoSucessor = estadoSucessor;
		this.accao = accao;
	}
	
	/**
	 * Método getter do estado atual
	 * 
	 * @return estadoAtual
	 */
	public Estado<EV, AC> getEstadoSucessor() {
		return estadoSucessor;
	}
	
	/**
	 * Método getter da ação
	 * 
	 * @return accao
	 */
	public AC getAccao() {
		return accao;
	}
}
